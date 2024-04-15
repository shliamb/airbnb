from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
from worker_db import get_all_rooms_not_None2
import asyncio
import shutil


def get_exel_file(choice):
        # Путь к исходному файлу и новое имя файла
    sourcefile = "./file/The Heigts анализ_research.xlsx"
    newfile = "./file/stat_data.xlsx"
        # Копирование файла
    shutil.copy(sourcefile, newfile)
        # Загрузка скопированного файла
    workbook = load_workbook(filename=newfile)
        # Выбор активного листа или листа по имени
    sheet = workbook["расчет ADR и OccupancyADR and O"] 

    if choice == "1":
        data = asyncio.run(get_all_rooms_not_None2()) 
    # elif choice == "2":
    #     data = asyncio.run(get_rooms_sorted_by_bedroom_asc())
    # elif choice == "3":
    #     data = asyncio.run(get_rooms_sorted_by_bedroom_desc()) 

        # Переменные
    all_static = []
    number = 0

        # Передаем в переменные данные из ответа базы в цыкле каждая строка
    for n, m in data:
            # Фильтруем записи без бедрум и если в локации пусто
        if n.bedroom != None and n.location != "":
                # Порядковый номер строк в ексель
            number += 1
                # Название объекта и ссылка на него
            object =  [n.title, n.url]
                # Если данные с Airdna есть, то формируем ссылку на локацию в google
            if m:
                url_location = m.location_lat,m.location_lng
            else:
                url_location = ""
            location = [n.location, url_location]             
                # Категория объекта
            type_house = n.type_house
                # Если бедром - 0, то ставим 1, ну явно просто забывают поставить
            bedrooms = 1 if int(n.bedroom) == 0 else n.bedroom
                # Если данные с Airdna существуют, то передаем их переменным
            if m is not None:
                list_per = m.days_available_ltm # Срок размещения / Listing period
                adr = m.average_daily_rate_ltm # Средняя цена юнита за сутки, $ / ADR
                actual_aver = m.occupancy_rate_ltm # Загрузка средняя фактическая / Actual average occupancy
                historic = m.revenue_ltm # Выручка историческая / Historical value
                # Цена за месяц, сказали пусть будет пустым
            price_month = ""# Цена за месяц, $, не оно - n.month_price
                # Площадь
            sqm = n.sqm
                # Вид
            view = n.view # Вид
                # Парковка
            parking = n.parking # P
                # Рестораны
            restraunt = n.restaurants # Ресторан/Restraunt
                # Басейны
            pool = n.bath # Бассейн / Pool
                # Кухня
            kitchen = n.kitchen # Кухня / Kitchen
                # Коворкинг
            coworking = n.workspace# Коворкинг/coworking
                # Руфтоп
            rooftop = n.rooftop# Руфтоп/ rooftop
                # Балкон, терраса, балкон на террасу
            balcony_terrace = n.terrace_balcony# Балкон, терасса/ Balcony or terrace
                # Хранение
            storage = n.storage # камера хранения/ storage room
                # Рейтинг
            rating = n.rating #stars, {n.reviews} reviews" # Рейтинг отзывов
                # Источник данных
            data_source = "" # Источник данных
                # Добавляем в список данные в цикле строк
            all_static.append([number, object, location, type_house, bedrooms, list_per, adr, actual_aver,\
            historic, price_month, sqm, view, parking, restraunt, pool, kitchen, coworking, rooftop, \
                balcony_terrace, storage, rating, data_source])
            
    print(f"info: Данные из базы получены и расформированы в списки. {number} строк.")

    f = 10
    alb =[ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V" ]
        # Формирование ячеек эксель из строк 
    for row in all_static:
        f += 1
        k = 0
        for s in row:
                # В каждом столбце "В", каждой строки, формируем крассивую ссылку
            if alb[k] == "B":
                cell_to_update = sheet[f"{alb[k]}{f}"]
                cell_to_update.value = s[0]
                cell_to_update.hyperlink = s[1]
                cell_to_update.font = Font(color="0000FF", underline="single")
                # В каждом столбце "С", каждой строки, формируем крассивую ссылку, если она есть, если нет, то просто Текст
            elif alb[k] == "C":
                if s[1] == "None":
                    cell_to_update = sheet[f"{alb[k]}{f}"]   # 'B11'
                    cell_to_update.value = s[0]
                else:
                    cell_to_update = sheet[f"{alb[k]}{f}"]
                    cell_to_update.value = s[0]
                    cell_to_update.hyperlink = f"https://www.google.com/maps?q={s[1]}"
                    cell_to_update.font = Font(color="0000FF", underline="single")
            else:
                cell_to_update = sheet[f"{alb[k]}{f}"]   # 'B11'
                cell_to_update.value = s
            k += 1

    print("info: Из данных сформированы ячейки которые будут записываться в Exel")
        # Формирование файла эксель библиотекой, долго, если много данных, позже подумаем...
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




