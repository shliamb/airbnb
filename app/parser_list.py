from functions_sys import begin_list, go_url, end_close, quick_sleep, scroll
from functions_list import build_url, find_id_url, get_url_next_page, save_ore_apdate_point
from worker_db import get_point
from colorama import Fore, Back, Style
import asyncio


async def get_list_id_url():
        # Приветствие
    print(Back.BLUE + "info: ID and URL collection started")
    print(Style.RESET_ALL)
        # Минимальные настройки
    country = "Bali-Province--Indonesia"
        # Сайт Airbnb сам принудительно выставит дату - месяц
    checkin_date = "[]"
    checkout_date = "[]"
    guests = 0
        # Корректировка времени для записи в базу
    time_correction = +8
    currency = "USD"
        # Для парса данных, в урл нужно добавить
    room_types = "Entire home%2Fapt" # Весь дом целиком
    #######

        # Получаю вилку стоимости из базы данных, в таблице Point всего одна страка - 1, если записи нет, присваиваю минимум
    point =  await get_point(1)
    if point is not None:
        price_min = str(point.price_min)
        price_max = str(point.price_max)
        print(f"info: Getting saved data in DB from the last session. {price_min}$, {price_max}$")
    else:
            # Если в базе нет записи, устанавливает  
        price_min = "10"
        price_max = "11"
        print("info: It's first running programm. price_min = 10$, price_max = 11$")
        # Формирую url
    url = await build_url(country, checkin_date, checkout_date, guests, currency, price_min, price_max, room_types)
        # Build Driver Chrome
    driver_list = await begin_list()
        # Парсинг в цикле списков id и url
    while True:
        code = await go_url(driver_list, url)
        if code is False:
            print(f"\nError: The url does not open correctly\n")
                # Close Driver Chrome
            await end_close(driver_list)
            break
            # Ожидание и скролинг
        await quick_sleep(5, 6)
        await scroll(driver_list)
            # Поиск данных на странице, сохранение
        await find_id_url(driver_list, time_correction, price_min, price_max)
            # Получение url следующей страницы
        url = await get_url_next_page(driver_list)
            # Если url следующей страницы нет
        if url == None:
            if price_max is None:
                await end_close(driver_list)
                return 
            elif int(price_max) < 16000:
                    # Закрытие драйвера Chrome
                await end_close(driver_list)
                print()
                    # Сдвигаем ценовой прайск поиска недвижимости
                price_min = str(int(price_min) + 1)
                price_max = str(int(price_max) + 1)
                    # Сохранение диапазона
                await save_ore_apdate_point(time_correction, price_min, price_max)
                print(f"info: The next price range: {price_min}$ to {price_max}$")
                    # Формируем новую страницу на основе новых цен
                url = await build_url(country, checkin_date, checkout_date, guests, currency, price_min, price_max, room_types)
                await quick_sleep(1, 2)
                    # Запускаем браузер для следующего поиска
                driver_list = await begin_list()
                await quick_sleep(1, 2)
                # Если цена максимальная перешла максимальный предел, то обнуляем ценообразование для следующего круга
            elif int(price_max) > 16000:
                    # Закрытие драйвера Chrome
                await end_close(driver_list)
                print()
                print(Back.BLUE + "info: The big crawl and list generation is over")
                print(Style.RESET_ALL)
                print("info: After a while, the next crawl and collection of lists will begin")
                price_min = "10"
                price_max = "11"
                print("info: It's first running programm. price_min = 10$, price_max = 11$")
                    # Сохранение диапазона
                await save_ore_apdate_point(time_correction, price_min, price_max)
                print("info: Update min = 10$ and max = 11$ to the database")
                    # Формируем новую страницу на основе новых цен
                url = await build_url(country, checkin_date, checkout_date, guests, currency, price_min, price_max, room_types)
                await quick_sleep(10, 20)
                    # Запускаем браузер для следующего поиска
                driver_list = await begin_list()
                await quick_sleep(1, 2)





max_attempts = 5
attempts = 0

while attempts < max_attempts:
    try:
        print("info: start parser")
        if __name__ == "__main__":
            asyncio.run(get_list_id_url())
        break
    except Exception as e:
        attempts += 1
        print(f"Произошла ошибка: {e}. Попытка {attempts} из {max_attempts}. Повторная попытка через 5 секунд...")
        asyncio.sleep(300)

if attempts == max_attempts:
    print("Превышено максимальное количество попыток. Завершение работы.")



# if __name__ == "__main__":
#     asyncio.run(get_list_id_url())
































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