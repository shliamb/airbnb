from openpyxl import Workbook
from worker_db import get_all_rooms
import asyncio


data = asyncio.run(get_all_rooms())

all_static = []
number = 0

all_static.append(["№", "Объект / Object", "Локация/ Location", "Категория", "Число br / Quantity of br", "Срок размещения / Listing period",\
                    "Средняя цена юнита за сутки, $ / ADR", "Загрузка средняя фактическая / Actual average occupancy",\
                    "Выручка историческая / Historical value", "Цена за месяц, $", "Площадь, м2",\
                    "Вид","P","Ресторан/Restraunt", "Бассейн / Pool", "Кухня / Kitchen",\
                    "Коворкинг/coworking", "Руфтоп/ rooftop", "Балкон, терасса/ Balcony or terrace", "камера хранения/ storage room",\
                    "Рейтинг отзывов", "Источник данных"])

for n in data:
    number += 1 # №
    # object = f"{n.title_room}\n  {n.url_room}" # Объект / Object
    object = n.title_room # Объект / Object
    location = "ссылка на карту" # Локация/ Location
    type_house = n.type_house # Категория
    bedrooms = n.bedroom # Число br / Quantity of br
    list_per = "Срок размещения" # Срок размещения / Listing period
    adr = "Средняя цена юнита за сутки" # Средняя цена юнита за сутки, $ / ADR
    actual_aver = "Загрузка средняя фактическая" # Загрузка средняя фактическая / Actual average occupancy
    historic = "Выручка историческая" # Выручка историческая / Historical value
    price_month = "Цена за месяц" # Цена за месяц, $
    sqm = n.sqm # Площадь, м2
    view = n.view # Вид
    parking = n.parking # P
    restraunt = n.restaurants # Ресторан/Restraunt
    pool = n.bath # Бассейн / Pool
    kitchen = n.kitchen # Кухня / Kitchen
    coworking = n.workspace# Коворкинг/coworking
    rooftop = n.rooftop# Руфтоп/ rooftop
    balcony_terrace = n.terrace_balcony# Балкон, терасса/ Balcony or terrace
    storage = n.storage # камера хранения/ storage room
    rating = n.rating # Рейтинг отзывов
    data_source = "Источник данных" # Источник данных


    all_static.append([number, object, location, type_house, bedrooms, list_per, adr, actual_aver,\
     historic, price_month, sqm, view, parking, restraunt, pool, kitchen, coworking, rooftop, \
        balcony_terrace, storage, rating, data_source]) # added user data


# Создание новой книги Excel
wb = Workbook()
ws = wb.active  # Получение активного листа

# # Заполнение листа данными
for row in all_static:
    ws.append(row)


# Сохранение книги Excel в файл
file_path = './file/data.xlsx'  # Укажите путь и имя файла, если нужно сохранить в определенной папке
wb.save(file_path)

print(f'Таблица успешно сохранена в файл {file_path}')