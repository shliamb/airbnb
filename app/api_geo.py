from keys import yandex_geo
from worker_db import get_all_airdna_id_join, adding_map
from functions_sys import day_utcnow
import asyncio
import requests

# Get location title at points in API Yandex 
async def api_geo(location_lat, location_lng) -> list:
    data_out = []
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={yandex_geo}&geocode={location_lng},{location_lat}&results=1&format=json"
    response = requests.get(url)
        # Преобразование ответа от сервера в JSON-формат
    data = response.json()
        # Получение списка компонентов адреса
    address_components = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
        # Создание словаря для хранения информации о стране, провинции и районе
    address_info = {
        'country': None,
        'province': None,
        'area': []
    }
        # Перебор компонентов адреса и заполнение словаря address_info
    for component in address_components:
        if component['kind'] == 'country':
            address_info['country'] = component['name']
        elif component['kind'] == 'province':
            address_info['province'] = component['name']
        elif component['kind'] == 'area':
            address_info['area'].append(component['name']) 

        # Вывод полученной информации
    data_out.append(f"Country: {address_info['country']}")
    data_out.append(f"Province: {address_info['province']}" )
        # Если есть несколько районов (областей), выводим каждый из них
    for area in address_info['area']:
            #print(f"Area: {area}")
        data_out.append(f"Area: {area}")
        #print(data_out)
    return data_out





# Write table Map 
async def build_table_map():
    i = 0
    j = 0
    confirmation = False
    data = await get_all_airdna_id_join()
    for n, k, m in data:
        url = ""
        location_lat = location_lng = id = 0
        if k:
            url = k.url
        if n:
            id = n.id # or k.id
            location_lng = n.location_lng
            location_lat = n.location_lat
        time_correction = +8
        date = await day_utcnow(time_correction)
        list_title = await api_geo(location_lat, location_lng)
        title = ' | '.join(list_title)

        if title == None or title == []:
            print("Error: It's Yandex limit, sorry.")
            break

        send_data = {
            "id": id,
            "title": title,
            "url": url,
            "location_lng": location_lng,
            "location_lat": location_lat,
            "date": date,
        }

        confirm = False
        confirm = await adding_map(send_data)
        if confirm is True:
            print(f"info: Data {id} in table Map is added.")
            confirmation = True
        elif confirm is False:
            print(f"Error: Data {id} in table Map is not added.")
            j += 1
        i += 1
    print(f"info: Added srings {i} and not added {j}")
    return confirmation

    

if __name__ == "__main__":
    asyncio.run(build_table_map())




































# location_lng = -8.68068
# location_lat = 115.24559

# url_title = api_geo(location_lat, location_lng)
# print(url_title)


#
# https://geocode-maps.yandex.ru/1.x/?apikey=YOUR_API_KEY&geocode=бульвар+Мухаммед+Бин+Рашид+1&format=json
#
# Поиск на оборот, на вход адрес, на выход координаты
#
# https://geocode-maps.yandex.ru/1.x/?apikey=YOUR_API_KEY&geocode=Бурж-Халифа&format=json
#
# Запрос с орфографической ошибкой «Бурж-Халифа», исправление опечатки в ответе
#
# 1000 в сутки что ли.. 25 000 в месяц вроед
#