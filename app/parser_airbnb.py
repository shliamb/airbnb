from worker_db import get_rooms_by_id, update_rooms, adding_rooms
from parser_sys import quick_sleep, str_int, day_utcnow, unformat_date
from bs4 import BeautifulSoup
import asyncio
import re



#### INDIVIDUAL FUNCTIONS BY ROOMS ####

# GET URL AIRBNB ROOMS amenities=[]
def build_url(location, checkin_date, checkout_date, guests=None, currency=None, price_min=None, price_max=None, room_types=None) -> str:
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

# FIND TEXT LIST FIXED BT4
# Позже сделать входные параметры в виде словаря для легкой подстройки к изменениям на сайте
def find_data_room(driver, country, time_correction, currency):
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    quick_sleep(2, 3)


    for el in nand.find_all("div", {"data-testid": "card-container"}):

        if el is None:
            print("Error is ...")
            return
        
        # # Title room
        # title = el.find("div", {"data-testid": "listing-card-title"})
        # if title != None:
        #     title_room = title.text.strip()
        #     print("title_room:", title_room)
        # else:
        #     title_room = None

        # # Name room
        # name = el.find("span", {"data-testid": "listing-card-name"})
        # if name != None:
        #     name_room = name.text.strip()
        #     print("name_room:", name_room)
        # else:
        #     name_room = None

        # # Subtitle room
        # subtitle = el.find("span", {"aria-hidden": "true"})
        # if subtitle != None:
        #     subtitle_room = subtitle.text.strip()
        #     print("subtitle_room:", subtitle_room)
        # else:
        #     subtitle_room = None

        # # Price night room
        # night = el.find("span", {"class": "_1y74zjx"})
        # if night != None:
        #     night_price = str_int(night.text.strip())
        #     print("night_price:", night_price) # float
        # else:
        #     night_price = 0

        # # Price total room
        # total = el.find("div", {"class": "_tt122m"})
        # if total != None:
        #     total_price = str_int(total.text.strip())
        #     print("total_price:", total_price)
        # else:
        #     total_price = 0

        # # Rating room - так как нет зацепок, то связывал с текстом который внутри
        # word_to_find = "out of 5 average rating"
        # rating_el = el.find("span", {"class": "r4a59j5"})
        # if rating_el != None:
        #     if word_to_find in rating_el.text:
        #         data = rating_el.text.strip()
        #         rating_place = rating_cleen(data)
        #         rating = rating_place[0]
        #         place = rating_place[1]
        #         print("rating:", rating)
        #         print("reviews:", place)

        #     else:
        #         rating = None
        #         place = None
        # else:
        #     rating = None
        #     place = None

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
                print("Ошибка поиска ID")
        else:
            print("Ошибка поиска URl")

        # # Img url room
        # data_img = el.find("img", {"class": "itu7ddv"})
        # if data_img != None:
        #     image_url = data_img.get("src") 
        #     print("image_url:", image_url)
        # else:
        #     image_url = None


        # Get day and time now
        rooms_date_update = day_utcnow(time_correction)

        # Preparing data for the room - Готовим данные 
        room_data = {"id": id, "url_room": url_room, "country": country, "rooms_date_update": rooms_date_update, "currency" : currency }
        
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


# FIND TEXT FIXED OBJECT BT4
# Позже сделать входные параметры в виде словаря для легкой подстройки к изменениям на сайте
def find_data_object(driver, url):#, country, time_correction):
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    #quick_sleep(2, 3)

    el = nand.find("body", {"class": "with-new-header"})

    if el is None:
        print("Error is ...")
        return
    
    print()

    # Title room
    title = el.find("h1", {"elementtiming": "LCP-target"})
    if title != None:
        title_room = title.text.strip()
        print("title_room:", title_room)
    else:
        title_room = None
        print(title_room)
        
    # Name room
    name = el.find("h2", {"elementtiming": "LCP-target"})
    if name != None:
        name_room = name.text.strip()
        print("name_room:", name_room)
    else:
        name_room = None
        print(name_room)

    # Night room
    night = el.find("span", {"class": "_1y74zjx"})
    if night != None:
        night_price = str_int(night.text.strip())
        print("night_price:", night_price)
    else:
        night_price = None
        print("There are no places, change the date") # Можно попробовать автоматически поменять дату снова и снова

    if night_price:
        month_price = night_price * 30 # 30 дней
        print("month_price:", month_price)
    else:
        print("There are no places, change the date") # Можно попробовать автоматически поменять дату снова и снова



    # Гости, кровати, басейны, кол спалень
    any_list = el.find("ol", {"class": "lgx66tx"})
    if any_list != None:
        text_list = any_list.text.strip()
        text_list = text_list.replace(" ·  · ", " | ")
        list_of_elements = text_list.split(" | ")

        for n in list_of_elements:
            if "guests" in n:
                guest = n
                print("guest:", guest)
            elif "droom" in n:
                bedroom = n 
                print("bedroom:", bedroom) 
            elif "bed" in n:
                bed = n
                print("bed:", bed) 
            elif "bath" in n:
                bath = n 
                print("bath:", bath)  # 1.5 baths бывает и так, хз.. полторы басейна.. прикол
    else:
        text_list = None
        print(text_list)





    # is Guest favorite
    guest_favorite = el.text.strip()
    # for n in ggg:
    if "Guest favorite" in guest_favorite:
        guest_favorite = True
        print("Guest favorite: True")
    else:
        guest_favorite = False

    # Rating room no Guest favorite
    if guest_favorite == False:
        rating_data_b = el.find("div", {"data-section-id": "REVIEWS_DEFAULT"})
        rating_data_a = rating_data_b.find("span", {"aria-hidden": "true"})
        if rating_data_a != None:
            rating_no_gf = rating_data_a.text.strip()
            print(f"Rating: {rating_no_gf}")


    # Rating room Guest Favorite
    if guest_favorite == True:
        rating_data = el.find("div", {"data-testid": "pdp-reviews-highlight-banner-host-rating"})
        if rating_data != None:
            rating = str_int(rating_data.text.strip())

        place_data = el.find("div", {"class": "r16onr0j"})
        if place_data != None:
            place = str_int(place_data.text.strip())

        print(f"Rating: {rating} · {place} reviews")



    # url
    print("url:", url)


    # Amenities - услуги
    amenities_data = el.find("div", {"aria-label": "What this place offers"})
    # Забираю все перечеркнутые элементы del и смотрю что в них - устанавливаю флаги
    del_text =  amenities_data.find_all("del")
    # not_dryer, not_garage, not_kitchen, not_lockbox, not_safe, not_lockbox  = False, False, False, False, False, False
    not_dryer = not_garage = not_kitchen = not_lockbox = not_safe = not_lockbox = dedicated_workspace = not_rooftop \
    = outdoor_dining_area = patio_or_balcony = private_backyard = courtyard_view = garden_view = sea_view = \
    beach_view = backyard = private_pool = mountain_view = park_view = river_view = valley_view = ocean_view = \
    pool_view = restaurant = coworking = storage = False

    for n_del_text in del_text:
        if n_del_text != None:
            del_text_clear = n_del_text.text.strip()
            if "dryer" in del_text_clear.lower():
                not_dryer = True
            if "residential garage" in del_text_clear.lower():
                not_garage = True
            if "kitchen" in del_text_clear.lower():
                not_kitchen = True
            if "lockbox" in del_text_clear.lower():
                not_lockbox = True
            if "safe" in del_text_clear.lower():
                not_safe = True
            if "lockbox" in del_text_clear.lower():
                not_lockbox = True
            if "dedicated workspace" in del_text_clear.lower():
                dedicated_workspace = True
            if "rooftop" in del_text_clear.lower():
                not_rooftop = True
            if "outdoor dining area" in del_text_clear.lower():
                outdoor_dining_area = True
            if "balcony" in del_text_clear.lower():  # private patio or 
                patio_or_balcony = True
            if "private backyard" in del_text_clear.lower():
                private_backyard = True
            if "courtyard view" in del_text_clear.lower():
                courtyard_view = True
            if "garden view" in del_text_clear.lower():
                garden_view = True
            if "sea view" in del_text_clear.lower():
                sea_view = True
            if "beach view" in del_text_clear.lower():
                beach_view = True
            if "backyard" in del_text_clear.lower():
                backyard = True
            if "private pool" in del_text_clear.lower():
                private_pool = True
            if "mountain view" in del_text_clear.lower():
                mountain_view = True
            if "park view" in del_text_clear.lower():
                park_view = True
            if "river view" in del_text_clear.lower():
                river_view = True
            if "valley view" in del_text_clear.lower():
                valley_view = True
            if "ocean view" in del_text_clear.lower():
                ocean_view = True
            if "pool view" in del_text_clear.lower():
                pool_view = True
            if "restaurant" in del_text_clear.lower():
                restaurant = True
            if "coworking" in del_text_clear.lower():
                coworking = True
            if "storage" in del_text_clear.lower():
                storage = True


    # Приверяю, есть ли в тексте ключевые слова
    if amenities_data != None:
        amenities = amenities_data.text.strip()

    if "free parking on premises" in amenities.lower():
        print("Free parking on premises")
    if "street parking" in amenities.lower():
        print("Free street parking")
    if not_garage == False and "free residential garage on premises" in amenities.lower():
        print("Free residential garage on premises")
    if not_dryer == False and "dryer" in amenities.lower():
        print("Dryer")
    if not_kitchen == False and "kitchen" in amenities.lower():
        print("Kitchen")
    if not_lockbox == False and "lockbox" in amenities.lower():
        print("Lockbox")
    if not_safe == False and "safe" in amenities.lower():
        print("Safe")
    if not_lockbox == False and "Lockbox" in amenities.lower():
        print("Lockbox")
    if dedicated_workspace == False and "dedicated workspace" in amenities.lower():
        print("Dedicated workspace")
    if not_rooftop == False and "not rooftop" in amenities.lower():
        print("Not rooftop")
    if outdoor_dining_area == False and "outdoor dining area" in amenities.lower():
        print("Outdoor dining area")
    if patio_or_balcony == False and "balcony" in amenities.lower():
        print("Patio or balcony")
    if private_backyard == False and "private backyard" in amenities.lower():
        print("Private backyard")
    if courtyard_view  == False and "courtyard view" in amenities.lower():
        print("Courtyard view")
    if garden_view  == False and "garden view" in amenities.lower():
        print("Garden view")
    if sea_view  == False and "sea view" in amenities.lower():
        print("Sea view")
    if beach_view  == False and "beach view" in amenities.lower():
        print("Beach view")
    if backyard  == False and "backyard" in amenities.lower():
        print("Backyard")
    if private_pool  == False and "private pool" in amenities.lower():
        print("Private pool")
    if mountain_view == False and "mountain view" in amenities.lower():
        print("Mountain view")
    if park_view == False and "park view" in amenities.lower():
        print("Park view")
    if river_view == False and "river view" in amenities.lower():
        print("River view")
    if valley_view == False and "valley view" in amenities.lower():
        print("Valley view")
    if ocean_view == False and "ocean view" in amenities.lower():
        print("Ocean view")
    if pool_view == False and "pool view" in amenities.lower():
        print("Pool view")
    if restaurant == False and "restaurant" in amenities.lower():
        print("Restaurant")
    if coworking == False and "coworking" in amenities.lower():
        print("Coworking")
    if storage == False and "storage" in amenities.lower():
        print("Storage")



















    # sqm площадь не нашел, в одном месте видел в виде текста (15 sqm, 15sqm) м²
    print("sqm:", "None")

    return



