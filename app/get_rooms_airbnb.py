from scraper import go_url, begin, build_url, end_close, quick_sleep, response_code, find_url, find_text

# DATA FOR SEARCH URL
location = "Bali"
checkin_date = "2024-05-01"
checkout_date = "2024-05-07"
guests = 2
#room_types = "Private room"






# Build URL
url = build_url(location, checkin_date, checkout_date, guests)#, room_types)

# Build Driver Chrome
driver = begin()

# Response code
code = response_code(url)
print(f"\nHTTP response code: {code}\n")

# Go to URL
go_url(driver, url)

# Wait time
quick_sleep(10, 11)

# Find url
data_url = find_url(driver, "a", "aria-label", "Next")
print(data_url)

# Find text
data_text = find_text(driver)
#print(data_text)

# Close Driver Chrome
end_close(driver)
