from colorama import Fore, Back, Style
import shutil
import random
import asyncio
import os

# PROFILESS CHROME

def call_counter(func):
    def helper(*args, **kwargs): 
        helper.calls += 1
        if helper.calls >= 10:
            # Получаю folder из аргументов
            folder_path = args[0] if args else kwargs.get('folder', '')
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
                os.makedirs(folder_path)
                print(Back.BLUE + "info: Profiles Chrome is deleted")
                print(Style.RESET_ALL)
            helper.calls = 0
        return func(*args, **kwargs) 
    helper.calls = 0
    return helper

@call_counter
def profil(folder) -> str:
    return f"profile{random.randint(1, 10)}"



if __name__ == "__main__":
    asyncio.run(profil())























# "./profiles/"





# PROFILESS CHROME
# def call_counter(func): # входит функция profil
#     def helper():
#         helper.calls += 1
#         if helper.calls >= 10:
#             folder_path = folder
#             if os.path.exists(folder_path):
#                 shutil.rmtree(folder_path)  # Удаляет папку profiles
#                 os.makedirs(folder_path) # Создает папку profiles
#                 print(Back.BLUE + "info: Profiles Chrome is deleted")
#                 print(Style.RESET_ALL)
#             helper.calls = 0
#         return func() # выходит результат функции profil
#     helper.calls = 0
#     return helper



# @call_counter
# def profil(folder) -> str:
#     return f"profile{random.randint(1, 10)}"

# if __name__ == "__main__":
#     asyncio.run(profil())


# PROFILESS CHROME
# def profil() -> str:

#     profil.counter += 1
#     i = profil.counter

#     if i >= 30:
#         folder_path = "./profiles/"
#         for item_name in os.listdir(folder_path):
#             item_path = os.path.join(folder_path, item_name)
#             if os.path.isfile(item_path) or os.path.islink(item_path):
#                 os.unlink(item_path)  # Удаление файла или символической ссылки
#             elif os.path.isdir(item_path):
#                 shutil.rmtree(item_path)  # удаление директории
#         print(Back.BLUE + "info: Profiles Chrome is deleted")
#         print(Style.RESET_ALL)
#         i = 0
#         profil.counter = 0

#     name = "profile" + str(random.randint(1, 10))
#     return name


    # Надо удалять профиля в папке /profile/, они сами появятся при работе.
    # Удалять надо, иначе блокирует airbnb через какое то время.

