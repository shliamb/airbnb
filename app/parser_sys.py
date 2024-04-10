from options_chrome import profil
from datetime import datetime, timezone, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# import asyncio
import requests
import time
import random
import sys
import re
# import pandas as pd


#### SYSTEM FUNCTIONS ####

# Begin work, options driver, return driver
def begin():
    ua = UserAgent() # ua = UserAgent(browsers=['edge', 'chrome'])  ua = UserAgent(os='linux') ua = UserAgent(min_version=120.0)  ua = UserAgent(platforms='mobile')  
    options = Options()
    # OPTINONS DRIVER CHRONE SELENIUM
    prof = profil()
    # print("\nOPTIONS DRIVER CHROME:")
    ####
    def add_options(options, *args):
        for arg in args:
            options.add_argument(arg)
            #print(arg)
    ####
    add_options(options, "--disable-webgl", "--disable-gpu", "--disable-3d-apis", "--enable-virtual-keyboard", "--mute-audio", "--disable-plugins-discovery", "--profile-directory=Default", "disable-infobars", "start-maximized", "--disable-blink-features=AutomationControlled", f"--user-agent={ua.random}", f"user-data-dir=./profiles/{prof}", "--headless=new") # , "--incognito", f"--proxy-server={PROXY}", "--headless=new")
    ####
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--no-sandbox")  # Отключение режима песочницы (sandbox)
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    # driver.delete_all_cookies()
    driver.set_window_size(1200,800)
    driver.set_window_position(0,0)
    print("info: Open driver Chrome")
    return driver
####

# QUICK SLEEP - промежуток случайных чисел на входе, между которыми будет случайный период остановки
def quick_sleep(mi: int, ma: int) -> bool:
    confirm = False
    num = random.randint(mi, ma)
    print(f"info: wait {num} seconds")
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
    print("info: Get response code url")
    return code or None

# GOING TO THE SITE
def go_url(driver, url: str) -> bool:
    confirmation = False
    code = response_code(url)
    if code == 200:
        driver.get(url)
        print("info: Going to the url")
        confirmation = True
    else:
        confirmation = False
        print(f"Error: Server back code response - {code}")
    return confirmation

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
    
# GET INTER at STR - Из строки получаем только целое число
def str_inter(num: str) -> int:
    pattern = r"(\d{1,3}(?:,\d{3})*(?:\.\d+)?)"
    num = re.sub(r"[^\d.,]", "", num)
    str_num = re.search(pattern, num)
    if not str_num:
        return None
    float_num_str = str_num.group(1).replace(',', '')
    try:
        float_num = int(float_num_str)
        return float_num
    except ValueError:
        return None

# GET DAY AND TIME
def day_utcnow(time_correction: str) -> datetime:
    utc_zone = timezone.utc
    a = datetime.now(timezone.utc).replace(tzinfo=utc_zone)
    a = a + timedelta(hours=time_correction)
    day_str = a.strftime("%Y-%m-%d %H:%M:%S")
    day = datetime.strptime(day_str, '%Y-%m-%d %H:%M:%S')
    print("info: Getting the day and time from the server")
    return day or None

# UNFORMAT TIME
def unformat_date(date) -> str | int:
    day_now = str(date.strftime("%Y-%m-%d"))
    time_now = float(date.strftime("%H.%M"))
    return day_now, time_now

# FIND SOME URL BT4
def find_url(driver, tag: str, name: str, value: str) -> str:
    html = driver.page_source
    nand = BeautifulSoup(html, 'lxml')
    data = nand.find(tag, {name : value})
    url_href = None
    if data:
        url_href = data.get("href")
    return url_href or None

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
            print("info: Scrolling is comlite")
            break

# CLOSE DRIVER CHROME
def end_close(driver):
    driver.close()
    driver.quit()
    print("info: Close driver Chrome")
    return



