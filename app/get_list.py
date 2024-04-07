from parser_sys import ( go_url, begin, end_close, quick_sleep, response_code, scroll)
from parser_airbnb import ( build_url, quick_sleep, find_data_room, get_url_next_page)
from get_object import get_room_data



#### GETTING DATA FOR ALL ROOMS ####
# Build 1rst URL to citi
def get_list_data():
    confirm = False
    # DATA FOR SEARCH URL
    location = "Bali-Province--Indonesia" # Bali Как точно надо? 
    checkin_date = "[]" # Он сам ставит на 1 месяц 
    checkout_date = "[]"
    guests = 1 # Гости Сколько гостей устанавливать в поиске?
    time_correction = +5
    currency = "USD"
    price_min = "10" # Не уверен что стоит вообще собирать от 10$ за ночь, там амбар сдают))
    price_max = "11"
    room_types = "Entire home%2Fapt" # Весь дом целиком
    # Добавить в таблицу Task ячейку 

    url = build_url(location, checkin_date, checkout_date, guests, currency, price_min, price_max, room_types)
    # Build Driver Chrome
    driver = begin()
    i = 1
    while True:
        # Response code
        code = response_code(url)
        if code != 200:
            print(f"\nHTTP response code: {code}\n")
            # Close Driver Chrome
            end_close(driver)
            break
        # Go to URL
        go_url(driver, url)
        # Wait time
        quick_sleep(5, 6)
        # Scroll page
        scroll(driver)
        # Find data room and save to DB
        find_data_room(driver, location, time_correction)
        quick_sleep(1, 2)
        # Find url next page
        url = get_url_next_page(driver)
        if url == None:
            # Close Driver Chrome
            end_close(driver)
            break
        i += 1
        quick_sleep(1, 2)

    confirm = True
    return confirm





def get_data_obj():
    confirm = False
    # DATA FOR SEARCH ID
    location = "Bali-Province--Indonesia" # Bali Как точно надо? 
    get_room_data(location) # Run geting room data
    confirm = True
    return confirm








































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