import shutil
import random
import os


# PROFILESS CHROME
def profil() -> str:

    profil.counter += 1
    i = profil.counter

    if i >= 30:
        folder_path = "./profiles/"
        for item_name in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item_name)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # Удаление файла или символической ссылки
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Рекурсивное удаление директории
        print("info: Profiles Chrome is deleted")
        i = 0

    name = "profile" + str(random.randint(1, 10))
    return name


    # Надо удалять профиля в папке /profile/, они сами появятся при работе.
    # Удалять надо, иначе блокирует airbnb через какое то время.

