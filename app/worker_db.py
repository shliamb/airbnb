from sqlalchemy import select, insert, update, join, func
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base, Users, Airbnb, Airdna, Task, Id, Point, Map
from keys import user_db, paswor_db
import sqlalchemy
import asyncio
import logging
import os




async def create_async_engine_and_session():                               # @postgres  # @localhost
    engine = create_async_engine(f"postgresql+asyncpg://{user_db}:{paswor_db}@postgres:5432/my_database") # echo=True - вывод логирования
    async_session = sessionmaker(bind=engine, class_=AsyncSession) #, autoflush=True, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return async_session
####





############################################
#               Проверенные                #
#                                          #


#### POINT #### 

# Read POINT
async def get_point(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Point).filter(Point.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()
        logging.info(f"info: Read point")
        return data or None

# Update POINT
async def update_point(id: int, data) -> bool: 
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Point).where(Point.id == id).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"info: point is update")
        except Exception as e:
            logging.error(f"Error: Failed to update point, error: {e}")
    return confirmation

# Add POINT
async def adding_point(data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Point).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("info: Adding point DB")
        except Exception as e:
            logging.error(f"Error: Failed to add point, errror: {e}")
    return confirmation
####

#### ID #### 

# Read Data for ID
async def get_id(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Id).filter(Id.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()
        logging.info(f"info: Read data for ID")
        return data or None

# Update Data for ID
async def update_id(id: int, data) -> bool: 
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Id).where(Id.id == id).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"info: The ID is update")
        except Exception as e:
            logging.error(f"Error: Failed to update table ID, error: {e}")
    return confirmation

# Add Data for ID
async def adding_id(data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Id).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("info: Adding a Table ID")
        except Exception as e:
            logging.error(f"Error: Failed to add a Table ID, errror:: {e}")
    return confirmation

# Read count id's at Table ID 
async def get_10_id_false(count):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = (
            select(Id)
            .filter(Id.passed_flag == False)
            .filter(Id.busy_flag == False)
            .limit(count) # Максимальное значение - count
        )
        result = await session.execute(query)
        data = result.scalars().all()  
        return data



#### AIRBNB #### - таблица с параметрами объекта 

# Read data airbnb
async def get_airbnb(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Airbnb).filter(Airbnb.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()
        logging.info(f"info: Reading data at table airbnb")
        return data or None

# Update Data aibnb
async def update_airbnb(id: int, data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Airbnb).where(Airbnb.id == id).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"info: Update data at table airbnb")
        except Exception as e:
            logging.error(f"Error: Failed to Update data at table airbnb, error: {e}")
    return confirmation

# Add data airbnb
async def adding_airbnb(data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Airbnb).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("info: Data airbnb is added")
        except Exception as e:
            logging.error(f"Error: Failed to add data airbnb, error: {e}")
    return confirmation




########## Map ###########

# Read data Map
async def get_map(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Map).filter(Map.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()
        logging.info(f"info: Reading data at table map")
        return data or None

# Update Data Map
async def update_map(id: int, data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Map).where(Map.id == id).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"info: Update data at table map")
        except Exception as e:
            logging.error(f"Error: Failed to Update data at table map, error: {e}")
    return confirmation

# Add data Map
async def adding_map(data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Map).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("info: Data map is added")
        except Exception as e:
            logging.error(f"Error: Failed to add data map, error: {e}")
    return confirmation




#### AIRDNA #### 

# Read Airdna
async def get_airdna(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Airdna).filter(Airdna.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()
        logging.info(f"info: Read Airdna data")
        return data or None

# Get ALL Airdna
async def get_all_airdna():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Airdna)
        result = await session.execute(query)
        data = result.scalars().all()
        logging.info(f"info: Read all Airdna data")
        return data or None

# Update Airdna
async def update_airdna(id: int, data) -> bool: 
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Airdna).where(Airdna.id == id).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"info: Data Airdna is update")
        except Exception as e:
            logging.error(f"Error: Failed to update data Airdna, error: {e}")
    return confirmation

# Add Airdna
async def adding_airdna(data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Airdna).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("info: Adding data Airdna DB")
        except Exception as e:
            logging.error(f"Error: Failed to add data Airdna, errror:: {e}")
    return confirmation


# Read table Airna join ID 
async def get_all_airdna_id_join():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = (
            select(Airdna, Id, Map)
            .outerjoin(Id, Airdna.id == Id.id)  # Убедитесь, что используете правильные поля для соединения
            .outerjoin(Map, Airdna.id == Map.id)  # Убедитесь, что используете правильные поля для соединения
            .where(Airdna.location_lat != 0)
            .where(Airdna.location_lng != 0)
            .where(Id.id.isnot(None))  # Используйте isnot(None) для проверки на не NULL
            .where(Map.id.is_(None))  # Используйте is_(None) для проверки на NULL
        )
        result = await session.execute(query)
        data = result.all()
        return data





#                                          #
#               Проверенные                #
############################################










































#
#
# Additional functions
#
#

# Read All Airbnb hwo Title is not None
async def get_all_rooms_not_None():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Airbnb)# .filter(Airbnb.title.isnot(None))
        result = await session.execute(query)
        data = result.scalars().all()  # Получение всех записей
        return data # Если не будет записей, то вернет пустой список

# EXEL Read All Airbnb and Airdna whith hes is hwo - забирает таблицу Airbnb и по id забирает с Airdna если оно есть там, для exel
async def get_all_airbnb_airdna():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = (
            select(Airbnb, Airdna)
            .outerjoin(Airdna, Airbnb.id == Airdna.id)  # Предполагаем что поле для соединения это 'id'
        )
        result = await session.execute(query)
        data = result.all()
        #data = result.scalars().all()
        return data

# Get_rooms_sorted_by_bedroom_asc
async def get_all_airbnb_airdna_sorted_bedroom_asc():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = (
            select(Airbnb, Airdna)
            .outerjoin(Airdna, Airbnb.id == Airdna.id)  # Предполагаем что поле для соединения это 'id'
            .order_by(Airbnb.bedroom.asc()) # asc() # desc()
        )
        result = await session.execute(query)
        rooms_sorted = result.all()  # Получаем отсортированный список комнат
        return rooms_sorted

# Get_rooms_sorted_by_bedroom_desc
async def get_all_airbnb_airdna_sorted_bedroom_desc():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = (
            select(Airbnb, Airdna)
            .outerjoin(Airdna, Airbnb.id == Airdna.id)  # Предполагаем что поле для соединения это 'id'
            .order_by(Airbnb.bedroom.desc()) # asc() # desc()
        )
        result = await session.execute(query)
        rooms_sorted = result.all()  # Получаем отсортированный список комнат
        return rooms_sorted









# # Read All Rooms For Location
# async def get_rooms_by_location(country: int):
#     async_session = await create_async_engine_and_session()
#     async with async_session() as session:
#         query = select(Airbnb).filter(Airbnb.location == country)
#         result = await session.execute(query)
#         data = result.scalars().all()  # Получение всех записей
#         return data # Если не будет записей, то вернет пустой список
    
# # Read All Rooms
# async def get_all_rooms():
#     async_session = await create_async_engine_and_session()
#     async with async_session() as session:
#         query = select(Airbnb)
#         result = await session.execute(query)
#         data = result.scalars().all()  # Получение всех записей
#         return data # Если не будет записей, то вернет пустой список


# # Read All Rooms
# async def get_all_rooms():
#     async_session = await create_async_engine_and_session()
#     async with async_session() as session:
#         query = select(Airbnb)
#         result = await session.execute(query)
#         data = result.scalars().all()
#         return data

# # Get Count All Rooms hwo not None
# async def get_count_rooms_not_None():
#     async_session = await create_async_engine_and_session()
#     async with async_session() as session:
#         # Используем func.count() для подсчета записей
#         query = select(func.count()).select_from(Airbnb).filter(Airbnb.title_room.isnot(None))
#         result = await session.execute(query)
#         count = result.scalar()  # Получаем количество записей как скалярное значение
#         return count

# # Get_rooms_sorted_by_price_asc
# async def get_rooms_sorted_by_price_asc():
#     async_session = await create_async_engine_and_session()
#     async with async_session() as session:
#         # Добавляем сортировку записей по цене за ночь от меньшей к большей
#         query = select(Airbnb).filter(Airbnb.title_room.isnot(None)).order_by(Rooms.night_price.asc()) # desc()
#         result = await session.execute(query)
#         rooms_sorted = result.scalars().all()  # Получаем отсортированный список комнат
#         return rooms_sorted

# # Get_rooms_sorted_by_bedroom_desc
# async def get_rooms_sorted_by_bedroom_desc():
#     async_session = await create_async_engine_and_session()
#     async with async_session() as session:
#         # Добавляем сортировку записей по цене за ночь от меньшей к большей
#         query = select(Airbnb).filter(Airbnb.title_room.isnot(None)).order_by(Rooms.bedroom.desc()) # asc() # desc()
#         result = await session.execute(query)
#         rooms_sorted = result.scalars().all()  # Получаем отсортированный список комнат
#         return rooms_sorted

####









#
#
# Additional functions
#
#

# Read ALL ID by Passed is False
async def get_id_passed_false_count():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        count_query = (
            select(func.count('*'))
            .select_from(Id)  # Указываем таблицу
            .filter(Id.passed_flag == False)
        )
        result = await session.execute(count_query)
        count = result.scalar_one()
        return count

# Read ALL coint good
async def get_all_airbnb_airdna_good_count():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = (
            select(func.count('*'))
            .select_from(Airbnb, Airdna)
            .outerjoin(Airdna, Airbnb.id == Airdna.id)  # Предполагаем что поле для соединения это 'id'
            .filter(Airbnb.location != "")
            .filter(Airbnb.bedroom != None)
        )
        result = await session.execute(query)
        data = result.scalar_one()
        return data

# async def get_id_passed_false_count():
#     async_session = await create_async_engine_and_session()
#     async with async_session() as session:
#         count_query = (
#             select(func.count('*'))  # Или func.count(Id.id), если нужно подсчитать по столбцу id
#             .select_from(Id)  # Указываем таблицу
#             .filter(Id.passed_flag == 0)  # Условие фильтрации
#         )
#         result = await session.execute(count_query)
#         count = result.scalar_one()  # Получаем результат запроса
#         return count

# Get_rooms_sorted_by_bedroom_desc
async def get_all_airbnb_airdna_sorted_bedroom_desc():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = (
            select(Airbnb, Airdna)
            .outerjoin(Airdna, Airbnb.id == Airdna.id)  # Предполагаем что поле для соединения это 'id'
            .order_by(Airbnb.bedroom.desc()) # asc() # desc()
        )
        result = await session.execute(query)
        rooms_sorted = result.all()  # Получаем отсортированный список комнат
        return rooms_sorted




# Read all id's at Table ID 
async def get_all_id_false():
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Id).filter(Id.passed_flag == False)
        result = await session.execute(query)
        data = result.scalars().all()  
        return data
    
# Update ALL ID Data
async def update_all_id(data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Id).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"info: All data ID Table is updated")
        except Exception as e:
            logging.error(f"Error: Failed to update data ID Table, error: {e}")
    return confirmation
####




# #### FLAG #### 

# # Read Data for FLAG
# async def get_flag(id: int):
#     async_session = await create_async_engine_and_session()
#     async with async_session() as session:
#         query = select(Flag).filter(Flag.id == id)
#         result = await session.execute(query)
#         data = result.scalar_one_or_none()
#         logging.info(f"Read data for Flag")
#         return data or None

# # Update Data for FLAG
# async def update_flag(id: int, data) -> bool: 
#     async_session = await create_async_engine_and_session()
#     confirmation = False
#     async with async_session() as session:
#         try:
#             query = update(Flag).where(Flag.id == id).values(**data)
#             await session.execute(query)
#             await session.commit()
#             confirmation = True
#             logging.info(f"The Flag is update")
#         except Exception as e:
#             logging.error(f"Failed to update table Flag, error: {e}")
#     return confirmation

# # Add Data for Flag
# async def adding_flag(data) -> bool:
#     async_session = await create_async_engine_and_session()
#     confirmation = False
#     async with async_session() as session:
#         try:
#             query = insert(Flag).values(**data)
#             await session.execute(query)
#             await session.commit()
#             confirmation = True
#             logging.info("Adding a Table Flag")
#         except Exception as e:
#             logging.error(f"Failed to add a Table Flag, errror: {e}")
#     return confirmation

#
#
# Additional functions
#
#







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
####




#### USERS PROPERTY #### 

# Read User
async def get_users(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Users).filter(Users.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()  # - это метод SQLAlchemy, который возвращает ровно один результат из результата запроса или None, если запрос не вернул ни одного результата.
        logging.info(f"info: Read Users")
        return data or None

# Update User Data
async def update_users(id: int, data) -> bool: 
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Users).where(Users.id == id).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"info: User data is update")
        except Exception as e:
            logging.error(f"Error: Failed to update user data, error: {e}")
    return confirmation

# Add User Data to DB
async def adding_users(data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Users).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("info: User data is add")
        except Exception as e:
            logging.error(f"Error: Failed to add user data, error: {e}")
    return confirmation
####




#### Task #### 

# Read Task
async def get_task(id: int):
    async_session = await create_async_engine_and_session()
    async with async_session() as session:
        query = select(Task).filter(Task.id == id)
        result = await session.execute(query)
        data = result.scalar_one_or_none()
        logging.info(f"info: Read Task")
        return data or None

# Update Task
async def update_task(id: int, data) -> bool: 
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = update(Task).where(Task.id == id).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info(f"info: Task is update by user: {id}")
        except Exception as e:
            logging.error(f"Error: Failed to update task, error: {e}")
    return confirmation

# Add Task
async def adding_task(data) -> bool:
    async_session = await create_async_engine_and_session()
    confirmation = False
    async with async_session() as session:
        try:
            query = insert(Task).values(**data)
            await session.execute(query)
            await session.commit()
            confirmation = True
            logging.info("info: Adding one task to DB")
        except Exception as e:
            logging.error(f"Error: Failed to add task, errror:: {e}")
    return confirmation



