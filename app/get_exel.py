from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
from worker_db import get_all_rooms_not_None2, get_all_rooms_not_None#, get_rooms_sorted_by_bedroom_asc, get_rooms_sorted_by_bedroom_desc
import asyncio
import shutil


async def get_rooms_data(choice):
    if choice == "1":
        return await get_all_rooms_not_None2()
    # elif choice == "2":
    #     return await get_all_rooms_not_None3()
    # elif choice == "3":
    #     return await get_all_rooms_not_None4()



async def get_exel_file(choice):
    sourcefile = "./file/The Heigts анализ_research.xlsx"
    newfile = "./file/stat_data.xlsx"
    shutil.copy(sourcefile, newfile)

    workbook = load_workbook(filename=newfile)
    sheet = workbook["расчет ADR и OccupancyADR and O"]

    rooms_data = await get_rooms_data(choice)

    all_static = []
    for number, (n, m) in enumerate(rooms_data, start=0):
        number += 1
        object =  [n.title, n.url] # Объект / Object
        #if m is not None:
        if m:
            url_location = m.location_lat, m.location_lng
        else:
            url_location = ""
        location = [n.location, url_location] #  f"https://www.google.com/maps?q={n.location_lat},{n.location_lng}" 
        type_house = n.type_house # Категория
        bedrooms = 1 if n.bedroom == 0 else n.bedroom # Число br / Quantity of br
        list_per, adr, actual_aver, historic, price_month = "", "", "", "", ""
        if m:
            list_per = m.days_available_ltm #"Срок размещения" # Срок размещения / Listing period
            adr = m.average_daily_rate_ltm #"Средняя цена юнита за сутки" # Средняя цена юнита за сутки, $ / ADR
            actual_aver = m.occupancy_rate_ltm #"Загрузка средняя фактическая" # Загрузка средняя фактическая / Actual average occupancy
            historic = m.revenue_ltm #"Выручка историческая" # Выручка историческая / Historical value
        price_month = ""#n.month_price # Цена за месяц, $
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
        data_source = "" # Источник данных

        all_static.append([number, object, location, type_house, bedrooms, list_per, adr, actual_aver,\
        historic, price_month, sqm, view, parking, restraunt, pool, kitchen, coworking, rooftop, \
            balcony_terrace, storage, rating, data_source]) 

    alb = [chr(i) for i in range(ord('A'), ord('W'))]  # Создает список букв от A до V
    for row_num, row in enumerate(all_static, start=11):
        for col_num, value in enumerate(row):
            col_letter = alb[col_num]
            cell_ref = f"{col_letter}{row_num}"
            cell = sheet[cell_ref]

            if col_letter == "B":
                cell.value, cell.hyperlink = value[0], value[1]
                cell.font = Font(color="0000FF", underline="single")
            elif col_letter == "C":
                cell.value = value[0]
                if value[1] != "None":
                    cell.hyperlink = f"https://www.google.com/maps?q={value[1]}"
                    cell.font = Font(color="0000FF", underline="single")
            else:
                cell.value = value

    workbook.save(filename=newfile)
    workbook.close()  # Закрыть рабочую книгу вручную
    print("info: Exel file is complete")
    return newfile



if __name__ == "__main__":
    choice = "1"  # Assigning "1" to the variable choice, not comparing it
    asyncio.run(get_exel_file(choice))









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






# def get_rooms_data(choice):
#     if choice == "1":
#         return get_all_rooms_not_None2()
#     # elif choice == "2":
#     #     return get_all_rooms_not_None3()
#     # elif choice == "3":
#     #     return get_all_rooms_not_None4()

# async def get_exel_file(choice):
#     sourcefile = "./file/The Heigts анализ_research.xlsx"
#     newfile = "./file/stat_data.xlsx"
#     shutil.copy(sourcefile, newfile)

#     workbook = load_workbook(filename=newfile)
#     sheet = workbook["расчет ADR и OccupancyADR and O"] 

#     rooms_data = await get_rooms_data(choice)

#     all_static = []
#     for number, (n, m) in enumerate(rooms_data, start=0):
#         number += 1
#         object =  [f"{n.title}", f"{n.url}"] # Объект / Object
#         #if m is not None:
#         if m is not None:
#             url_location = f"{m.location_lat},{m.location_lng}"
#         else:
#             url_location = ""
#         location = [f"{n.location}", f"{url_location}"] #  f"https://www.google.com/maps?q={n.location_lat},{n.location_lng}" 
#         type_house = n.type_house # Категория
#         bedrooms = 1 if n.bedroom == 0 else n.bedroom # Число br / Quantity of br
#         list_per, adr, actual_aver, historic, price_month = "", "", "", "", ""
#         if m is not None:
#             list_per = m.days_available_ltm #"Срок размещения" # Срок размещения / Listing period
#             adr = m.average_daily_rate_ltm #"Средняя цена юнита за сутки" # Средняя цена юнита за сутки, $ / ADR
#             actual_aver = m.occupancy_rate_ltm #"Загрузка средняя фактическая" # Загрузка средняя фактическая / Actual average occupancy
#             historic = m.revenue_ltm #"Выручка историческая" # Выручка историческая / Historical value
#         price_month = ""#n.month_price # Цена за месяц, $
#         sqm = n.sqm # Площадь, м2
#         view = n.view # Вид
#         parking = n.parking # P
#         restraunt = n.restaurants # Ресторан/Restraunt
#         pool = n.bath # Бассейн / Pool
#         kitchen = n.kitchen # Кухня / Kitchen
#         coworking = n.workspace# Коворкинг/coworking
#         rooftop = n.rooftop# Руфтоп/ rooftop
#         balcony_terrace = n.terrace_balcony# Балкон, терасса/ Balcony or terrace
#         storage = n.storage # камера хранения/ storage room
#         rating = n.rating # Рейтинг отзывов
#         data_source = "" # Источник данных

#         all_static.append([number, object, location, type_house, bedrooms, list_per, adr, actual_aver,\
#         historic, price_month, sqm, view, parking, restraunt, pool, kitchen, coworking, rooftop, \
#             balcony_terrace, storage, rating, data_source]) 

#     alb = [chr(i) for i in range(ord('A'), ord('W'))]  # Создает список букв от A до V
#     for row_num, row in enumerate(all_static, start=11):
#         for col_num, value in enumerate(row):
#             col_letter = alb[col_num]
#             cell_ref = f"{col_letter}{row_num}"
#             cell = sheet[cell_ref]

#             if col_letter == "B":
#                 cell.value, cell.hyperlink = value[0], value[1]
#                 cell.font = Font(color="0000FF", underline="single")
#             elif col_letter == "C":
#                 cell.value = value[0]
#                 if value[1] != "None":
#                     cell.hyperlink = f"https://www.google.com/maps?q={value[1]}"
#                     cell.font = Font(color="0000FF", underline="single")
#             else:
#                 cell.value = value

#     workbook.save(filename=newfile)
#     print("info: Exel file is complete")
#     return newfile



# if __name__ == "__main__":
#     choice = "1"  # Assigning "1" to the variable choice, not comparing it
#     asyncio.run(get_exel_file(choice))