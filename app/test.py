from worker_db import get_all_airdna_id_join, get_airbnb, get_id, get_map
from datetime import datetime, timezone, timedelta
#from app.bad.parser_sys import str_inter
import asyncio
import time
import random
import sys
# from tqdm import tqdm
import re
# from colorama import Fore, Back, Style
# from options_chrome import profil

# profil.counter = 0


# profil()
# profil()
# profil()
# profil()


#url_href = "/rooms/897544692951213383?adults"
# url_href = "/luxury/listing/20473374?adults=1&ch"


# pattern = r"/(?:rooms|listing)/(\d+)"


# match = re.search(pattern, url_href)
# if match:
#     id = int(match.group(1))
# else:
#     id = None

# print("id:", id)



# room_data = {"id": 4445, "url": 34, "date": 343}

# for n in room_data:
#     print(n["url"])






# room_data = {"id": 4445, "url": 34, "date": 343}

# print(room_data['url'])


# url = "https://www.airbnb.ru/rooms/945811232623268326?adults=1&category_tag=Tag%3A5635&children=0&enable_m3_private_room=true&infants=0&pets=0&photo_id=1824705786&search_mode=flex_destinations_search&check_in=2024-07-29&check_out=2024-08-03&source_impression_id=p3_1713289897_FGt11VEmkmQNPnhq&previous_page_section_name=1000&federated_search_id=65e9afac-3b5d-4fe0-bfd0-3bf6e390bdfa"
# #url = "https://www.airbnb.ru/luxury/listing/26197937?adults=1&children=0&enable_m3_private_room=true&infants=0&pets=0&check_in=2024-04-17&check_out=2024-04-22&source_impression_id=p3_1713150034_4ZBpuHJRM8yIkxrI&previous_page_section_name=1000&federated_search_id=e7538e51-0aa1-4233-90db-44026bf8abe3&_set_bev_on_new_domain=1712664722_NmUyY2E3NmYyNmI1"

# pattern = r'(/listing/\d+|rooms/\d+)'
# url_object = re.sub(pattern, r'\1/amenities', url)


# print(url_object)


# pattern = r'(/?listing|rooms/\d+)'
# url_object = re.sub(pattern, r'/amenities', url)



















# id = 738026793777154035

# data = asyncio.run(get_id(id))
# if data is not None:
#     print(f"{data.passed_flag}\n{data.id}\n{data.url}\n{data.date}\n{data.busy_flag}")


# data_room = asyncio.run(get_airbnb(id))
# if data_room is not None:





# data = asyncio.run(get_all_airdna_id_join())

# i = 0

# for n, k, p in data:
#     print(n.location_lat)
#     i += 1
# print(f"Всего: {i}")



# a = ['Country: Индонезия', 'Province: провинция Бали', 'Area: Кабупатен-Табанан']

# d = ' | '.join(a)

# print(d)






# id = 967685889953187975

# data = asyncio.run(get_map(id))

# print(data.id)
# print(data.url)
# print(data.title)
# print(data.location_lat)
# print(data.location_lng)
# print(data.date)

# i = 0

# for n in data:
#     print(n.location_lat)
#     i += 1
# print(f"Всего: {i}")































# id = 738026793777154035

# data = asyncio.run(get_id(id))
# if data is not None:
#     print(f"{data.passed_flag}\n{data.id}\n{data.url}\n{data.date}\n{data.busy_flag}")


# data_room = asyncio.run(get_airbnb(id))
# if data_room is not None:
#     pass
#     print()
#     print(data_room.id)
#     print(data_room.url)
#     print(data_room.title)
#     print(data_room.name)
#     print(data_room.type_house)
#     print(data_room.night_price)
#     print(data_room.month_price)
#     print(data_room.currency)
#     print(data_room.rating)
#     print(data_room.reviews)
#     print(data_room.guest_favorite)
#     print(data_room.guest)
#     print(data_room.bedroom)
#     print(data_room.bed)
#     print(data_room.bath)
#     print(data_room.parking)
#     print(data_room.kitchen)
#     print(data_room.view)
#     print(data_room.workspace)
#     print(data_room.rooftop)
#     print(data_room.terrace_balcony)
#     print(data_room.restaurants)
#     print(data_room.storage)
#     print(data_room.sqm)
#     print(data_room.date_update)
#     print(data_room.date)
#     print(data_room.location)
#     print()
# else:
#     print("None data, sorry..")



















# i = 0

# data_room = asyncio.run(get_all_airdna())

# if data_room is not None:
#     for n in data_room:
#         print("id: ", n.id)
#         print("n.revenue_ltm: ", n.revenue_ltm)
#         print("n.revenue_potential_ltm: ", n.revenue_potential_ltm)
#         print("n.occupancy_rate_ltm: ", n.occupancy_rate_ltm)
#         print("n.average_daily_rate_ltm: ", n.average_daily_rate_ltm)
#         print("n.days_available_ltm: ", n.days_available_ltm)
#         print("n.location_lat: ", n.location_lat)
#         print("n.location_lng: ", n.location_lng)
#         print("n.date: ", n.date)
#         print()
#         i += 1
# print("i: ", i)


# id = 1035169267511734598

# n = asyncio.run(get_airdna(id))
# if n is not None:
#     pass
#     print(n.id)
#     print(n.revenue_ltm)
#     print(n.revenue_potential_ltm)
#     print(n.occupancy_rate_ltm)
#     print(n.average_daily_rate_ltm)
#     print(n.days_available_ltm)
#     print(n.location_lat)
#     print(n.location_lng)
#     print(n.date)
#     print()
# else:
#     print("нет такой чтука")





# async def main():
#     i = 0
#     rooms_data = await get_all_rooms_not_None2()
#     for room in rooms_data:
#         airbnb_room, airdna_room = room
#         print(airbnb_room.id)  # Объект из таблицы Airbnb
#         if airdna_room is not None:
#             print(airdna_room.location_lat)  # Связанный объект из таблицы Airdna (если есть)
#             print()
#         i += 1
#     print("Всего: ", i)

# asyncio.run(main())




# from datetime import datetime, timezone, timedelta



# GET DAY AND TIME
# def get_time_utcnow() -> time:
#     current_time = datetime.now(timezone.utc).strftime("%M")
#     return current_time


# current_time = get_time_utcnow()
# print(current_time)







# from datetime import datetime, timezone

# def time_utcnow() -> str:
#     return datetime.now(timezone.utc).strftime("%H:%M:%S")

# # Использование функции
# current_time_str = time_utcnow()
# print(current_time_str)  # Выводит текущее время в UTC в формате HH:MM:SS






















# import glob
# import os

# # Путь к папке, в которой нужно искать файлы
# folder_path = "./json/"

# # Поиск всех файлов с расширением .json в указанной папке
# json_files = glob.glob(os.path.join(folder_path, '*.json'))

# # Вывод списка названий файлов .json
# for file_path in json_files:
#     print(os.path.basename(file_path))



# for n, a in data:
#     object =  f'"{n.title_room}", "{n.url_room}"' 
#     type_house = n.type_house
#     bedrooms = n.bedroom


#     all_static.append([object, type_house, bedrooms])


# for row in all_static:
#     for s in row:

#         print(s[0])
#         print(s[1])



# alb =[ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V" ]



# for s in alb:
#     #if alb[k] == "B":
#     print(s)











# print(Fore.RED + 'some red text')

# print("fdfd")
# print(Back.RED + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)

# print(Back.BLUE + 'and with a green background')
# print(Style.RESET_ALL)
# print('back to normal now')


# [
#   {
#     "property_id": "abnb_13962793",
#     "airbnb_property_id": "13962793",
#     "vrbo_property_id": null,
#     "listing_type": "entire_place",
#     "bedrooms": 2,
#     "bathrooms": 1,
#     "accommodates": 3,
#     "rating": 4.9,
#     "reviews": 374,
#     "title": "Pondok Prapen -Ubud Center Private Pool Villa",
#     "revenue_ltm": 1057925600,
#     "revenue_potential_ltm": 1071900000,
#     "occupancy_rate_ltm": 97.5,
#     "average_daily_rate_ltm": 3014024,
#     "days_available_ltm": 360,
#     "images": [
#       "htlarge",
#       "hteg"
#     ],
#     "market_id": 32,
#     "market_name": "Bali",
#     "location": {
#       "lat": -8.50222,
#       "lng": 115.26749
#     },
#     "currency": "idr"
#   },
# ...






# a = "gfserdsdsgazg"
# b = "ddghjdse"

# def ger(a, b):
#     c = sorted(set(a + b))

#     print(c)



# # b = sorted(a)
# print(ger(a, b))

# a = "gfserdsdsgazg"

# b = set("gfserdsdsgazg")

# i = ""

# for n in b:
#     #print(type(n))
#     i = i + n

# print(type(i))








# for n in range(2,-10):
#     print(n)


# id = 826564732035479725
# data_room = asyncio.run(get_rooms_by_id(id))
# if data_room is not None:
#     pass
#     print()
#     print(data_room.title_room)
#     print(data_room.name_room)
#     print(data_room.type_house)
#     print(data_room.night_price)
#     print(data_room.month_price)
#     print(data_room.currency)
#     print(data_room.rating)
#     print(data_room.reviews)
#     print(data_room.guest_favorite)
#     print(data_room.guest)
#     print(data_room.bedroom)
#     print(data_room.bed)
#     print(data_room.bath)
#     print(data_room.parking)
#     print(data_room.kitchen)
#     print(data_room.view)
#     print(data_room.workspace)
#     print(data_room.rooftop)
#     print(data_room.terrace_balcony)
#     print(data_room.restaurants)
#     print(data_room.storage)
#     print(data_room.sqm)
#     print(data_room.url_room)
#     print(data_room.location)
#     print(data_room.obj_date_update)
#     print(data_room.currency)
#     print(data_room.revenue_ltm)
#     print(data_room.revenue_potential_ltm)
#     print(data_room.occupancy_rate_ltm)
#     print(data_room.average_daily_rate_ltm)
#     print(data_room.days_available_ltm)
#     print(data_room.location_lat)
#     print(data_room.location_lng)
#     print(data_room.currency)
#     print(data_room.is_done)
#     print(data_room.is_parse)


#     print()
# else:
#     print("None data, sorry..")












# как в строку 
# a = "https://www.airbnb.com/rooms/708579259703259226?adults=1&category_t"
# вставить amenities сразу после rooms/ при помощи re

# https://www.airbnb.com/rooms/708579259703259226/amenities?adults=1&category_t








# s = "dfd VIfLA fdf dfff"

# if "vila" in s.lower():
#     print("Yes")
# else:
#     print("Not")






# a = "2 guests ·  · 1 bedroom ·  · 1 bed ·  · 1 bath"

# # Заменяем " ·  · " на "|"
# a = a.replace(" ·  · ", " | ")

# # Разделяем строку по "|"
# list_of_elements = a.split(" | ")

# aa = list_of_elements

# print(aa[0])





# num = int('-2')


# print(num)
# print(type(num))


# def dddf():
#     data_room = asyncio.run(get_rooms_by_location("Bali"))

#     for data in data_room:
#         print(data.id)

# if __name__ == "__main__":
#     dddf()






# # text = "The room is 15sqm in size."
# text = "The room is 15sqm in size."
# # Этот шаблон ищет одно или более чисел, за которыми следует необязательный пробел и 'sqm'
# pattern = r'(\d+)\s*sqm'

# match = re.search(pattern, text)
# if match:
#     number = match.group(1)
#     unit = 'sqm'
#     print(f"Number: {number}, Unit: {unit}")
# else:
#     print("No match found.")



# import sys

# number = 989583347152579661
# print(sys.getsizeof(number))

# выходит примерно около 32кб каждая 1000 id в памяти - приемлемо




# def rating_clean2(num: str) -> float | int:
#     match1 = re.search(r"\b\d+(?:\.\d+)?\b", num)
#     if match1:
#         rating = float(match1.group(0))
#     else:
#         rating = 0.0

#     match2 = re.search(r"\b(\d+)\s+reviews\b", num)
#     if match2:
#         reviews = int(match2.group(1))
#     else:
#         reviews = 0

#     return rating, reviews


# a = rating_clean2("4.95 · 37 reviews")
# print(a[0])
# print(a[1])


# id
# title_room
# name_room
# type_house
# night_price
# month_price
# currency
# rating
# reviews
# guest_favorite
# guest
# bedroom
# bed
# bath
# parking
# kitchen
# view
# workspace
# rooftop
# terrace_balcony
# restaurants
# storage
# sqm

# CLEAN RATING
# def rating_cleen(num: str) -> float | int:
#     match1 = re.search(r"\b\d+\.\d+\b", num)
#     if match1:
#         rating = float(match1.group(0))
#     else:
#         rating = None

#     match2 = re.search(r",\s*(\d+)s+reviews", num)
#     if match2:
#         place = int(match2.group(1))
#     else:
#         place = None
#     return rating, place


# print(rating_cleen("4.95 · 37 reviews"))



    # # Извлечение количества отзывов
    # match2 = re.search(r',s*(d+)s+reviews', text)
    # if match2:
    #     place = int(match2.group(1))
    # else:
    #     place = None







# sqm площадь не нашел, в одном месте видел в виде текста (15 sqm, 15sqm) м²
# print("sqm:", "None")










# location = "Bali-Province--Indonesia"


# data_room = asyncio.run(get_rooms_by_location(location))

# for data in data_room:
#     id = data.id
#     url = data.url_room
#     print(id)

#data_room = [...] # Здесь должен быть ваш список объектов

# # Откроем файл test.txt для записи
# with open('test.txt', 'w') as file:
#     for data in data_room:
#         id = data.id  # Получаем ID
#         url = data.url_room  # URL не используется в данном примере, но вы могли бы также записать его в файл
#         print(id)  # Выводим ID на экран (это можно убрать, если не нужно)
        
#         # Записываем ID в файл, добавляя символ новой строки после каждого ID
#         file.write(str(id) + '\n')



# id = 986635336249978757
# data_room = asyncio.run(get_rooms_by_id(id))
# if data_room is not None:
#     pass
#     print()
#     print(data_room.title_room)
#     print(data_room.name_room)
#     print(data_room.type_house)
#     print(data_room.night_price)
#     print(data_room.month_price)
#     print(data_room.currency)
#     print(data_room.rating)
#     print(data_room.reviews)
#     print(data_room.guest_favorite)
#     print(data_room.guest)
#     print(data_room.bedroom)
#     print(data_room.bed)
#     print(data_room.bath)
#     print(data_room.parking)
#     print(data_room.kitchen)
#     print(data_room.view)
#     print(data_room.workspace)
#     print(data_room.rooftop)
#     print(data_room.terrace_balcony)
#     print(data_room.restaurants)
#     print(data_room.storage)
#     print(data_room.sqm)

#     print(data_room.url_room)
#     print(data_room.location)
#     print(data_room.obj_date_update)
#     print(data_room.currency)
#     print()
# else:
#     print("None data, sorry..")

        # # "id": id,
        # "title_room": title_room,
        # "name_room": name_room,
        # "type_house": type_house,
        # "night_price": night_price,
        # "month_price": month_price,
        # "currency": currency,
        # "rating": rating,
        # "reviews": reviews,
        # "guest_favorite": guest_favorite,
        # "guest": guest,
        # "bedroom": bedroom,
        # "bed": bed,
        # "bath": bath,
        # "parking": parking,
        # "kitchen": kitchen,
        # "view": view,
        # "workspace": workspace,
        # "rooftop": rooftop,
        # "terrace_balcony": terrace_balcony,
        # "restaurants": restaurants,
        # "storage": storage,
        # "sqm": sqm,
        # # "url_room": url_room,
        # # "location": location,
        # "obj_date_update": obj_date_update,
        # "currency" : currency 











# title_room: Bed and breakfast in Kecamatan Ubud
# name_room: Budget traveller's private roon in Central Ubud
# subtitle_room: 1 bed
# night_price: 20.0
# total_price: 121.0
# rating: 4.13
# place: 15
# url_room: https://www.airbnb.com/rooms/687145322276122257?guests=1&search_mode=regular_search&check_in=2024-05-01&check_out=2024-05-07&source_impression_id=p3_1712417859_c4TYxJZNcHnyOvYu&previous_page_section_name=1000&federated_search_id=61e7798c-2be8-4705-b497-b52c41db70b1
# id: 687145322276122257
# image_url: https://a0.muscache.com/im/pictures/miso/Hosting-687145322276122257/original/d2b138d4-e1a4-4efc-9eb6-9cc1ccf8de82.jpeg?im_w=720

# The record 687145322276122257 is fresh, there is no need to update it





# # Получение текущего времени
# a = datetime.now()
# # Установка значения для ff
# ff = -2
# # Добавление ff часов к текущему времени
# a = a + timedelta(hours=ff)
# print(a)  # Выведет время, увеличенное на ff часа


# GET DAY AND TIME
# def day_utcnow(time_correction: str) -> datetime:
#     utc_zone = timezone.utc
#     a = datetime.now(timezone.utc).replace(tzinfo=utc_zone)
#     a = a + timedelta(hours=time_correction)
#     day_str = a.strftime("%Y-%m-%d %H:%M:%S")
#     day = datetime.strptime(day_str, '%Y-%m-%d %H:%M:%S')
#     return day or None

# time_correction = +3
# b = day_utcnow(time_correction)
# print(type(b))

# UNFORMAT TIME
# def unfomat_date(date_of_update) -> str | int:
#     day_now = str(date_of_update.strftime("%Y-%m-%d"))
#     time_now = float(date_of_update.strftime("%H.%M"))
#     return day_now, time_now


# time_correction = +3
# b = day_utcnow(time_correction)
# a = unfomat_date(b)

# print(a[0]) 
# print(a[1])




# # CLEAN RATING
# def rating_cleen(num: str) -> float | int:
#     match1 = re.search(r"\b\d+\.\d+\b", num)
#     if match1:
#         rating = float(match1.group(0))
#     else:
#         rating = None

#     match2 = re.search(r',\s*(\d+)\s+', num)
#     if match2:
#         place = int(match2.group(1))
#     else:
#         place = None
#     return rating, place


# a = "4.71 out of 5 average rating,  457 reviews4.71 (457)"
# #a = "5.0 out of 5 average rating,  15 reviews5.0 (15)"
# #a = "4.95 out of 5 average rating,  19 reviews4.95 (19)"

# b = rating_cleen(a)
# print(b[0])
# print(b[1])


# def rating_cleen(num: str) -> float:
#     pattern = r"(\d{1,3}(?:,\d{3})*)"
#     num = re.sub(r"[^\d.,]", "", num)
#     str_num = re.search(pattern, num)
#     float_num_str = str_num.group(1).replace(',', '')
#     float_num = float(float_num_str)
#     print(float_num)



#a = "5.0 out of 5 average rating,  15 reviews5.0 (15)"
#a = "4.95 out of 5 average rating,  19 reviews4.95 (19)"
#a = "4.71 out of 5 average rating,  457 reviews4.71 (457)"

# rating_cleen(a)




# def rating_cleen(num: str) -> float:
#     pattern = r"(\d{1,3}(?:,\d{3})*(?:\.\d+)?)"
#     num = re.sub(r"[^\d.,]", "", num)
#     str_num = re.search(pattern, num)
#     float_num_str = str_num.group(1).replace(',', '')
#     float_num = float(float_num_str)
#     print(float_num)





# def str_int(num: str) -> float:
#     #pattern = "(\d+)"
#     pattern = r"(\d{1,3}(?:,\d{3})*(?:\.\d+)?)"
#     str_num = re.search(pattern, num)
#     float_num = float(str_num.group(1))
#     return float_num or None


# print(str_int("$1,345"))



# def str_int(num: str) -> float:
#     pattern = r"(\d{1,3}(?:,\d{3})*(?:\.\d+)?)"
#     num = re.sub(r"[^\d.,]", "", num)
#     str_num = re.search(pattern, num)
#     if not str_num:
#         return None
#     float_num_str = str_num.group(1).replace(',', '')
#     try:
#         float_num = float(float_num_str)
#         return float_num
#     except ValueError:
#         return None

# print(str_int("$10,548,00"))




# title_room: Villa in Lalang Lingga
# name_room: Beachside Villa at Balian Surf Break
# subtitle_room: On the beach
# night_price: $156
# total_price: $935 total
# rating: 4.86 out of 5 average rating,  261 reviews4.86 (261)
# url_room: https://www.airbnb.com/rooms/7095467?guests=1&search_mode=regular_search&check_in=2024-05-01&check_out=2024-05-07&source_impression_id=p3_1712342793_8FxZO8RGEyLHa2X%2F&previous_page_section_name=1000&federated_search_id=7b7829c1-0636-4fcb-842b-29e073c21324
# id: 7095467
# image_url: https://a0.muscache.com/im/pictures/bc9cb356-c44d-471d-9768-8b67f47f86ad.jpg?im_w=720




































# def quick_sleep(mi: int, ma: int) -> bool:
#     confirm = False
#     num = random.randint(mi, ma)
#     print(f"wait {num} seconds")
#     def spinning_cursor():
#         while True:
#             for cursor in '|/-\|':
#                 yield cursor
#     spinner = spinning_cursor()
#     i = 0
#     while i < num:
#         sys.stdout.write(next(spinner))
#         sys.stdout.flush()
#         time.sleep(0.04)
#         sys.stdout.write('\r')
#         i += 0.042
#     sys.stdout.flush()
#     #print()
#     confirm = True
#     return confirm

# quick_sleep(5, 5)

    # for _ in range(50):
    #     sys.stdout.write(next(spinner))
    #     sys.stdout.flush()
    #     time.sleep(0.05)
    #     sys.stdout.write('\r')  


# def spinning_cursor():
#     while True:
#         for cursor in '|/-\|':
#             yield cursor

# spinner = spinning_cursor()  # Создание генератора
# for _ in range(50):  # Количество повторений
#     sys.stdout.write(next(spinner))  # Вывод следующего символа из генератора
#     sys.stdout.flush()               # Очистка буфера вывода
#     time.sleep(0.05)                  # Пауза
#     sys.stdout.write('\r')           # Возврат курсора на один символ назад


# for i in range(0, 101, 1):
#   print("\r>> You have finished {}%".format(i), end='')
#   #sys.stdout.flush()
#   time.sleep(0.01)
# print()







# def quick_sleep(mi: int, ma: int) -> bool:
#     num = random.uniform(0.001, 0.01)

#     print("")
#     items = range(0, 100)
#     for _ in tqdm(items, desc="Wait"):
#         time.sleep(num)





# quick_sleep(2, 3)





# def quick_sleep(mi: int, ma: int) -> bool:
#     # Пример использования
#     items = list(range(mi, ma))
#     l = len(items)

#     # Инициализация шкалы заполнения
#     print_progress_bar(0, l, prefix='Прогресс:', suffix='Завершено', length=50)

#     num = random.uniform(mi, ma)
#     i = num / 5
#     j = 1
#     while j < 6:
#         #print(f"{j} ", end='', flush=True)

#         # Обновление шкалы заполнения
#         print_progress_bar(i + 1, l, prefix='Прогресс:', suffix='Завершено', length=50)

#         time.sleep(i)
#         j += 1
#     print("\n")




# def quick_sleep(mi: int, ma: int) -> bool:
#     confirm = False
#     for _ in range(0, random.randint(mi, ma)):
#         print(".", end='', flush=True)
#         time.sleep(random.uniform(0.001, 1.00))
#     print("\n")
#     confirm = True
#     return confirm


# quick_sleep(5, 10)


















# url = "/rooms/661325654411077501?guests=2&search_mode=regular_search&check_in=2024-05-01&check_out=2024-05-07&source_impression_id=p3_1712264377_mf6Ndm%2B9LbqodAZl&previous_page_section_name=1000&federated_search_id=b2d561d5-e492-4fd4-975c-360adaa25228"



# # Регулярное выражение для поиска последовательности цифр после '/rooms/'
# #patern = "/rooms/(\d+)"
# match = re.search("/rooms/(\d+)", url)
# if match:
#     room_number = match.group(1)
#     print(room_number)


# def quick_sleep(mi: int, ma: int) -> bool:
#     confirm = False
#     num = random.randint(mi, ma)
#     i = 0
#     while i < num:
#         print(".")
#         time.sleep(1)
#         i += 1
#     confirm = True
#     return confirm

# result = quick_sleep(2, 4)
# print(result)



# import random
# import time
# import sys

# def quick_sleep(mi, ma):
#     num = random.randint(mi, ma)
#     for _ in range(num):
#         print(".", end='', flush=True)
#         time.sleep(1)
#     print("")

# quick_sleep(4, 5)










# import time
# import random

# prof = "ss"
# uarandom = "dfd"

# texter = ("--disable-webgl", "--disable-gpu", "--disable-3d-apis", "--enable-virtual-keyboard", 
#                     "--mute-audio", "--disable-plugins-discovery", "--profile-directory=Default", "disable-infobars", 
#                     "start-maximized", "--disable-blink-features=AutomationControlled", f"--user-agent={uarandom}", 
#                     f"user-data-dir=./profiles/{prof}/")

# # print(texter)



# print(', '.join(f'"{t}"' for t in texter))
