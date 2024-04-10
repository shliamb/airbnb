from get_list import get_list_data
from get_object import get_data_obj
from parser_sys import quick_sleep
from colorama import Fore, Back, Style
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
    print(Back.BLUE + "Info: Parsing is complit.")
    print(Style.RESET_ALL)


if __name__ == "__main__":
    run()








