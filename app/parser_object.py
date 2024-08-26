from functions_sys import begin_object, go_url, end_close, quick_sleep, scroll
from functions_object import find_data_object
from worker_db import get_10_id_false, update_id
from colorama import Fore, Back, Style
import asyncio
import re

# Сбор данных каждого объекта по ID и URL
async def get_data_obj():
    print(Back.BLUE + "info: Starting object data collection")
    print(Style.RESET_ALL)
    time_correction = +8
    currency = "USD"
        # Из базы будет брать 10 id не занятые и не пройденые
    count = 10
        # Цикл парсера
    while True:
            # Получение списка из максимум count штук id и upl
        data_room = await get_10_id_false(count)
            # Если нету на проходобъектов, то пробует через 300 сек в цикле
        while data_room is None or data_room == []:
            print(Back.RED + "Error: The objects in the database are over, let's wait a bit.")
            print(Style.RESET_ALL)
            await asyncio.sleep(300)
            # await quick_sleep(250, 300)
            data_room = await get_10_id_false(count)


            # Перебор по полученым id 
        for data in data_room:
            id = data.id
            url = data.url
                # Помечаем для остальных парсеров, что этот объект взяли в работу
            data_false = {"busy_flag": True}
            await update_id(id, data_false)
                #
            pattern = r'(/listing/\d+|rooms/\d+)'
            url_object = re.sub(pattern, r'\1/amenities', url)
                # Build Driver Chrome
            driver_object = await begin_object()
                # Go to URL
            code = await go_url(driver_object, url_object)
            if code is False:
                print(f"\nError: The url does not open correctly\n")
                    # Close Driver Chrome
                await end_close(driver_object)
                break

            await quick_sleep(2, 3)
                # Find data room and save to DB
            await find_data_object(driver_object, id, url_object, time_correction, currency)
            #await quick_sleep(500, 600)
                # Close Driver Chrome
            await end_close(driver_object)
                # Помечаем, что id  объкта уже парсили
            data_true = {"busy_flag": False, "passed_flag": True}
            await update_id(id, data_true)
        print(Back.BLUE + f"info: The following {count} objects")
        print(Style.RESET_ALL)





attempts = 0
max_attempts = 5  # Примерное количество максимальных попыток

async def main():
    global attempts
    while attempts < max_attempts:
        try:
            print("info: start parser")
            if __name__ == "__main__":
                await get_data_obj()
            break  # Если функция выполнится без ошибок, выйдем из цикла
        except Exception as e:
            attempts += 1
            print(f"Произошла ошибка: {e}. Попытка {attempts} из {max_attempts}. Повторная попытка через 300 секунд...")
            await asyncio.sleep(300)  # Ожидание перед повторной попыткой

# Запуск асинхронной функции main
asyncio.run(main())













# if __name__ == "__main__":
#     asyncio.run(get_data_obj())

    # Scroll page
# await scroll(driver)