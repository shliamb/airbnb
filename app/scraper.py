from options_chrome import profil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
# import pandas as pd
import time
import random
# import re

ua = UserAgent()
service = Service()
options = Options()


# OPTINONS
prof = profil()
url = "https://www.airbnb.com/s/Bali--Indonesia/homes?adults=1&place_id=ChIJoQ8Q6NNB0S0RkOYkS7EPkSQ&refinement_paths%5B%5D=%2Fhomes"

def add_options(options, *args):
    for arg in args:
        options.add_argument(arg)

add_options(options, "--disable-webgl", "--disable-gpu", "--disable-3d-apis", "--enable-virtual-keyboard", 
                    "--mute-audio", "--disable-plugins-discovery", "--profile-directory=Default", "disable-infobars",
                    "start-maximized", "--disable-blink-features=AutomationControlled")

# options.add_argument('--headless=new') # Режим без окна, старый - options.add_argument('--headless=old)
options.add_argument(f"--user-agent={ua.random}")
options.add_argument(f"user-data-dir=./profiles/{prof}/")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
#options.add_argument("--incognito")
#options.add_argument(f"--proxy-server={PROXY}")

driver = webdriver.Chrome(service=service, options=options)
driver.delete_all_cookies()
driver.set_window_size(1200,800)
driver.set_window_position(0,0)

# Получение ответа сервера
status_code = requests.get(url)
print(f"HTTP response code: {status_code}")
print(f"Used profil - {prof}")

page = driver.get(url)

time.sleep(10)

# Получение исходного кода страницы
html = driver.page_source
# Создание объекта BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html, 'lxml')


np = soup.find("a", {"aria-label" : "Next"})
#print(np)
if np:
    href = np.get("href")
    print(href)
else:
    print("Link with aria-label 'Next' not found.")

time.sleep(300000)
driver.close()
driver.quit()