from options_chrome import profil
from worker_db import get_rooms_by_id, update_rooms, adding_rooms
from datetime import datetime, timezone
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import asyncio
import requests
import time
import random
import sys
import re
# import pandas as pd
# import re

#### SYSTEM FUNCTIONS ####

# Begin work, options driver, return driver
def begin():
    ua = UserAgent(browsers=['edge', 'chrome']) # ua = UserAgent(browsers=['edge', 'chrome'])  ua = UserAgent(os='linux') ua = UserAgent(min_version=120.0)  ua = UserAgent(platforms='mobile')  
    service = Service() # Попробовать удалить..
    options = Options()
    # OPTINONS DRIVER CHRONE SELENIUM
    prof = profil()
    print("\nOPTIONS DRIVER CHROME:")
    ####
    def add_options(options, *args):
        for arg in args:
            options.add_argument(arg)
            print(arg)
    ####
    add_options(options, "--disable-webgl", "--disable-gpu", "--disable-3d-apis", "--enable-virtual-keyboard", "--mute-audio", "--disable-plugins-discovery", "--profile-directory=Default", "disable-infobars", "start-maximized", "--disable-blink-features=AutomationControlled", f"--user-agent={ua.random}", f"user-data-dir=./profiles/{prof}/") # , "--incognito", f"--proxy-server={PROXY}", "--headless=new")
    ####
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(service=service, options=options)
    # driver.delete_all_cookies()
    driver.set_window_size(1200,800)
    driver.set_window_position(0,0)
    return driver
####

# QUICK SLEEP - промежуток случайных чисел на входе, между которыми будет случайный период остановки
def quick_sleep(mi: int, ma: int) -> bool:
    confirm = False
    num = random.randint(mi, ma)
    print(f"wait {num} seconds")
    def spinning_cursor():
        while True:
            for cursor in '|/-\|':
                yield cursor
    spinner = spinning_cursor()
    i = 0
    while i < num:
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.04)
        sys.stdout.write('\r')
        i += 0.042
    #print()
    confirm = True
    return confirm

# RESPONSE CODE URL - на вход url, на выход код ответа сервера
def response_code(url: str) -> int:
    response = requests.get(url)
    code = response.status_code
    return code or None

# GOING TO THE SITE
def go_url(driver, url: str) -> bool:
    confirmation = False
    code = response_code(url)
    if code == 200:
        driver.get(url)
        confirmation = True
    else:
        confirmation = False
        print(f"Error: server back code response - {code}")
    return confirmation
    
# CLOSE DRIVER CHROME
def end_close(driver):
    driver.close()
    driver.quit()

# GET FLOAT at STR - Из строки получаем только не целое число
def str_int(num: str) -> float:
    pattern = r"(\d{1,3}(?:,\d{3})*(?:\.\d+)?)"
    num = re.sub(r"[^\d.,]", "", num)
    str_num = re.search(pattern, num)
    if not str_num:
        return None
    float_num_str = str_num.group(1).replace(',', '')
    try:
        float_num = float(float_num_str)
        return float_num
    except ValueError:
        return None

# GET DAY AND TIME
def day_utcnow() -> str:
    a = datetime.now(timezone.utc).replace(tzinfo=None)
    day_str = a.strftime("%Y-%m-%d %H:%M:%S")
    day = datetime.strptime(day_str, '%Y-%m-%d %H:%M:%S')
    return day

# FIND SOME URL BT4
def find_url(driver, tag: str, name: str, value: str) -> str:
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    data = nand.find(tag, {name : value})
    url_href = None
    if data:
        url_href = data.get("href")
    return url_href

# SCROLL PAGE SLOWLY - Медленная прокрутка страницы вниз
def scroll(driver):
    scroll_pause_time = random.uniform(0.31, 0.83) # Задержка между прокрутками
    screen_height = driver.execute_script("return window.innerHeight;")  # Получить высоту окна браузера
    i = 1
    while True:
        # Прокрутить на одну высоту окна за раз
        driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
        i += 1
        time.sleep(scroll_pause_time)
        # Получить прокрученную высоту
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        # Прервать цикл, если достигнут конец страницы
        if (screen_height * i) > scroll_height:
            break








#### INDIVIDUAL FUNCTIONS ####

# GET URL AIRBNB ROOMS
def build_url(location, checkin_date, checkout_date, guests=None, room_types=None, amenities=[]) -> str:
    url = f"https://www.airbnb.com/s/{location}/homes?checkin={checkin_date}&checkout={checkout_date}&enable_auto_translate=false&locale=en&currency=USD"
    if guests:
        url += f"&guests={guests}"
    if room_types:
        url += f"&room_types={room_types}"
    if amenities:
        url += "&amenities=" + "+".join(amenities)
    return url

# FIND URL NEXT PAGE 
def get_url_next_page(driver) -> str:
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    data = nand.find("a", {"aria-label" : "Next"})
    url_href = None
    if data:
        url_href = "https://www.airbnb.com/" + data.get("href")
    return url_href

# CLEAN RATING
def rating_cleen(num: str) -> float | int:
    match1 = re.search(r"\b\d+\.\d+\b", num)
    if match1:
        rating = float(match1.group(0))
    else:
        rating = None

    match2 = re.search(r',\s*(\d+)\s+', num)
    if match2:
        place = int(match2.group(1))
    else:
        place = None
    return rating, place

# FIND TEXT FIXED BT4
# Позже сделать входные параметры в виде словаря для легкой подстройке к изменениям на сайте
def find_data_room(driver, country):
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    quick_sleep(2, 3)


    for el in nand.find_all("div", {"data-testid": "card-container"}):

        # Title room
        title = el.find("div", {"data-testid": "listing-card-title"})
        if title != None:
            title_room = title.text.strip()
            print("title_room:", title_room)

        # Name room
        name = el.find("span", {"data-testid": "listing-card-name"})
        if name != None:
            name_room = name.text.strip()
            print("name_room:", name_room)

        # Subtitle room
        subtitle = el.find("span", {"aria-hidden": "true"})
        if subtitle != None:
            subtitle_room = subtitle.text.strip()
            print("subtitle_room:", subtitle_room)

        # Price night room
        night = el.find("span", {"class": "_1y74zjx"})
        if night != None:
            night_price = str_int(night.text.strip())
            print("night_price:", night_price) # float

        # Price total room
        total = el.find("div", {"class": "_tt122m"})
        if total != None:
            total_price = str_int(total.text.strip())
            print("total_price:", total_price)

        # Rating room - так как нет зацепок, то связывал с текстом который внутри
        word_to_find = "out of 5 average rating"
        rating_el = el.find("span", {"class": "r4a59j5"})
        if rating_el != None:
            if word_to_find in rating_el.text:
                data = rating_el.text.strip()
                rating_place = rating_cleen(data)
                rating = rating_place[0]
                place = rating_place[1]
                print("rating:", rating)
                print("place:", place)

            else:
                rating = None
                place = None
        else:
            rating = None
            place = None

        # Room url and ID room
        room_url = el.find("a", {"class": "l1ovpqvx"})
        if room_url:
            url_href = room_url.get("href")
            url_room = f"https://www.airbnb.com{url_href}"
            print("url_room:", url_room)
            # ID ROOM
            patern = "/rooms/(\d+)"
            match = re.search(patern, url_href)
            if match:
                id = int(match.group(1))
                print("id:", id)

        # Img url room
        data_img = el.find("img", {"class": "itu7ddv"})
        if data_img != None:
            image_url = data_img.get("src") 
            print("image_url:", image_url)

        # Get day and time now
        date_of_update = day_utcnow()

        # Preparing data for the room - Готовим данные 
        room_data = {"id": id, "title_room": title_room, "name_room": name_room, "subtitle_room": subtitle_room,\
                        "night_price": night_price, "total_price": total_price, "rating": rating,\
                        "place": place, "url_room": url_room, "image_url": image_url, "country": country,\
                        "date_of_update": date_of_update }
        


        # Обновляем или добавляем данные
        data_room = asyncio.run(get_rooms_by_id(id))
        if data_room is not None:
            asyncio.run(update_rooms(id, room_data))
            print()
            print(f"Update Room {id} !!!!!!")
            print()
        else:
            asyncio.run(adding_rooms(room_data))
            print()
            print(f"ADD Room {id} !!!!!!")
            print()





        print()

    return






























#quick_sleep(1000, 2000)

# if __name__ == "__main__":
#     restore_db()

# url = "https://www.airbnb.com/s/Bali--Indonesia/homes?adults=1&place_id=ChIJoQ8Q6NNB0S0RkOYkS7EPkSQ&refinement_paths%5B%5D=%2Fhomes"
# get_url(url)


# quick_sleep(3, 4)
# res = find_url("a", "aria-label", "Next")
# print(res)


# while True:
#     res = find_url_soup("a", "aria-label", "Next")
#     if res != None:
#         print(res)
#         break

# Так наверное слишком жестко
# while True:
#     res = find_url_soup(soup, "a", "aria-label", "Next")
#     if res != None:
#         print(res)
#         break

# Получение селениумом url
# page = driver.get(url)

# # Получение исходного кода страницы
# html = driver.page_source
# # Создание объекта BeautifulSoup для парсинга HTML
# soup = BeautifulSoup(html, 'lxml')