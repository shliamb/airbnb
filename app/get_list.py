from parser_sys import ( go_url, begin, end_close, quick_sleep, response_code, scroll)
from parser_airbnb import ( build_url, quick_sleep, find_data_room, get_url_next_page, get_position)
from worker_db import update_position
from parser_sys import day_utcnow
from colorama import Fore, Back, Style
import asyncio



#### GETTING DATA FOR ALL ROOMS ####
# Build 1rst URL to citi
def get_list_data():
    data_id =[]
    i = 0
    print()
    print("info: Starting getting lists of id and url objects")
    confirm = False
    # DATA FOR SEARCH URL
    location = "Bali-Province--Indonesia" # Bali Как точно надо? 
    checkin_date = "[]" # Он сам ставит на 1 месяц 
    checkout_date = "[]"
    guests = 0 # Гости Сколько гостей устанавливать в поиске?
    time_correction = +8
    currency = "USD"
    room_types = "Entire home%2Fapt" # Весь дом целиком



    data_position = asyncio.run(get_position(1))
    if data_position is not None:
        price_min = str(data_position.price_min)
        price_max = str(data_position.price_max)
        print(f"info: Getting saved data from the last session. {price_min}$, {price_max}$")
    else:
        price_min = "10" # Не уверен что стоит вообще собирать от 10$ за ночь, там амбар сдают))
        price_max = "11"
        print("info: It's first running. price_min = 10$, price_max = 11$")



    url = build_url(location, checkin_date, checkout_date, guests,\
                     currency, price_min, price_max, room_types)
    # Build Driver Chrome
    driver = begin()

    while True:

        
        code = go_url(driver, url)
        if code is False:
            print(f"\nError: The url does not open correctly\n")
            # Close Driver Chrome
            end_close(driver)
            break
        
        quick_sleep(5, 6)
        scroll(driver)

        # Find data room and save to DB
        data_id = find_data_room(driver, location, time_correction, price_min, price_max)

        if i >= 10:
            print(Back.BLUE + f"info: {i} iterations have been completed.")
            print(Style.RESET_ALL)
            break
        i += 1
        # Find url next page
        url = get_url_next_page(driver)
        if url == None:
            #i += 1
            if int(price_max) < 16000:
                # Close Driver Chrome
                end_close(driver)
                price_min = str(int(price_min) + 1)
                price_max = str(int(price_max) + 1)
                print(f"info: from {price_min}$ to {price_max}$")
                url = build_url(location, checkin_date, checkout_date, guests,\
                        currency, price_min, price_max, room_types)
                quick_sleep(1, 2)
                # Build Driver Chrome
                driver = begin()
                quick_sleep(1, 2)
            else:
                min = 10
                max = 11
                list_date_update = day_utcnow(time_correction)
                price_data = {"date": list_date_update, "price_min": min, "price_max": max}
                asyncio.run(update_position(1, price_data))
                print(f"info: Update min = 10$ and max = 11$ to the database")
                # Close Driver Chrome
                end_close(driver)
                print(Back.BLUE + "info: The search list for objects has been completed")
                print(Style.RESET_ALL)
                return data_id
            
    return data_id

if __name__ == "__main__":
    get_list_data()





































# # Scroll page
# scroll(driver)

# # Build Driver Chrome  - запуск настроек, создание экземпляров, драйвер
# driver = begin()

# # Response code - Получить код ответа сервера по url при помощи response
# code = response_code(url)
# print(f"\nHTTP response code: {code}\n")

# # Go to URL - переход на url Selenium
# go_url(driver, url)

# # Wait time - Запуск тайм слип на случайное число секунд из диапозона
# quick_sleep(5, 6)

# # Find url - Поиск и возврат href по параметрам, <a aria-label="Next" href= 
# data_url = find_url(driver, "a", "aria-label", "Next")
# print(data_url)

# # Find url next page - просто возврат url следующей страницы для сайта airbnb
# url_next = get_url_next_page(driver)
# print(url_next)

# # Find data Airbnb - специализированный скраблинг данных room с Airbnb
# data_room = find_data_room(driver)
# print(data_room)

# # Close Driver Chrome - закрытие сеанса 
# end_close(driver)

# if __name__ == "__main__":
#     get_rooms_data()