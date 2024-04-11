import os
import logging
import asyncio
import sqlalchemy
from sqlalchemy import select, insert, update, join, func
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base, Users, Rooms, Task, Positions
from keys import user_db, paswor_db

# from dotenv import load_dotenv
# load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
# user_db, paswor_db = os.environ.get('USER_DB'),  os.environ.get('PASWOR_DB')

async def create_async_engine_and_session():                               # postgres
    engine = create_async_engine(f"postgresql+asyncpg://{user_db}:{paswor_db}@localhost:5432/my_database") # echo=True - вывод логирования
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
        logging.info(f"Read Users")
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
        logging.info(f"Read Rooms")
        return data or None

# Update Rooms Data
async def update_rooms(id: int, updated_data_room) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Rooms).where(Rooms.id == id).values(**updated_data_room)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"Rooms date is update")
        except Exception as e:
            logging.error(f"Failed to update rooms data, error: {e}")
    return confirmation


# Update ALL Rooms Data
async def update_all_rooms(updated_data_room) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Rooms).values(**updated_data_room)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"All rooms data is updated")
        except Exception as e:
            logging.error(f"Failed to update all rooms data, error: {e}")
    return confirmation


# Add Rooms to DB
async def adding_rooms(new_data_room) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Rooms).values(**new_data_room)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("Rooms is add")
        except Exception as e:
            logging.error(f"Failed to add rooms, error: {e}")
    return confirmation

# Read All Rooms For Location
async def get_rooms_by_location(country: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Rooms).filter(Rooms.location == country)
        result = await session.execute(query)
        data = result.scalars().all()  # Получение всех записей
        return data # Если не будет записей, то вернет пустой список
    
# Read All Rooms
async def get_all_rooms():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Rooms)
        result = await session.execute(query)
        data = result.scalars().all()  # Получение всех записей
        return data # Если не будет записей, то вернет пустой список

# Read All Rooms hwo Title is not None
async def get_all_rooms_not_None():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Rooms).filter(Rooms.title_room.isnot(None))
        result = await session.execute(query)
        data = result.scalars().all()  # Получение всех записей
        return data # Если не будет записей, то вернет пустой список

# Read All Rooms For False in is_parse
async def get_rooms_by_false_parse():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Rooms).filter(Rooms.is_parse == False)
        result = await session.execute(query)
        data = result.scalars().all()  # Получение всех записей
        return data # Если не будет записей, то вернет пустой список

# Read All Rooms
async def get_all_rooms():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Rooms)
        result = await session.execute(query)
        data = result.scalars().all()
        return data

# Get Count All Rooms hwo not None
async def get_count_rooms_not_None():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        # Используем func.count() для подсчета записей
        query = select(func.count()).select_from(Rooms).filter(Rooms.title_room.isnot(None))
        result = await session.execute(query)
        count = result.scalar()  # Получаем количество записей как скалярное значение
        return count

# Get_rooms_sorted_by_price_asc
async def get_rooms_sorted_by_price_asc():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        # Добавляем сортировку записей по цене за ночь от меньшей к большей
        query = select(Rooms).filter(Rooms.title_room.isnot(None)).order_by(Rooms.night_price.asc()) # desc()
        result = await session.execute(query)
        rooms_sorted = result.scalars().all()  # Получаем отсортированный список комнат
        return rooms_sorted


# Get_rooms_sorted_by_bedroom_desc
async def get_rooms_sorted_by_bedroom_desc():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        # Добавляем сортировку записей по цене за ночь от меньшей к большей
        query = select(Rooms).filter(Rooms.title_room.isnot(None)).order_by(Rooms.bedroom.desc()) # asc() # desc()
        result = await session.execute(query)
        rooms_sorted = result.scalars().all()  # Получаем отсортированный список комнат
        return rooms_sorted



# Get_rooms_sorted_by_bedroom_asc
async def get_rooms_sorted_by_bedroom_asc():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        # Добавляем сортировку записей по цене за ночь от меньшей к большей
        query = select(Rooms).filter(Rooms.title_room.isnot(None)).order_by(Rooms.bedroom.asc()) # asc() # desc()
        result = await session.execute(query)
        rooms_sorted = result.scalars().all()  # Получаем отсортированный список комнат
        return rooms_sorted



#### Task #### 
# Read Task
async def get_task_by_id(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Task).filter(Task.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()
        logging.info(f"Read Task")
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



#### Positions #### 
# Read Positions
async def get_position(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Positions).filter(Positions.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()
        logging.info(f"Read Positions")
        return data or None

# Update Positions
async def update_position(id: int, updated_task_data) -> bool: 
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Positions).where(Positions.id == id).values(**updated_task_data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"Positions is update")
        except Exception as e:
            logging.error(f"Failed to update Positions, error: {e}")
    return confirmation

# Add Positions
async def adding_position(task_data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Positions).values(**task_data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("Adding Positionsto DB")
        except Exception as e:
            logging.error(f"Failed to add Positions, errror:: {e}")
    return confirmation
















# #### AIRDNA ####  
# # Read Airdna
# async def get_airdna(id: int):
#     async_session = await create_async_engine_and_session()
#     async with async_session() as session:
#         query = select(Airdna).filter(Airdna.id == id)
#         result = await session.execute(query)
#         data = result.scalar_one_or_none()
#         logging.info(f"Read Airdna data")
#         return data or None

# # Get ALL Airdna
# async def get_all_airdna():
#     async_session = await create_async_engine_and_session()
#     async with async_session() as session:
#         query = select(Airdna)
#         result = await session.execute(query)
#         data = result.scalars().all()
#         logging.info(f"Read all Airdna data")
#         return data or None

# # Update Airdna
# async def update_airdna(id: int, updated_task_data) -> bool: 
#     async_session = await create_async_engine_and_session()
#     confirmation = False
#     async with async_session() as session:
#         try:
#             query = update(Airdna).where(Airdna.id == id).values(**updated_task_data)
#             await session.execute(query)
#             await session.commit()
#             confirmation = True
#             logging.info(f"Data Airdna is update")
#         except Exception as e:
#             logging.error(f"Failed to update data Airdna, error: {e}")
#     return confirmation

# # Add Airdna
# async def adding_airdna(task_data) -> bool:
#     async_session = await create_async_engine_and_session()
#     confirmation = False
#     async with async_session() as session:
#         try:
#             query = insert(Airdna).values(**task_data)
#             await session.execute(query)
#             await session.commit()
#             confirmation = True
#             logging.info("Adding data Airdna DB")
#         except Exception as e:
#             logging.error(f"Failed to add data Airdna, errror:: {e}")
#     return confirmation

# # ADMIN Read all settings and users an id
# async def get_all_rooms_and_airdna():
#     async_session = await create_async_engine_and_session()
#     async with async_session() as session:

#         query = (
#             select(Rooms, Airdna)
#             .join(Airdna)
#         )

#         # for user_telegram, settings in data:
#         #     print("User:", user_telegram.id, user_telegram.is_admin, user_telegram.full_name,\
#         #            user_telegram.name)
#         #     print("Settings:", settings.id, settings.temp_chat, settings.money)
#         result = await session.execute(query)
#         data = result.fetchall()  # Получение всех строк
#         return data
