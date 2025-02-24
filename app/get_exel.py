from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
from worker_db import get_all_airbnb_airdna, get_all_airbnb_airdna_sorted_bedroom_asc, get_all_airbnb_airdna_sorted_bedroom_desc
import asyncio
import shutil


async def get_exel_file(choice):
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
        data = await get_all_airbnb_airdna()
    elif choice == "2":
        data = await get_all_airbnb_airdna_sorted_bedroom_asc()
    elif choice == "3":
        data = await get_all_airbnb_airdna_sorted_bedroom_desc()

        # Переменные
    all_static = []
    number = 0

    list_per = adr = actual_aver = historic = url_location = location = ""

        # Передаем в переменные данные из ответа базы в цыкле каждая строка
    for n, m in data:
            # Фильтруем записи без бедрум и если в локации пусто
        if n.bedroom != None and n.location != "":
                # Порядковый номер строк в ексель
            number += 1
                # Название объекта и ссылка на него в airdna
            url_aird = f"https://app.airdna.co/data/listing/abnb_{n.id}"
            object =  [n.title, url_aird]
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
                actual_aver = str(int(m.occupancy_rate_ltm)) + " %" # Загрузка средняя фактическая / Actual average occupancy
                historic = m.revenue_ltm # Выручка историческая / Historical value
                # Цена за месяц, сказали пусть будет пустым
            price_month = ""# Цена за месяц, $, не оно - n.month_price
                # Площадь
            sqm = n.sqm
                # Вид
            view = n.view # Вид
                # Парковка
            parking = 1 if n.parking != "" else 0 # P
                # Рестораны
            restraunt = 1 if n.restaurants != "" else 0  # Ресторан/Restraunt
                # Басейны
            pool = 1 if n.bath != "" else 0 # Бассейн / Pool
                # Кухня
            kitchen = 1 if n.kitchen != "" else 0 # Кухня / Kitchen
                # Коворкинг
            coworking = 1 if n.workspace != "" else 0 # Коворкинг/coworking
                # Руфтоп
            rooftop = 1 if n.rooftop != "" else 0 # Руфтоп/ rooftop
                # Балкон, терраса, балкон на террасу
            balcony_terrace = 1 if n.terrace_balcony != "" else 0 # Балкон, терасса/ Balcony or terrace
                # Хранение
            storage = 1 if n.storage != "" else 0 # камера хранения/ storage room
                # Рейтинг
            rating = 5 if n.rating > 5 else round(n.rating, 2) #stars, {n.reviews} reviews" # Рейтинг отзывов
                # Источник данных
            data_source = ["airbnb", n.url]  # Источник данных
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
            elif alb[k] == "V":
                cell_to_update = sheet[f"{alb[k]}{f}"]
                cell_to_update.value = s[0]
                cell_to_update.hyperlink = s[1]
                cell_to_update.font = Font(color="0000FF", underline="single")
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
    asyncio.run(get_exel_file())
















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




