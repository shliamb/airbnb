from options_chrome import profil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import time
import random
# import pandas as pd
# import re

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
####


# QUICK SLEEP - промежуток случайных чисел на входе, между которыми будет случайный период остановки
def quick_sleep(mi: int, ma: int) -> bool:
    print("Please wait...")
    confirm = False
    time.sleep(random.randint(mi, ma))
    confirm = True
    return confirm

# RESPONSE CODE URL - на вход url, на выход код ответа сервера
def response_code(url: str) -> int:
    response = requests.get(url)
    code = response.status_code
    print(f"\nHTTP response code: {code}\n")
    return code

# GOING TO THE SITE AND GET LXML BS4 - на вход url, переходит на сайт BS4
def get_url_lxml_bs4(url: str) -> BeautifulSoup:
    if response_code(url) == 200:
        quick_sleep(1, 2)
        driver.get(url) # page = driver.get(url)
        quick_sleep(1, 2)
        html = driver.page_source
        quick_sleep(1, 2)
        soup = BeautifulSoup(html, 'lxml')
        quick_sleep(1, 2)
        return soup

# FIND URL SOUP 
def find_url_soup(nand, tag, name, value):
        np = nand.find(tag, {name : value})
        quick_sleep(1, 2)
        if np:
            url_href = np.get("href")
            return url_href
        else:
            print("Error")


#quick_sleep(1, 2) # !!!!!! Не знаю почему, но без него не будет работать !!!!!


url = "https://www.airbnb.com/s/Bali--Indonesia/homes?adults=1&place_id=ChIJoQ8Q6NNB0S0RkOYkS7EPkSQ&refinement_paths%5B%5D=%2Fhomes"

quick_sleep(3, 4)

soup = get_url_lxml_bs4(url)

quick_sleep(10, 11)


a = find_url_soup(soup, "a", "aria-label", "Next")
print(a)

quick_sleep(100, 200)

driver.close()
driver.quit()









# Получение селениумом url
# page = driver.get(url)

# # Получение исходного кода страницы
# html = driver.page_source
# # Создание объекта BeautifulSoup для парсинга HTML
# soup = BeautifulSoup(html, 'lxml')