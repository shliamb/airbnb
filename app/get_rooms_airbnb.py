from scraper import ( go_url, begin, build_url, end_close, quick_sleep, response_code, find_data_room,\
get_url_next_page, scroll, find_url )
import time
import random


# DATA FOR SEARCH URL
location = "Bali"
checkin_date = "2024-05-01"
checkout_date = "2024-05-07"
guests = 2
# room_types = "Private room"




#### GETTING DATA FOR ALL ROOMS ####

# Build 1rst URL to citi
url = build_url(location, checkin_date, checkout_date, guests)
# Build Driver Chrome
driver = begin()
i = 1
while True:
    print(f"Is {i} page:")
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

    # Find data room
    data_room = find_data_room(driver)
    quick_sleep(1, 2)
    # Find url next page
    url = get_url_next_page(driver)
    if url == None:
        # Close Driver Chrome
        end_close(driver)
        break
    i += 1
    quick_sleep(1, 2)















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