import os
import sys
import time
import json
import random
from time import sleep
from selenium import webdriver
from configparser import ConfigParser
from utils.webdriver_tools import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


link = r"https://teams.live.com/meet/945811452815?p=HcbVocQAwijQt0rGko"

driver =  Service(ChromeDriverManager().install())
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_camera": 1,  # Kamera izni
    "profile.default_content_setting_values.media_stream_mic": 1,     # Mikrofon izni
})
driver = webdriver.Chrome(service=driver, options=options)

driver.get(link)
sleep(4)

print("Started...")

print("1. Butona tıklanıyor")
click(driver, 'xpath', "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/button[2]")
print("1. Butona tıklandı")
sleep(10)

print("İsim Yazılıyor")
for i in range(5):
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(0.2) 
ActionChains(driver).send_keys("Eren").perform()
time.sleep(1)  # Bir saniye bekleme süresi
ActionChains(driver).send_keys(" Akkoç").perform()
time.sleep(1)  # Bir saniye bekleme süresi
print("İsim Yazıldı")
sleep(4)


print("Mic. Butona tıklanıyor")
ActionChains(driver).send_keys(Keys.TAB).perform()
time.sleep(0.2) 
ActionChains(driver).send_keys(Keys.ENTER).perform()
print("Mic. Butona tıklandı")
sleep(4)

print("Kamera Butona tıklanıyor")
ActionChains(driver).send_keys(Keys.RIGHT).perform()
time.sleep(0.2)
ActionChains(driver).send_keys(Keys.ENTER).perform()
print("Kamera Butona tıklandı")
sleep(4)

print("Join Butona tıklanıyor")
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
print("Join Butona tıklandı")
sleep(20) 



