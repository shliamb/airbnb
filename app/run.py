from get_list import get_list_data
from get_object import get_data_obj
from parser_sys import quick_sleep
from worker_db import get_all_id_false, update_all_id
import asyncio
from colorama import Fore, Back, Style
import time


def run():
    i = 0
    while True:

        # Запуск обхода списков по поиску
        confirm_list = get_list_data()
        if confirm_list is False:
            print(Back.RED + "Error: The crawl of the lists in the search was completed unsuccessfully")
            print(Style.RESET_ALL)

        # Проверка ресурса не пропарсеных объектов
        all_false_id = asyncio.run(get_all_id_false())
        if all_false_id == []:
            data = {"passed_flag": False}
            asyncio.run(update_all_id(data))
            print(Back.RED + "info: Zeroing object parsing")
            print(Style.RESET_ALL)
            # Прверяет, если записей больше нет, которые не проходили, то обнуляет все, для очередного прохода.

        # Запуск детального обхода объектов
        confirm_obj = get_data_obj()
        if confirm_obj is False:
            print(Back.RED + "Error: Object traversal failed")
            print(Style.RESET_ALL)

        
        #quick_sleep(1,2)

        i += 1
        print(Back.BLUE + f"Info: {i} big cicles Parsing is completed. Congratulation.")
        print(Style.RESET_ALL)


max_attempts = 5
attempts = 0

# run()
asyncio.run(run())


# while attempts < max_attempts:
#     try:
#         print("info: start parser")
#         if __name__ == "__main__":
#             run()
#         break
#     except Exception as e:
#         attempts += 1
#         print(f"Произошла ошибка: {e}. Попытка {attempts} из {max_attempts}. Повторная попытка через 5 секунд...")
#         time.sleep(5)

# if attempts == max_attempts:
#     print("Превышено максимальное количество попыток. Завершение работы.")





