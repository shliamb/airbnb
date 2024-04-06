from sys_def_scraper import ( go_url, begin, end_close, quick_sleep, response_code, scroll)
from airbnb_def_scraper import ( build_url, quick_sleep, find_data_room, get_url_next_page)
from get_room_airbnb import get_room_data


# DATA FOR SEARCH URL
location = "Bali"
checkin_date = "2024-05-01"
checkout_date = "2024-05-07"
guests = 1
time_correction = +3
# room_types = "Private room"




#### GETTING DATA FOR ALL ROOMS ####
# Build 1rst URL to citi
def get_rooms_data(location, checkin_date, checkout_date, guests, time_correction):
    url = build_url(location, checkin_date, checkout_date, guests)
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
        break
    get_room_data(location) # Run geting room data
    

if __name__ == "__main__":
    get_rooms_data(location, checkin_date, checkout_date, guests, time_correction)



















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