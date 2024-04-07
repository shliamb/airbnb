from get_list import get_list_data
from get_object import get_data_obj


def run():
    # Запуск обхода списков по поиску
    complite_list = get_list_data()
    if complite_list is False:
        print("Error, ...1")
        return

    # Не совсем определился по какому параметру выбрать разделение всех объектов в базе не части, так как
    # закидывать в оперативку все id не очень умно, то ли по локациям, то ли по ценам, то ли по типу недвижемости

    # Так же нужно как то реализовать запись в таблицу Task текущую итерацию, к примеру предел сумм поиска
    # для того, что бы, при возникновении сбоя, следующий обход начать с того места где остановились.
    
    # Запуск детального переобхода объектов
    complite_obj = get_data_obj()
    if complite_obj is False:
        print("Error, ...2")
        return



if __name__ == "__main__":
    run()