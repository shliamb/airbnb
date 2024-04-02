from worker_db import get_rooms_by_id, adding_rooms
import requests
import asyncio











## Work at DB
# Добавляем в базу тестово
async def add_rooms(data) -> bool:
    a = await adding_rooms(data)
    return print(a)

data = {
    "id": 13434,
    "name_room": "Дом на дереве, Gaular",
    "country": "Норвегия",
    "bedrooms": "3",
    "night_price": 150,
}

asyncio.run(add_rooms(data))


#  Забираем из базы тестово
async def read_rooms():
    id = 13434
    data = await get_rooms_by_id(id)
    print(data.country)

# asyncio.run(read_rooms())