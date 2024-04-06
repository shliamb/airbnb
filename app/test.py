from worker_db import get_rooms_by_id#, update_rooms, adding_rooms
from datetime import datetime, timezone, timedelta
import asyncio
import time
import random
import sys
from tqdm import tqdm
import re





id = 687145322276122257
data_room = asyncio.run(get_rooms_by_id(id))
if data_room is not None:
    pass
    print()
    print(data_room.title_room)
    print(data_room.name_room)
    print(data_room.subtitle_room)
    print(data_room.night_price)
    print(data_room.total_price)
    print(data_room.currency)
    print(data_room.rating)
    print(data_room.place)
    print(data_room.url_room)
    print(data_room.image_url)
    print(data_room.country)
    print(data_room.rooms_date_update)
    print(data_room.room_date_update)
    print()
else:
    print("None data, sorry..")

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
