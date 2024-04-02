from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)
user_db = os.environ.get('USER_DB')
paswor_db = os.environ.get('PASWOR_DB')

from sqlalchemy import ForeignKey
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from typing import AsyncGenerator
# from keys import user_db, paswor_db


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
    name_room = Column(sqlalchemy.String(100), nullable=True)
    country = Column(sqlalchemy.String(100), nullable=True)
    city = Column(sqlalchemy.String(50), nullable=True)
    address_room = Column(sqlalchemy.String(200), nullable=True)
    url_room = Column(sqlalchemy.String(200), nullable=True)
    image_url = Column(sqlalchemy.String(200), nullable=True)
    guest = Column(sqlalchemy.String(100), nullable=True)
    bedrooms = Column(sqlalchemy.String(100), nullable=True)
    beds = Column(sqlalchemy.String(100), nullable=True)
    bathrooms = Column(sqlalchemy.String(100), nullable=True)
    owner = Column(sqlalchemy.String(100), nullable=True)
    conveniences = Column(sqlalchemy.String(100), nullable=True)
    important_info = Column(sqlalchemy.String(100), nullable=True)
    cancellation_policy = Column(sqlalchemy.String(100), nullable=True)
    currency = Column(sqlalchemy.String(10), default="USD", server_default="USD", nullable=False)
    night_price = Column(sqlalchemy.Float, default=0, server_default="0", nullable=False)
    date_of_update = Column(sqlalchemy.DateTime, nullable=True)

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