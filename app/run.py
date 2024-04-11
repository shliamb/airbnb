from get_list import get_list_data
from get_object import get_data_obj
from parser_sys import quick_sleep
from worker_db import get_rooms_by_false_parse, update_all_rooms
import asyncio
from colorama import Fore, Back, Style
# import time


def run():
    i = 0
    while True:



        # # Запуск обхода списков по поиску
        data_id = get_list_data()
        if data_id is False:
            print("Error: The crawl of the lists in the search was completed unsuccessfully")
            return

        data_room = asyncio.run(get_rooms_by_false_parse())
        if data_room is None:
            data = {"is_parse": False}
            asyncio.run(update_all_rooms(data))
            print(Back.RED + "info: Zeroing object parsing")
            print(Style.RESET_ALL)
            # Прверяет, если записей больше нет, которые не проходили, то обнуляет все, для очередного прохода.


        # Запуск детального обхода объектов
        complite_obj = get_data_obj()
        if complite_obj is False:
            print("Error: Object traversal failed")
            return
        
        #quick_sleep(2,3)
        i += 1
        print(Back.BLUE + f"Info: {i} big cicles Parsing is completed. Congratulation.")
        print(Style.RESET_ALL)


if __name__ == "__main__":
    run()








