from worker_db import get_rooms_by_id, update_rooms
import asyncio
import json
import glob
import os



def transfer_json():
    confirmation = False
    # Путь к папке, в которой нужно искать файлы
    folder_path = "./json/"
    # Поиск всех файлов с расширением .json в указанной папке
    json_files = glob.glob(os.path.join(folder_path, '*.json'))
    # Вывод списка названий файлов .json
    for file_path in json_files:
        name_file = "./json/" + os.path.basename(file_path)
        # Чтение и загрузка содержимого JSON-файла
        with open(name_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            up_db = not_found = 0 # Обнуление счетчиков
            # Извлечение данных из каждого элемента списка
            for item in data:
                id = item.get('airbnb_property_id')
                if id is not None:
                    id = int(id)
                else:
                    id = 0
                revenue_ltm = int(item.get('revenue_ltm'))
                revenue_potential_ltm  = int(item.get('revenue_potential_ltm'))
                occupancy_rate_ltm = float(item.get('occupancy_rate_ltm'))
                average_daily_rate_ltm = int(item.get('average_daily_rate_ltm'))
                days_available_ltm = int(item.get('days_available_ltm'))
                lat = item['location']['lat'] if 'location' in item and 'lat' in item['location'] else None
                lng = item['location']['lng'] if 'location' in item and 'lng' in item['location'] else None
                location_lat = float(lat)
                location_lng = float(lng)

                room_data = {

                    #"id": id,
                    "revenue_ltm": revenue_ltm,
                    "revenue_potential_ltm": revenue_potential_ltm,
                    "occupancy_rate_ltm": occupancy_rate_ltm,
                    "average_daily_rate_ltm": average_daily_rate_ltm,
                    "days_available_ltm": days_available_ltm,
                    "location_lat": location_lat,
                    "location_lng": location_lng,

                            }

                data_room = asyncio.run(get_rooms_by_id(id))
                if data_room != None:
                    asyncio.run(update_rooms(id, room_data))
                    up_db += 1
                else:
                    not_found += 1

            print(f"info: Transferring data from a json file {name_file} to a database.\ninfo: Update: {up_db}. Not found id: {not_found}\n")
    
    confirmation = True    
    return confirmation

if __name__ == "__main__":
    transfer_json()