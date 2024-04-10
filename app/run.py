from get_list import get_list_data
from get_object import get_data_obj
from parser_sys import quick_sleep
import time


def run():
    # while True:
    #Запуск обхода списков по поиску
    complite_list = get_list_data()
    if complite_list is False:
        print("Error: The crawl of the lists in the search was completed unsuccessfully")
        return

    # Запуск детального переобхода объектов
    complite_obj = get_data_obj()
    if complite_obj is False:
        print("Error: Object traversal failed")
        return
    #quick_sleep(2,3)
    print("Info: Parsing is complit.")


if __name__ == "__main__":
    run()








