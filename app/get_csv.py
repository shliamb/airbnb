from worker_db import get_all_rooms
import csv
from io import StringIO, BytesIO
import asyncio
import os



data = asyncio.run(get_all_rooms())


all_static = []
number = 0
all_static.append(["№", "Объект / Object", "Локация/ Location", "Категория", "Число br / Quantity of br", "Срок размещения / Listing period",\
                    "Средняя цена юнита за сутки, $ / ADR", "Загрузка средняя фактическая / Actual average occupancy",\
                    "Выручка историческая / Historical value", "Цена за месяц, $", "Площадь, м2",\
                    "Вид","P","Ресторан/Restraunt", "Бассейн / Pool", "Кухня / Kitchen",\
                    "Коворкинг/coworking", "Руфтоп/ rooftop", "Балкон, терасса/ Balcony or terrace", "камера хранения/ storage room",\
                    "Рейтинг отзывов", "Источник данных"])


            # "id": id,
                        # "revenue_ltm": revenue_ltm,
            # "revenue_potential_ltm": revenue_potential_ltm,
                        # "occupancy_rate_ltm": occupancy_rate_ltm,
                        # "average_daily_rate_ltm": average_daily_rate_ltm,
            # "days_available_ltm": days_available_ltm,


            # "location_lat": location_lat,
            # "location_lng": location_lng,

for n in data:
    number += 1 # №
    # object = f"{n.title_room}\n  {n.url_room}" # Объект / Object
    object = n.title_room # Объект / Object
    location = "ссылка на карту" # Локация/ Location
    type_house = n.type_house # Категория
    bedrooms = n.bedroom # Число br / Quantity of br
    #list_per = a.days_available_ltm #"Срок размещения" # Срок размещения / Listing period - days ev
    #adr = a.average_daily_rate_ltm # Средняя цена юнита за сутки, $ / ADR
    #actual_aver = a.occupancy_rate_ltm # Загрузка средняя фактическая / Actual average occupancy
    #historic = a.revenue_ltm # "Выручка историческая" # Выручка историческая / Historical value - revenue_ltm
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
    #print(n.id)


    # all_static.append([number, object, location, type_house, bedrooms, list_per, adr, actual_aver,\
    #  historic, price_month, sqm, view, parking, restraunt, pool, kitchen, coworking, rooftop, \
    #     balcony_terrace, storage, rating, data_source]) # added user data


# Create csv file
# Использование StringIO для записи данных в формате CSV.
output = StringIO()
writer = csv.writer(output)

# Запись строк данных в объект StringIO.
for row in all_static:
    writer.writerow(row)

# Получение всех данных из StringIO.
csv_data = output.getvalue()
output.close()

# Имя файла для сохранения.
file_name = "./file/data.csv"

# Сохранение данных в файл в рабочей папке.
try:
    # Открытие файла на запись в текстовом режиме.
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(csv_data)
    print(f"Файл {file_name} успешно сохранен.")
except Exception as e:
    print(f"Произошла ошибка при сохранении файла: {e}")