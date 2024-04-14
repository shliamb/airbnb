from worker_db import get_airdna, update_airdna, adding_airdna
import asyncio
import glob
import json
import os


async def process_data(item, semaphore):
    async with semaphore:  # Ожидание доступа к ресурсу
        #
        id = item.get('airbnb_property_id', 0)
        id = int(id) if id is not None else 0
        #
        revenue_ltm = item.get('revenue_ltm', 0)
        revenue_ltm = int(revenue_ltm) if revenue_ltm is not None else 0
        #
        revenue_potential_ltm = item.get('revenue_potential_ltm', 0)
        revenue_potential_ltm = int(revenue_potential_ltm) if revenue_potential_ltm is not None else 0
        #
        occupancy_rate_ltm = item.get('occupancy_rate_ltm', 0)
        occupancy_rate_ltm = float(occupancy_rate_ltm) if occupancy_rate_ltm is not None else 0
        #
        average_daily_rate_ltm = item.get('average_daily_rate_ltm', 0)
        average_daily_rate_ltm = int(average_daily_rate_ltm) if average_daily_rate_ltm is not None else 0
        #
        days_available_ltm = item.get('days_available_ltm', 0)
        days_available_ltm = int(days_available_ltm) if days_available_ltm is not None else 0
        #
        location = item.get('location', {})
        #
        location_lat = float(location.get('lat', 0))
        location_lat = float(location_lat) if location_lat is not None else 0
        #
        location_lng = float(location.get('lng', 0))
        location_lng = float(location_lng) if location_lng is not None else 0

        room_data = {
            "id": id,
            "revenue_ltm": revenue_ltm,
            "revenue_potential_ltm": revenue_potential_ltm,
            "occupancy_rate_ltm": occupancy_rate_ltm,
            "average_daily_rate_ltm": average_daily_rate_ltm,
            "days_available_ltm": days_available_ltm,
            "location_lat": location_lat,
            "location_lng": location_lng,
        }

        data_room = await get_airdna(id)
        if data_room is not None:
            print(f"ino: update data")
            await update_airdna(id, room_data)
        else:
            print(f"info: added data")
            await adding_airdna(room_data)
            
    #print(f"info: Update is: {i}, Added is: {j}")

async def process_file(file_path, semaphore):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            yield process_data(item, semaphore)  # Использование генератора

async def transfer_json():
    confirmation = False 
    folder_path = "./json/"
    json_files = glob.glob(os.path.join(folder_path, '*.json'))
    semaphore = asyncio.Semaphore(7)  # Ограничение на 10 одновременных операций

    for file_path in json_files:
        print(f"Processing file: {file_path}")
        tasks = [task async for task in process_file(file_path, semaphore)]
        await asyncio.gather(*tasks)

    confirmation = True
    return confirmation




if __name__ == "__main__":
    asyncio.run(transfer_json())
















# from worker_db import get_airdna, update_airdna, adding_airdna
# import asyncio
# import glob
# import json
# import os

# async def process_data(item):
#     id = item.get('airbnb_property_id', 0)
#     id = int(id) if id is not None else 0

#     revenue_ltm = item.get('revenue_ltm', 0)
#     revenue_ltm = int(revenue_ltm) if revenue_ltm is not None else 0

#     revenue_potential_ltm = item.get('revenue_potential_ltm', 0)
#     revenue_potential_ltm = int(revenue_potential_ltm) if revenue_potential_ltm is not None else 0

#     occupancy_rate_ltm = item.get('occupancy_rate_ltm', 0)
#     occupancy_rate_ltm = float(occupancy_rate_ltm) if occupancy_rate_ltm is not None else 0
    
#     average_daily_rate_ltm = item.get('average_daily_rate_ltm', 0)
#     average_daily_rate_ltm = int(average_daily_rate_ltm) if average_daily_rate_ltm is not None else 0

#     days_available_ltm = item.get('days_available_ltm', 0)
#     days_available_ltm = int(days_available_ltm) if days_available_ltm is not None else 0

#     location = item.get('location', {})

#     location_lat = float(location.get('lat', 0))
#     location_lat = float(location_lat) if location_lat is not None else 0

#     location_lng = float(location.get('lng', 0))
#     location_lng = float(location_lng) if location_lng is not None else 0

#     room_data = {
#         "id": id,
#         "revenue_ltm": revenue_ltm,
#         "revenue_potential_ltm": revenue_potential_ltm,
#         "occupancy_rate_ltm": occupancy_rate_ltm,
#         "average_daily_rate_ltm": average_daily_rate_ltm,
#         "days_available_ltm": days_available_ltm,
#         "location_lat": location_lat,
#         "location_lng": location_lng,
#     }

#     data_room = await get_airdna(id)
#     if data_room is not None:
#         print("update")
#         await update_airdna(id, room_data)
#     else:
#         print("added")
#         await adding_airdna(room_data)

# def transfer_json():
#     folder_path = "./json/"
#     json_files = glob.glob(os.path.join(folder_path, '*.json'))
#     tasks = []
#     for file_path in json_files:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#             for item in data:
#                 tasks.append(process_data(item))
#                 print("Task aded")

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.gather(*tasks))

# transfer_json()













# from worker_db import get_airdna, update_airdna, adding_airdna
# import asyncio
# import json
# import glob
# import os



# def transfer_json():
#     confirmation = False
#     # Путь к папке, в которой нужно искать файлы
#     folder_path = "./json/"
#     # Поиск всех файлов с расширением .json в указанной папке
#     json_files = glob.glob(os.path.join(folder_path, '*.json'))
#     # Вывод списка названий файлов .json
#     for file_path in json_files:
#         name_file = "./json/" + os.path.basename(file_path)
#         # Чтение и загрузка содержимого JSON-файла
#         with open(name_file, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#             up_db = ad_db = 0 # Обнуление счетчиков
#             # Извлечение данных из каждого элемента списка
#             for item in data:
#                 id = item.get('airbnb_property_id')
#                 if id is not None:
#                     id = int(id)
#                 else:
#                     id = 0
#                 revenue_ltm = int(item.get('revenue_ltm'))
#                 revenue_potential_ltm  = int(item.get('revenue_potential_ltm'))
#                 occupancy_rate_ltm = float(item.get('occupancy_rate_ltm'))
#                 average_daily_rate_ltm = int(item.get('average_daily_rate_ltm'))
#                 days_available_ltm = int(item.get('days_available_ltm'))
#                 lat = item['location']['lat'] if 'location' in item and 'lat' in item['location'] else None
#                 lng = item['location']['lng'] if 'location' in item and 'lng' in item['location'] else None
#                 location_lat = float(lat)
#                 location_lng = float(lng)

#                 room_data = {

#                     "id": id,
#                     "revenue_ltm": revenue_ltm,
#                     "revenue_potential_ltm": revenue_potential_ltm,
#                     "occupancy_rate_ltm": occupancy_rate_ltm,
#                     "average_daily_rate_ltm": average_daily_rate_ltm,
#                     "days_available_ltm": days_available_ltm,
#                     "location_lat": location_lat,
#                     "location_lng": location_lng,

#                             }
                
#                 data_room = asyncio.run(get_airdna(id))
#                 if data_room is not None:
#                     print("update")
#                     asyncio.run(update_airdna(id, room_data))
#                     up_db += 1
#                 else:
#                     print("aded")
#                     asyncio.run(adding_airdna(room_data))
#                     ad_db += 1

#             print(f"info: Transferring data from a json file {name_file} to a database.\ninfo: Update: {up_db}. Add: {ad_db}\n")
    
#     confirmation = True    
#     return confirmation

# if __name__ == "__main__":
#     transfer_json()