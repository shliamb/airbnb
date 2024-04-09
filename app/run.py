from get_list import get_list_data
from get_object import get_data_obj


def run():
    # Запуск обхода списков по поиску
    complite_list = get_list_data()
    if complite_list is False:
        print("Error: The crawl of the lists in the search was completed unsuccessfully")
        return

    # Запуск детального переобхода объектов
    complite_obj = get_data_obj()
    if complite_obj is False:
        print("Error: Object traversal failed")
        return



if __name__ == "__main__":
    run()








