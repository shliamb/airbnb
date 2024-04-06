from sys_def_scraper import ( go_url, begin, end_close, quick_sleep, response_code, scroll)
from airbnb_def_scraper import ( build_url, quick_sleep, find_data_room, get_url_next_page)



#### GETTING DATA FOR ROOM AT ITS ID IN DB ####
# Build 1rst URL to citi



url = build_url(location, checkin_date, checkout_date, guests)
# Build Driver Chrome
driver = begin()
i = 1
while True:
    # Response code
    code = response_code(url)
    if code != 200:
        print(f"\nHTTP response code: {code}\n")
        # Close Driver Chrome
        end_close(driver)
        break
    # Go to URL
    go_url(driver, url)
    # Wait time
    quick_sleep(5, 6)
    # Scroll page
    scroll(driver)
    # Find data room and save to DB
    data_room = find_data_room(driver, location, time_correction)
    quick_sleep(1, 2)
    # Find url next page
    url = get_url_next_page(driver)
    if url == None:
        # Close Driver Chrome
        end_close(driver)
        break
    i += 1
    quick_sleep(1, 2)




