from worker_db import get_rooms_by_id#, adding_rooms
import asyncio



# async def add_rooms(data) -> bool:
#     a = await adding_rooms(data)
#     return a

# data = {
#     "id": 13433,
#     "name_room": "Дом на дереве, Gaular",
#     "country": "Норвегия",
#     "bedrooms": "3",
#     "night_price": 150,
# }

# asyncio.run(res = add_rooms(data))
# print(res)



# async def read_rooms():
#     data = await get_rooms_by_id(13433)
#     #print(data)
#     return

# # id = 13433
# asyncio.run(read_rooms())


async def read_rooms():
    id = 13433
    data = await get_rooms_by_id(id)
    print(data.country)

asyncio.run(read_rooms())