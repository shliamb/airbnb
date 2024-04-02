from keys import user_db, paswor_db
import logging
import asyncio
import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base, Users, Rooms, Task
from sqlalchemy import select, insert, update, join, func

async def create_async_engine_and_session():                               # localhost
    engine = create_async_engine(f"postgresql+asyncpg://{user_db}:{paswor_db}@postgres:5432/my_database") # echo=True - вывод логирования
    async_session = sessionmaker(bind=engine, class_=AsyncSession)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return async_session


#### USERS PROPERTY #### 
# Read User
async def get_users_by_id(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Users).filter(Users.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()  # - это метод SQLAlchemy, который возвращает ровно один результат из результата запроса или None, если запрос не вернул ни одного результата.
        return data or None

# Update User Data
async def update_users(id: int, updated_data) -> bool: 
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Users).where(Users.id == id).values(**updated_data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"User data is update")
        except Exception as e:
            logging.error(f"Failed to update user data, error: {e}")
    return confirmation

# Add User Data to DB
async def adding_users(user_data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Users).values(**user_data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("User data is add")
        except Exception as e:
            logging.error(f"Failed to add user data, error: {e}")
    return confirmation


#### ROOMS #### 
# Read Rooms Data
async def get_rooms_by_id(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Rooms).filter(Rooms.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()
        return data or None

# Update Rooms Data
async def update_rooms(id: int, updated_session) -> bool: 
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Rooms).where(Rooms.id == id).values(**updated_session)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"Rooms date is update")
        except Exception as e:
            logging.error(f"Failed to update rooms data, error: {e}")
    return confirmation

# Add User Session to DB
async def adding_rooms(session_data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Rooms).values(**session_data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("Rooms is add")
        except Exception as e:
            logging.error(f"Failed to add rooms, error: {e}")
    return confirmation


#### Task #### 
# Read Task
async def get_task_by_id(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Task).filter(Task.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()
        return data or None

# Update Task
async def update_task(id: int, updated_task_data) -> bool: 
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Task).where(Task.id == id).values(**updated_task_data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"Task is update by user: {id}")
        except Exception as e:
            logging.error(f"Failed to update task, error: {e}")
    return confirmation

# Add Task
async def adding_task(task_data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Task).values(**task_data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("Adding one task to DB")
        except Exception as e:
            logging.error(f"Failed to add task, errror:: {e}")
    return confirmation