from worker_db import get_rooms_by_id#, update_rooms, adding_rooms
import asyncio
import time
import random
import sys
from tqdm import tqdm
import re


id = 4354526
data_room = asyncio.run(get_rooms_by_id(id))

print()
print(data_room.title_room)
print(data_room.name_room)
print(data_room.subtitle_room)
print(data_room.night_price)
print(data_room.total_price)
print(data_room.currency)
print(data_room.rating)
print(data_room.url_room)
print(data_room.image_url)
print(data_room.country)
print(data_room.date_of_update)
print()



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
