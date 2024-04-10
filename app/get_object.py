from parser_sys import ( go_url, begin, end_close, quick_sleep, response_code, scroll)
from parser_airbnb import ( find_data_object, build_url, quick_sleep, find_data_room, get_url_next_page)
from worker_db import get_rooms_by_false_parse
# from get_list import get_list_data
from colorama import Fore, Back, Style
import asyncio
import re


#### GETTING DATA FOR ROOM AT ITS ID IN DB ####

def get_data_obj():
    confirm = False
    location = "Bali-Province--Indonesia"
    time_correction = +8
    currency = "USD"
    data_room = asyncio.run(get_rooms_by_false_parse())

    if data_room is None:
        print("Error: There is no data, I may have already bypassed everything.")
        return

    # Перебор по полученым id из базы входящей категории
    for data in data_room:
        id = data.id
        url = data.url_room
        print(Back.BLUE + f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {id} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(Style.RESET_ALL)
        pattern = r'(/rooms/\d+)'
        url_room = re.sub(pattern, r'\1/amenities', url)

        # Build Driver Chrome
        driver = begin()
        # Go to URL
        code = go_url(driver, url_room)
        if code is False:
            print(f"\nError: The url does not open correctly\n")
            # Close Driver Chrome
            end_close(driver)
            break
        # Wait time
        quick_sleep(5, 6)
        # Scroll page
        scroll(driver)
        # Find data room and save to DB
        find_data_object(driver, id, url_room, location, time_correction, currency)
        # quick_sleep(1, 2)

        #quick_sleep(500, 600)
        print()
        # Close Driver Chrome
        end_close(driver)

    print(Back.BLUE + "info: The parse Objects has been completed")
    print(Style.RESET_ALL)
    confirm = True
    return confirm

if __name__ == "__main__":
    get_data_obj()

