from worker_db import get_airdna, update_airdna, adding_airdna, get_all_airdna, get_rooms_by_id
import asyncio
import json





# data = asyncio.run(get_all_airdna())
# for n in data:
#     print(n.id)






# Путь JSON-файлу
file_path = "./json/san.json"

# Список для сохранения извлеченных данных
extracted_data = []

# Чтение и загрузка содержимого JSON-файла
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

    # Извлечение данных из каждого элемента списка
    for item in data:
        id = int(item.get('airbnb_property_id'))
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

            "id": id,
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
            data_air = asyncio.run(get_airdna(id))
            if data_air != None:
                asyncio.run(update_airdna(id, room_data))
                print("update")
            else:
                asyncio.run(adding_airdna(room_data))
                print("add")
        else:
            print("нет такова в роомс... id")







        # data_id = asyncio.run(get_airdna(id))
        # for n in data_id:
        #     print(n)


# data_id.id

        # if data_id is not None:
        #     print("Yes", data_id.id)
        # else:
        #     print("dfgd")
        # #print(data_id.id)


        # asyncio.run(update_rooms(id, room_data))
        # print(f"info: Updated Data  at object {id}")



# data = asyncio.run(get_all_airdna())
# for n in data:
#     print(n.revenue_ltm)