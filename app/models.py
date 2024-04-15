import os
from sqlalchemy import ForeignKey
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from typing import AsyncGenerator
# from keys import user_db, paswor_db

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
user_db, paswor_db = os.environ.get('USER_DB'),  os.environ.get('PASWOR_DB')


#DATABASE_URL = f"postgresql+asyncpg://{user_db}:{paswor_db}@postgres:5432/my_database"
DATABASE_URL = f"postgresql+asyncpg://{user_db}:{paswor_db}@localhost:5432/my_database"
engine = create_async_engine(DATABASE_URL)
Base = declarative_base()
Column = sqlalchemy.Column
####



# ID - id и url объекта, не связанная таблица. id в таблицах FLAG, AIRBNB, ARBDNA, ID - это одно и то же, но в разном порядке
class Id(Base):
    __tablename__ = 'id'
    id = Column(sqlalchemy.BigInteger, primary_key=True, unique=True, nullable=False, index=True)
    url = Column(sqlalchemy.String(5000), nullable=False, index=True)
    busy_flag = Column(sqlalchemy.Boolean, default=False, server_default="False", nullable=False, index=True) # для пометки уже взятых id в работу, в случае, если будут работать больше одной копии
    passed_flag = Column(sqlalchemy.Boolean, default=False, server_default="False", nullable=False, index=True) # пометка, что пропарсена
    date = Column(sqlalchemy.DateTime, nullable=True)

# POINT - точка остановки (от 10$ до 11$) сбора списков объектов
class Point(Base):
    __tablename__ = 'point'
    id = Column(sqlalchemy.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True, index=True)
    date = Column(sqlalchemy.DateTime, nullable=True)
    price_min = Column(sqlalchemy.Integer, default=10, server_default="10", nullable=False, index=True)
    price_max = Column(sqlalchemy.Integer, default=11, server_default="11", nullable=False, index=True)
    currency = Column(sqlalchemy.String(10), default="USD", server_default="USD", nullable=False)

# AIRBNB - параметры объектов, не связанная таблица.
class Airbnb(Base):
    __tablename__ = 'airbnb'
    id = Column(sqlalchemy.BigInteger, primary_key=True, unique=True, nullable=False, index=True)
    url = Column(sqlalchemy.String(5000), nullable=False) # - дублируется, усложения в этом нет, так как при парсе объекта из таблицы ID забирается id и url, который можно закидывать в таблицу AIRBNB за одно, для того, что бы потом одним запросом забирать его.
    title = Column(sqlalchemy.String(3000), nullable=True)
    name = Column(sqlalchemy.String(3000), nullable=True)
    type_house = Column(sqlalchemy.String(3000), nullable=True)
    night_price = Column(sqlalchemy.Float, default=0, server_default="0", nullable=False)
    month_price = Column(sqlalchemy.Float, default=0, server_default="0", nullable=False)
    currency = Column(sqlalchemy.String(10), default="USD", server_default="USD", nullable=False)
    rating = Column(sqlalchemy.Float, nullable=True)
    reviews = Column(sqlalchemy.Integer, nullable=True)
    guest_favorite = Column(sqlalchemy.Float, nullable=True)
    guest = Column(sqlalchemy.Integer, nullable=True)
    bedroom = Column(sqlalchemy.Integer, nullable=True)
    bed = Column(sqlalchemy.Integer, nullable=True)
    bath = Column(sqlalchemy.Float, nullable=True)
    parking = Column(sqlalchemy.String(3000), nullable=True)
    kitchen = Column(sqlalchemy.String(3000), nullable=True)
    view = Column(sqlalchemy.String(3000), nullable=True)
    workspace = Column(sqlalchemy.String(3000), nullable=True)
    rooftop = Column(sqlalchemy.String(3000), nullable=True)
    terrace_balcony = Column(sqlalchemy.String(3000), nullable=True)
    restaurants = Column(sqlalchemy.String(3000), nullable=True)
    storage = Column(sqlalchemy.String(3000), nullable=True)
    sqm = Column(sqlalchemy.String(3000), nullable=True)
    location = Column(sqlalchemy.String(3000), nullable=False)
    date_update = Column(sqlalchemy.DateTime, nullable=True)
    date = Column(sqlalchemy.DateTime, nullable=True)

# AIRDNA - параметры объектов, не связанная таблица, заливается сразу из json.
class Airdna(Base):
    __tablename__ = 'airdna'
    id = Column(sqlalchemy.BigInteger, primary_key=True, unique=True, nullable=False, index=True)
    revenue_ltm = Column(sqlalchemy.BigInteger, nullable=True)
    revenue_potential_ltm = Column(sqlalchemy.BigInteger, nullable=True)
    occupancy_rate_ltm = Column(sqlalchemy.Float, nullable=True)
    average_daily_rate_ltm = Column(sqlalchemy.BigInteger, nullable=True)
    days_available_ltm = Column(sqlalchemy.BigInteger, nullable=True)
    location_lat = Column(sqlalchemy.Float, nullable=True)
    location_lng = Column(sqlalchemy.Float, nullable=True)
    date = Column(sqlalchemy.DateTime, nullable=True)

# MAP - из API будет андрес текстом и дублироваться url, location_lat, location_lng
class Map(Base):
    __tablename__ = 'map'
    id = Column(sqlalchemy.BigInteger, primary_key=True, unique=True, nullable=False, index=True)
    title = Column(sqlalchemy.String(3000), nullable=True, index=True)
    description = Column(sqlalchemy.String(3000), nullable=True)
    url = Column(sqlalchemy.String(3000), nullable=True)
    location_lat = Column(sqlalchemy.Float, nullable=True, index=True)
    location_lng = Column(sqlalchemy.Float, nullable=True, index=True)
    date = Column(sqlalchemy.DateTime, nullable=True)

# TASK - автоматизированные задачи
class Task(Base):
    __tablename__ = 'task'
    id = Column(sqlalchemy.BigInteger, primary_key=True, unique=True, nullable=False, index=True)
    name_task = Column(sqlalchemy.String(3000), nullable=True)
    date_task = Column(sqlalchemy.DateTime, nullable=True)
    data_task = Column(sqlalchemy.String(3000), nullable=True)
    owner_task = Column(sqlalchemy.BigInteger, ForeignKey('users.id'), primary_key=True)
    ####
    users_task = relationship("Users", back_populates="task")

# USERS - настройки пользователя, что бы сохранялись параметры работы
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
    time_correction = Column(sqlalchemy.Integer, default=+5, server_default="+5", nullable=False) # +3 часа или - 4 часа пояса часового...
    # Настройки по умолчанию, что бы каждый раз не набирать
    checkin_date = Column(sqlalchemy.DateTime, nullable=True) # "2024-05-01"
    checkout_date = Column(sqlalchemy.DateTime, nullable=True) # "2024-05-07"
    country = Column(sqlalchemy.String(3000), default="Bali", server_default="Bali", nullable=False) # Bali - например, иначе потом хер найдешь
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






# # FLAG - устанавливается флаг, когда объект пропарсили, не связанная таблица.
# class Flag(Base):
#     __tablename__ = 'flag'
#     id = Column(sqlalchemy.BigInteger, primary_key=True, unique=True, nullable=False, index=True)
#     busy_flag = Column(sqlalchemy.Boolean, default=False, server_default="False", nullable=False) # для пометки уже взятых id в работу, в случае, если будут работать больше одной копии
#     passed_flag = Column(sqlalchemy.Boolean, default=False, server_default="False", nullable=False) # пометка, что пропарсена
#     date = Column(sqlalchemy.DateTime, nullable=True)