from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
from worker_db import get_all_rooms_not_None
import asyncio
import shutil

def get_exel_file():
    # Путь к исходному файлу и новое имя файла
    sourcefile = "./file/The Heigts анализ_research.xlsx"
    newfile = "./file/data.xlsx"
    # Копирование файла
    shutil.copy(sourcefile, newfile)
    # Загрузка скопированного файла
    workbook = load_workbook(filename=newfile)
    # Выбор активного листа или листа по имени
    sheet = workbook["расчет ADR и OccupancyADR and O"] 

    data = asyncio.run(get_all_rooms_not_None()) # Получаем даные из базы

    all_static = []
    number = 0

    # Собираем ячейки
    for n in data:
        number += 1
        object =  [f"{n.title_room}", f"{n.url_room}"] # f"{n.title_room} + " # Объект / Object
        location = f"https://www.google.com/maps?q={n.location_lat},{n.location_lng}" #"ссылка на карту" # Локация/ Location
        type_house = n.type_house # Категория
        bedrooms = n.bedroom # Число br / Quantity of br
        list_per = n.days_available_ltm #"Срок размещения" # Срок размещения / Listing period
        adr = n.average_daily_rate_ltm #"Средняя цена юнита за сутки" # Средняя цена юнита за сутки, $ / ADR
        actual_aver = n.occupancy_rate_ltm #"Загрузка средняя фактическая" # Загрузка средняя фактическая / Actual average occupancy
        historic = n.revenue_ltm #"Выручка историческая" # Выручка историческая / Historical value
        price_month = n.month_price # Цена за месяц, $
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
        rating = f"{n.rating} stars, {n.reviews} reviews" # Рейтинг отзывов
        data_source = "Источник данных" # Источник данных

        all_static.append([number, object, location, type_house, bedrooms, list_per, adr, actual_aver,\
        historic, price_month, sqm, view, parking, restraunt, pool, kitchen, coworking, rooftop, \
            balcony_terrace, storage, rating, data_source]) 
    
    # Магия не иначе, переписать
    f = 10
    alb =[ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V" ]
    for row in all_static:
        f += 1
        k = 0
        for s in row:
            if alb[k] == "B":
                cell_to_update = sheet[f"{alb[k]}{f}"]
                cell_to_update.value = s[0]
                cell_to_update.hyperlink = f"{s[1]}"
                cell_to_update.font = Font(color="0000FF", underline="single")
            elif alb[k] == "C":
                cell_to_update = sheet[f"{alb[k]}{f}"]
                cell_to_update.value = "map"
                cell_to_update.hyperlink = s
                cell_to_update.font = Font(color="0000FF", underline="single")
            else:
                cell_to_update = sheet[f"{alb[k]}{f}"]   # 'B11'
                cell_to_update.value = s
            k += 1

    workbook.save(filename=newfile)
    print("info: Exel file is complite")
    return newfile



if __name__ == "__main__":
    get_exel_file()












    # EXEL
    #
    # A B C D E F G H I J K L M N O P Q R S T U V
    # 11
    # 12
    # 13

    # cell_to_update = sheet['B11']
    # cell_to_update.value = "Новые данныеdfd f"


    # all_static.append(["number", "Объект / Object", "Локация/ Location", "Категория", "Число br / Quantity of br", "Срок размещения / Listing period",\
    #                     "Средняя цена юнита за сутки, $ / ADR", "Загрузка средняя фактическая / Actual average occupancy",\
    #                     "Выручка историческая / Historical value", "Цена за месяц, $", "Площадь, м2",\
    #                     "Вид","P","Ресторан/Restraunt", "Бассейн / Pool", "Кухня / Kitchen",\
    #                     "Коворкинг/coworking", "Руфтоп/ rooftop", "Балкон, терасса/ Balcony or terrace", "камера хранения/ storage room",\
    #                     "Рейтинг отзывов", "Источник данных"])