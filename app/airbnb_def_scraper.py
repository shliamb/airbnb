from worker_db import get_rooms_by_id, update_rooms, adding_rooms
from sys_def_scraper import quick_sleep, str_int, day_utcnow, unformat_date
from bs4 import BeautifulSoup
import asyncio
import re



#### INDIVIDUAL FUNCTIONS BY ROOMS ####

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
# Позже сделать входные параметры в виде словаря для легкой подстройки к изменениям на сайте
def find_data_room(driver, country, time_correction):
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    quick_sleep(2, 3)


    for el in nand.find_all("div", {"data-testid": "card-container"}):

        if el is None:
            print("Error is ...")
            return
        
        # Title room
        title = el.find("div", {"data-testid": "listing-card-title"})
        if title != None:
            title_room = title.text.strip()
            print("title_room:", title_room)
        else:
            title_room = None

        # Name room
        name = el.find("span", {"data-testid": "listing-card-name"})
        if name != None:
            name_room = name.text.strip()
            print("name_room:", name_room)
        else:
            name_room = None

        # Subtitle room
        subtitle = el.find("span", {"aria-hidden": "true"})
        if subtitle != None:
            subtitle_room = subtitle.text.strip()
            print("subtitle_room:", subtitle_room)
        else:
            subtitle_room = None

        # Price night room
        night = el.find("span", {"class": "_1y74zjx"})
        if night != None:
            night_price = str_int(night.text.strip())
            print("night_price:", night_price) # float
        else:
            night_price = None

        # Price total room
        total = el.find("div", {"class": "_tt122m"})
        if total != None:
            total_price = str_int(total.text.strip())
            print("total_price:", total_price)
        else:
            total_price = None

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
            else:
                return # Если нет id, то делать тут не чего..
        else:
            return # Если нет url, то делать тут не чего..

        # Img url room
        data_img = el.find("img", {"class": "itu7ddv"})
        if data_img != None:
            image_url = data_img.get("src") 
            print("image_url:", image_url)
        else:
            image_url = None


        # Get day and time now
        rooms_date_update = day_utcnow(time_correction)

        # Preparing data for the room - Готовим данные 
        room_data = {"id": id, "title_room": title_room, "name_room": name_room, "subtitle_room": subtitle_room,\
                        "night_price": night_price, "total_price": total_price, "rating": rating,\
                        "place": place, "url_room": url_room, "image_url": image_url, "country": country,\
                        "rooms_date_update": rooms_date_update }
        
        # Обновляем или добавляем данные
        data_room = asyncio.run(get_rooms_by_id(id))
        # Update data to room, if is outdated
        if data_room is not None:
            # Get day -> str and time -> float now in format
            format_date_now = unformat_date(rooms_date_update)
            format_day_now = format_date_now[0]
            format_time_now = format_date_now[1]
            # Get in DB room day -> str and time -> float now in format
            date_room_db = data_room.rooms_date_update
            format_date_db = unformat_date(date_room_db)
            format_day_db = format_date_db[0]
            format_time_db = format_date_db[1]

            if format_day_now != format_day_db or (format_day_now == format_day_db and (format_time_now - format_time_db) >= 1.00):

                # Update data room
                asyncio.run(update_rooms(id, room_data))
                print(f"\nUpdate Room {id}\n")
            else:
                print(f"\nThe record {id} is fresh, there is no need to update it\n")
        else:
            # Adding data room
            asyncio.run(adding_rooms(room_data))
            print(f"\nADD Room {id}\n")

    return