from worker_db import get_rooms_by_id, update_rooms, adding_rooms, update_position, get_position, adding_position
from parser_sys import quick_sleep, str_int, day_utcnow, unformat_date, str_inter
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
    print("info: Building a url")
    return url

# FIND URL NEXT PAGE 
def get_url_next_page(driver) -> str:
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    data = nand.find("a", {"aria-label" : "Next"})
    url_href = None
    if data:
        url_href = "https://www.airbnb.com/" + data.get("href")
        print("info: Get url next page")
    return url_href

# CLEAN RATING
def rating_clean(num: str) -> float | int:
    match1 = re.search(r"\b\d+(?:\.\d+)?\b", num)
    if match1:
        rating = float(match1.group(0))
    else:
        rating = 0.0

    match2 = re.search(r"\b(\d+)\s+reviews\b", num)
    if match2:
        reviews = int(match2.group(1))
    else:
        reviews = 0

    return rating, reviews






# FIND TEXT LIST FIXED BT4  -  Сбор со страниц поиска id и url
# Позже сделать входные параметры в виде словаря для легкой подстройки к изменениям на сайте
def find_data_room(driver, country, time_correction, price_min, price_max):
    data_id = []
    print("\ninfo: Getting data (id, url) of objects in the search")
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    quick_sleep(2, 3)


    for el in nand.find_all("div", {"data-testid": "card-container"}):

        if el is None:
            print("Error: No data found on the html url")
            return
        
        print("---------")

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
                print("Error: Ошибка поиска ID")
        else:
            print("Error: Ошибка поиска URl")


        # Get day and time now
        list_date_update = day_utcnow(time_correction)

        # Preparing data for the room - Готовим данные 
        room_data = {"id": id, "url_room": url_room, "location": country, "list_date_update": list_date_update}
        

        # Добавление словаря с текущими id и url_room в список
        data_frame = {"id": id, "url_room": url_room}
        data_id.append(data_frame)


        # Обновляем или добавляем данные
        data_room = asyncio.run(get_rooms_by_id(id))

        # Update data to room, if is outdated
        if data_room is not None:

            # Update data list
            asyncio.run(update_rooms(id, room_data))
            print(f"info: Update {id} and url to the database")
        else:
            # Adding data room
            asyncio.run(adding_rooms(room_data))
            print(f"info: Added {id} and url to the database")


        # price_min, price_max
        data_position = asyncio.run(get_position(1))
        min = str_inter(price_min)
        max = str_inter(price_max)

        if data_position is not None:
            price_data = {"date": list_date_update, "price_min": min, "price_max": max}
            asyncio.run(update_position(1, price_data))
            print(f"info: Update min - max to the database")
        else:
            price_data = {"id": 1, "date": list_date_update, "price_min": min, "price_max": max}
            asyncio.run(adding_position(price_data))
            print(f"info: Added min - max to the database")




    return data_id















# FIND TEXT FIXED OBJECT BT4  -  Сбор и сохранение данных на странице заведения
# Позже сделать входные параметры в виде словаря для легкой подстройки к изменениям на сайте
def find_data_object(driver, id, url_room, location, time_correction, currency):#, country, time_correction):
    print("-------------")
    print("info: Get data at url object")
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    #quick_sleep(2, 3)

    el = nand.find("body", {"class": "with-new-header"})

    if el is None:
        print("Error: is ...")
        return
    
    print()

    # Title room
    title = el.find("h1", {"elementtiming": "LCP-target"})
    if title != None:
        title_room = title.text.strip()
        print("title_room:", title_room)
    else:
        title_room = ""
        print(title_room)
        
    # Name room
    name = el.find("h2", {"elementtiming": "LCP-target"})
    if name != None:
        name_room = name.text.strip()
        print("name_room:", name_room)
    else:
        name_room = ""
        print(name_room)

    # Night room
    night = el.find("span", {"class": "_1y74zjx"})
    if night != None:
        night_price = str_int(night.text.strip())
        print("night_price:", night_price)
    else:
        night_price = 0
        print("There are no places, change the date") # Можно попробовать автоматически поменять дату снова и снова

    if night_price:
        month_price = night_price * 30 # 30 дней
        print("month_price:", month_price)
    else:
        month_price = 0
        print("There are no places, change the date") # Можно попробовать автоматически поменять дату снова и снова



    # Гости, кровати, басейны, кол спалень
    any_list = el.find("ol", {"class": "lgx66tx"})
    guest = bedroom = bed = bath = 0
    if any_list != None:
        text_list = any_list.text.strip()
        text_list = text_list.replace(" ·  · ", " | ")
        list_of_elements = text_list.split(" | ")


        for n in list_of_elements:
            if "guests" in n:
                guest = str_inter(n)
                print("guest:", guest)
            elif "droom" in n:
                bedroom = str_inter(n) 
                print("bedroom:", bedroom) 
            elif "bed" in n:
                bed = str_inter(n)
                print("bed:", bed) 
            elif "bath" in n:
                bath = str_int(n) # float
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


    rating = reviews = 0
    # Rating room no Guest favorite
    if guest_favorite == False:
        rating_data_b = el.find("div", {"data-section-id": "REVIEWS_DEFAULT"})
        if rating_data_b != None:
            rating_data_a = rating_data_b.find("span", {"aria-hidden": "true"})
            if rating_data_a != None:
                rating_no_gf = rating_data_a.text.strip()
                rating_data = rating_clean(rating_no_gf)
                rating = rating_data[0]
                reviews = rating_data[1]
                print(f"Rating: {rating}, {reviews}")


    # Rating room Guest Favorite
    if guest_favorite == True:
        rating_data = el.find("div", {"data-testid": "pdp-reviews-highlight-banner-host-rating"})
        if rating_data != None:
            rating = str_int(rating_data.text.strip())

        place_data = el.find("div", {"class": "r16onr0j"})
        if place_data != None:
            reviews = str_inter(place_data.text.strip())

        print(f"Rating: {rating}, {reviews}")




    # url
    print("url:", url_room)






    # # Initialize del_text before the if statement
    # del_text = None  # or an appropriate default value, such as an empty list

    # # ... your existing code ...

    # if amenities_data is not None:
    #     del_text = amenities_data.find_all("del")
    # else:
    #     # Handle the situation when amenities_data is None
    #     print("No amenities data found")

    # # Now you can safely check if del_text is not None because it has been initialized
    # if del_text is not None:
    #     # ... do something with del_text ...
    #     pass




    # Amenities - услуги
    amenities = ""
    amenities_data = el.find("div", {"aria-label": "What this place offers"})
    # Забираю все перечеркнутые элементы del и смотрю что в них - устанавливаю флаги
    if amenities_data is not None:
        del_text =  amenities_data.find_all("del")
    else:
        del_text = None
        print("Error: No amenities data found")

    # not_dryer, not_garage, not_kitchen, not_lockbox, not_safe, not_lockbox  = False, False, False, False, False, False
    not_dryer = not_garage = not_kitchen = not_safe = not_lockbox = dedicated_workspace = not_rooftop \
    = outdoor_dining_area = patio_or_balcony = private_backyard = courtyard_view = garden_view = sea_view = \
    beach_view = private_pool = mountain_view = park_view = river_view = valley_view = ocean_view = \
    pool_view = restaurant = coworking = storage = False

    if del_text is not None:
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

    parking, kitchen, storage, workspace, rooftop, terrace_balcony, view, restaurants = [], [], [], [], [], [], [], []

    # parking
    if "free parking on premises" in amenities.lower():
        parking.append("Free parking on premises")
    if "street parking" in amenities.lower():
        parking.append("Street parking")
    if not_garage == False and "free residential garage on premises" in amenities.lower():
        parking.append("Free residential garage on premises")
    print(', '.join(parking))

    # kitchen 
    if not_kitchen == False and "kitchen" in amenities.lower():  # Кухня
        kitchen.append("kitchen")
    print(', '.join(kitchen))

    # Storage room
    if not_lockbox == False and "lockbox" in amenities.lower(): # Запирающийся ящик
        storage.append("Lockbox")
    if not_safe == False and "safe" in amenities.lower(): # Сейф
        storage.append("Safe")
    if storage == False and "storage" in amenities.lower(): # Место хранения
        storage.append("Storage")
    print(', '.join(storage))

    # coworking
    if dedicated_workspace == False and "dedicated workspace" in amenities.lower(): # Коворкинг
        workspace.append("Dedicated workspace")
    if coworking == False and "coworking" in amenities.lower():
        workspace.append("Coworking")
    print(', '.join(workspace))

    # rooftop
    if not_rooftop == False and "rooftop" in amenities.lower(): # Крыша
        rooftop.append("Rooftop")
    print(', '.join(rooftop))

    # Terrace or balcony
    if outdoor_dining_area == False and "outdoor dining area" in amenities.lower(): # обеденная зона на открытом воздухе
        terrace_balcony.append("Outdoor dining area")
    if patio_or_balcony == False and "balcony" in amenities.lower(): # Балконы
        terrace_balcony.append("Patio or balcony")
    if private_backyard == False and "backyard" in amenities.lower(): # частный задний двор
        terrace_balcony.append("Backyard")
    if private_pool  == False and "private pool" in amenities.lower():
        terrace_balcony.append("Private pool")
    print(', '.join(terrace_balcony))

    # View - вид
    if courtyard_view  == False and "courtyard view" in amenities.lower():
        view.append("Courtyard view")
    if garden_view  == False and "garden view" in amenities.lower():
        view.append("Garden view")
    if sea_view  == False and "sea view" in amenities.lower():
        view.append("Sea view")
    if beach_view  == False and "beach view" in amenities.lower():
        view.append("Beach view")
    if mountain_view == False and "mountain view" in amenities.lower():
        view.append("Mountain view")
    if park_view == False and "park view" in amenities.lower():
        view.append("Park view")
    if river_view == False and "river view" in amenities.lower():
        view.append("River view")
    if valley_view == False and "valley view" in amenities.lower():
        view.append("Valley view")
    if ocean_view == False and "ocean view" in amenities.lower():
        view.append("Ocean view")
    if pool_view == False and "pool view" in amenities.lower():
        view.append("Pool view")
    print(', '.join(view))

    # restaurants
    if restaurant == False and "restaurant" in amenities.lower():
        restaurants.append("Restaurant")
    print(', '.join(restaurants))

    # 
    if not_dryer == False and "dryer" in amenities.lower():  # Сушилка
        print("Dryer")




    # title_room + name_room --> type_house
    if title_room is None:
        title_room = ""

    if name_room is None:
        name_room = ""

    title_house = title_room + " " + name_room
    if "hotel" in title_house.lower():
        type_house = "Hotel"
    elif "guesthouse" in title_house.lower():
        type_house = "Guesthouse"
    elif "house" in title_house.lower():
        type_house = "House"
    elif "villa" in title_house.lower():
        type_house = "Villa"
    elif "townhouse" in title_house.lower():
        type_house = "Townhouse"
    elif "bungalow" in title_house.lower():
        type_house = "Bungalow"
    elif "cottage" in title_house.lower():
        type_house = "Cottage"
    elif "cabin" in title_house.lower():
        type_house = "Cabin"
    elif "barn" in title_house.lower():
        type_house = "Barn"
    elif "home" in title_house.lower():
        type_house = "Home"
    elif "treehouse" in title_house.lower():
        type_house = "Treehouse"
    elif "hut" in title_house.lower():
        type_house = "Hut"
    elif "tent" in title_house.lower():
        type_house = "Tent"
    elif "farmstay" in title_house.lower():
        type_house = "Farmstay"
    elif "farm" in title_house.lower():
        type_house = "Farmstay"
    elif "apartment" in title_house.lower():
        type_house = "Apartment"
    elif "condo" in title_house.lower():
        type_house = "Condo"
    elif "guest" in title_house.lower():
        type_house = "Guesthouse"
    elif "homestay" in title_house.lower():
        type_house = "Homestay"
    elif "place" in title_house.lower():
        type_house = "Place"
    else:
        type_house = "Place"
    print("type_house:", type_house)



    # SQM  - площадь не нашел, но попадалось в тексте иногда опиание площади (15 sqm, 15sqm) м²
    sqm = None
    text_room = el.find("div", {"data-section-id": "DESCRIPTION_DEFAULT"})
    if text_room != None:
        text = text_room.text.strip()
        pattern = r"(\d+)\s*sqm"
        match = re.search(pattern, text)
        if match:
            sqm = match.group(1)
            print(f"Square: {sqm} sqm")






    # Get day and time now
    obj_date_update = day_utcnow(time_correction)

    # Preparing data for the room - Готовим данные 
    parking = (', '.join(parking))
    kitchen = (', '.join(kitchen))
    view = (', '.join(view))
    workspace = (', '.join(workspace))
    rooftop = (', '.join(rooftop))
    terrace_balcony = (', '.join(terrace_balcony))
    restaurants = (', '.join(restaurants))
    storage = (', '.join(storage))


    room_data = {

        # "id": id,
        "title_room": title_room,
        "name_room": name_room,
        "type_house": type_house,
        "night_price": night_price,
        "month_price": month_price,
        "currency": currency,
        "rating": rating,
        "reviews": reviews,
        "guest_favorite": guest_favorite,
        "guest": guest,
        "bedroom": bedroom,
        "bed": bed,
        "bath": bath,
        "parking": parking,
        "kitchen": kitchen,
        "view": view,
        "workspace": workspace,
        "rooftop": rooftop,
        "terrace_balcony": terrace_balcony,
        "restaurants": restaurants,
        "storage": storage,
        "sqm": sqm,
        # "url_room": url_room,
        # "location": location,
        "obj_date_update": obj_date_update,
        "currency" : currency 

                }
       

    # # Обновляем или добавляем данные
    # data_room = asyncio.run(get_rooms_by_id(id))
    # # Update data to object - обновляем данные по id
    # if data_room.obj_date_update is not None:
    # Update data room
    asyncio.run(update_rooms(id, room_data))
    print(f"info: Updated Data  at object {id}")







    return


#
# 1. Home (House, Townhouse, Villa, Bungalow, Cottage, Cabin, Entire Cabin, Barn, Home)
# 2. Alternative Status (Treehouse, Hut, Tent, Farmstay, Farm Stay)
# 3. Apartment (Apartment, Entire Condo, Guest Suite)
# 4. Hospitality (Hotel, Guesthouse, Homestay)
# 5. Miscellaneous (Place) is a general term for any type of accommodation, unless a specific category is specified.
#

# id
# title_room
# name_room
# type_house
# night_price
# month_price
# currency
# rating
# reviews
# guest_favorite
# guest
# bedroom
# bed
# bath
# parking
# kitchen
# view
# workspace
# rooftop
# terrace_balcony
# restaurants
# storage
# sqm

        # Update data to room, if is outdated
        # if data_room is not None:
            # # Get day -> str and time -> float now in format
            # format_date_now = unformat_date(list_date_update)
            # format_day_now = format_date_now[0]
            # format_time_now = format_date_now[1]
            # # Get in DB room day -> str and time -> float now in format
            # date_room_db = data_room.list_date_update
            # format_date_db = unformat_date(date_room_db)
            # format_day_db = format_date_db[0]
            # format_time_db = format_date_db[1]

            #if format_day_now != format_day_db or (format_day_now == format_day_db and (format_time_now - format_time_db) >= 1.00):
