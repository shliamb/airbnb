from get_list import get_list_data
from get_object import get_data_obj
from parser_sys import quick_sleep
from colorama import Fore, Back, Style
import time


def run():
    i = 0
    while True:

        # Запуск обхода списков по поиску
        data_id = get_list_data()
        if data_id is False:
            print("Error: The crawl of the lists in the search was completed unsuccessfully")
            return

        # Запуск детального обхода объектов
        complite_obj = get_data_obj(data_id)
        if complite_obj is False:
            print("Error: Object traversal failed")
            return
        
        #quick_sleep(2,3)
        i += 1
        print(Back.BLUE + f"Info: Parsing is complit {i} cicles.")
        print(Style.RESET_ALL)


if __name__ == "__main__":
    run()








