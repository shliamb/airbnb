from worker_db import get_id, update_id, adding_id, get_point, adding_point, update_point
from functions_sys import quick_sleep, day_utcnow
from bs4 import BeautifulSoup
import asyncio
import re



#### INDIVIDUAL FUNCTIONS BY ROOMS ####

# Из входных параметров строит url для парса id и url
async def build_url(location, checkin_date, checkout_date, guests=None, currency=None, price_min=None, price_max=None, room_types=None) -> str:
    url = f"https://www.airbnb.com/s/{location}/homes?checkin={checkin_date}&checkout={checkout_date}&enable_auto_translate=false&locale=en"
    if guests:
        url += f"&guests={guests}"
    # if amenities:
    #     url += "&amenities=" + "+".join(amenities)
    if currency:
        url += f"&currency={currency}" 
    if price_min:
        url += f"&price_min={price_min}"   
    if price_max:
        url += f"&price_max={price_max}"
    if room_types:
        url += f"&room_types[]={room_types}"
    print("info: Building a url to pars list id and url")
    return url

# FIND URL NEXT PAGE 
async def get_url_next_page(driver) -> str:
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    data = nand.find("a", {"aria-label" : "Next"})
    url_href = None
    if data:
        url_href = "https://www.airbnb.com/" + data.get("href")
        print("info: Get url next page")
    return url_href

# SAVE POINT
async def save_ore_apdate_point(time_correction: int, price_min: str, price_max: str) -> bool:
    confirmation = False
        # Get day and time now
    list_date_update = await day_utcnow(time_correction)
        # price_min, price_max
    data_position = await get_point(1) # Для проверки что существует
    min = int(price_min)
    max = int(price_max)
    if data_position is not None:
        price_data = {"id": 1, "date": list_date_update, "price_min": min, "price_max": max}
        await update_point(1, price_data)
        print(f"info: Update to DB price_min: {min}, price_max: {max}")
        confirmation = True
    else:
        price_data = {"id": 1, "date": list_date_update, "price_min": min, "price_max": max}
        await adding_point(price_data)
        print(f"info: Added to DB price_min: {min}, price_max: {max}")
        confirmation = True
    return confirmation

# SAVE URL ID
async def save_id_url_to_db(id, room_data) -> bool:
    confirmation = False
    #id = room_data['id']
    data_room = await get_id(id)
        # Update data to room, if is outdated
    if data_room is not None:
            # Update data list
        await update_id(id, room_data)
        print(f"info: Update {id} and url to the database")
    else:
            # Adding data room
        await adding_id(room_data)
        print(f"info: Added {id} and url to the database")
        confirmation = True

    return confirmation

# Это та часть что собирает ID URL и все... типа сам парсер
# Сбор со страниц поиска id и url
async def find_id_url(driver, time_correction, price_min, price_max):

    print("info: Go parsing list home in the search.")
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    await quick_sleep(2, 3)

    for el in nand.find_all("div", {"data-testid": "card-container"}):
        if el is None:
            print("Error: No data found on the html url")
            return
        print("---------")

        # Забираем ID и URL
        room_url = el.find("a", {"class": "l1ovpqvx"})
        if room_url:
            url_href = room_url.get("href")
            url_room = f"https://www.airbnb.com{url_href}"
            print("info: url_room:", url_room)
            # ID ROOM
            pattern = r"/(?:rooms|listing)/(\d+)"
            match = re.search(pattern, url_href)
            if match:
                id = int(match.group(1))
                print("info: id:", id)
            else:
                id = 0
                print("Error: Ошибка поиска ID")
        else:
            id = 0
            print("Error: Ошибка поиска URl")

        # Готовим данные к сохранению
        list_date_update = await day_utcnow(time_correction)
        room_data = {"id": id, "url": url_room, "date": list_date_update}

            # Записываем данные id и url в DB
        await save_id_url_to_db(id, room_data)
        
    return