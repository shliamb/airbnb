import os
from sqlalchemy import ForeignKey
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from typing import AsyncGenerator
from keys import user_db, paswor_db

# from dotenv import load_dotenv
# load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
# user_db, paswor_db = os.environ.get('USER_DB'),  os.environ.get('PASWOR_DB')


#DATABASE_URL = f"postgresql+asyncpg://{user_db}:{paswor_db}@postgres:5432/my_database"
DATABASE_URL = f"postgresql+asyncpg://{user_db}:{paswor_db}@localhost:5432/my_database"
engine = create_async_engine(DATABASE_URL)
Base = declarative_base()
Column = sqlalchemy.Column
####

# Rooms - Main
class Rooms(Base):
    __tablename__ = 'rooms_id'
    id = Column(sqlalchemy.BigInteger, primary_key=True, unique=True, nullable=False, index=True) # id rooms or any data id
    title_room = Column(sqlalchemy.String(500), nullable=True)
    name_room = Column(sqlalchemy.String(500), nullable=True)
    subtitle_room = Column(sqlalchemy.String(500), nullable=True)
    night_price = Column(sqlalchemy.Float, default=0, server_default="0", nullable=False)
    total_price = Column(sqlalchemy.Float, default=0, server_default="0", nullable=False)
    currency = Column(sqlalchemy.String(10), default="USD", server_default="USD", nullable=False) # берем из настроек или url
    rating = Column(sqlalchemy.Float, nullable=True)
    place = Column(sqlalchemy.Integer, nullable=True)
    url_room = Column(sqlalchemy.String(2000), nullable=False) 
    image_url = Column(sqlalchemy.String(2000), nullable=True)
    country = Column(sqlalchemy.String(500), nullable=False) # Bali - например, иначе потом хер найдешь из настроек или url

    city = Column(sqlalchemy.String(50), nullable=True)
    address_room = Column(sqlalchemy.String(200), nullable=True)
    guest = Column(sqlalchemy.String(100), nullable=True)
    bedrooms = Column(sqlalchemy.String(100), nullable=True)
    beds = Column(sqlalchemy.String(100), nullable=True)
    bathrooms = Column(sqlalchemy.String(100), nullable=True)
    owner = Column(sqlalchemy.String(100), nullable=True)
    conveniences = Column(sqlalchemy.String(100), nullable=True)
    important_info = Column(sqlalchemy.String(100), nullable=True)
    cancellation_policy = Column(sqlalchemy.String(100), nullable=True)
    
    room_date_update = Column(sqlalchemy.DateTime, nullable=True) 
    rooms_date_update = Column(sqlalchemy.DateTime, nullable=True)

# Task
class Task(Base):
    __tablename__ = 'task'
    id = Column(sqlalchemy.BigInteger, primary_key=True, unique=True, nullable=False, index=True)
    name_task = Column(sqlalchemy.String(100), nullable=True)
    date_task = Column(sqlalchemy.DateTime, nullable=True)
    data_task = Column(sqlalchemy.String(3000), nullable=True)
    owner_task = Column(sqlalchemy.BigInteger, ForeignKey('users.id'), primary_key=True)
    ####
    users_task = relationship("Users", back_populates="task")

# Users
class Users(Base):
    __tablename__ = 'users'
    id = Column(sqlalchemy.BigInteger, primary_key=True, unique=True, nullable=False, index=True) # Telegram user_id or any else
    username = Column(sqlalchemy.String(50), nullable=False, unique=True)
    password = Column(sqlalchemy.String(100), nullable=False)
    email = Column(sqlalchemy.String(100), nullable=True, unique=True)
    date_reg = Column(sqlalchemy.DateTime, nullable=True)
    date_visit = Column(sqlalchemy.DateTime, nullable=True)
    is_admin = Column(sqlalchemy.Boolean, default=False, server_default="False", nullable=False)
    is_block = Column(sqlalchemy.Boolean, default=False, server_default="False", nullable=False)
    
    # +3 часа или - 4 часа пояса часового...
    # time_correction = Column(sqlalchemy.Integer, default=+5, server_default="+5", nullable=False)

    # Настройки по умолчанию, что бы каждый раз не набирать
    checkin_date = Column(sqlalchemy.DateTime, nullable=True) # "2024-05-01"
    checkout_date = Column(sqlalchemy.DateTime, nullable=True) # "2024-05-07"
    country = Column(sqlalchemy.String(100), default="Bali", server_default="Bali", nullable=False) # Bali - например, иначе потом хер найдешь
    guest = Column(sqlalchemy.Integer, default=0, server_default="0", nullable=False)
    currency = Column(sqlalchemy.String(10), default="USD", server_default="USD", nullable=False)
    ####
    task = relationship("Task", back_populates="users_task", uselist=False)






# Build Table to DB
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Creature session interactions to DB
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session