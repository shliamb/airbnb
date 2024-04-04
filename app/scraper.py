from options_chrome import profil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import time
import random
import sys
# import pandas as pd
# import re

def begin():
    ua = UserAgent(browsers=['edge', 'chrome']) # ua = UserAgent(browsers=['edge', 'chrome'])  ua = UserAgent(os='linux') ua = UserAgent(min_version=120.0)  ua = UserAgent(platforms='mobile')  
    service = Service()
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
    for _ in range(num):
        print(".", end='', flush=True)
        time.sleep(1)
    print("\n")
    confirm = True
    return confirm

# RESPONSE CODE URL - на вход url, на выход код ответа сервера
def response_code(url: str) -> int:
    response = requests.get(url)
    code = response.status_code
    return code

# GOING TO THE SITE
def go_url(driver, url: str) -> str:
    if response_code(url) == 200:
        driver.get(url)
        return

# FIND URL BT4 
def find_url(driver, tag: str, name: str, value: str) -> str:
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    data = nand.find(tag, {name : value})
    url_href = None
    if data:
        url_href = data.get("href")
    return url_href

# FIND TEXT BT4
def find_text(driver):
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    quick_sleep(2, 3)
    a = ""
    for el in nand.find_all("div", {"class": "dir-ltr"}):
        prop_type = el.find("div", {"data-testid": "listing-card-title"})
        if prop_type != None:# and prop_type != "":
            if a != prop_type.text.strip():
                a = prop_type.text.strip()
                print(a)
    return

# GET URL AIRBNB
def build_url(location, checkin_date, checkout_date, guests=None, room_types=None, amenities=[]) -> str:
    url = f"https://www.airbnb.com/s/{location}/homes?checkin={checkin_date}&checkout={checkout_date}"
    if guests:
        url += f"&guests={guests}"
    if room_types:
        url += f"&room_types={room_types}"
    if amenities:
        url += "&amenities=" + "+".join(amenities)
    return url

# CLOSE DRIVER CHROME
def end_close(driver):
    driver.close()
    driver.quit()





























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