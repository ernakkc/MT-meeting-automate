import datetime
import configparser
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os

class AutoEnter:
    def __init__(self, link):
        self.link = link
        self.enterTimes = []
        self.exitTimes = []
        self.driver = None
        self.isEntered = False
        self.nameSurname = ""
        self.tryNow = False
        
    def readConfig(self):
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='utf-8')
        
        name = config['Account']['name']
        surname = config['Account']['surname']
        self.nameSurname = name + " " + surname
        
        enter_times = config['Times']['enter_times'].replace(" ","").split(",")
        exit_times = config['Times']['exit_times'].replace(" ","").split(",")
        
        self.tryNow = bool(config['Settings']["tryNow"])
        
        for i in range(len(enter_times)):
            hour, minute = map(int, enter_times[i].split("."))
            self.enterTimes.append([hour, minute])
        for i in range(len(exit_times)):
            hour, minute = map(int, exit_times[i].split("."))
            self.exitTimes.append([hour, minute])
        return self.enterTimes, self.exitTimes
    
    def setDriver(self):
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
        options.add_argument("--user-data-dir={}".format(os.path.abspath("user_data")))
        prefs = {
            "protocol_handler.excluded_schemes": {
                "msteams": False},
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.media_stream_mic": 1}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(service=service, options=options)
        return self.driver
    
    def enterLesson(self):
        if self.isEntered:
            return

        driver = self.driver
        driver.get(self.link)
        print("[DRIVER] Driver started...")
        sleep(5)
        

        # Continue with browser
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        sleep(20)
        
        # Enter name
        for i in range(20): 
            ActionChains(driver).send_keys(Keys.BACK_SPACE).perform()
            sleep(0.1)
        ActionChains(driver).send_keys(self.nameSurname).perform()
        sleep(1)
        
        # Close camera and mic. popups
        ActionChains(driver).send_keys(Keys.TAB).perform()
        # ActionChains(driver).send_keys(Keys.ENTER).perform() # Close camera
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).send_keys(Keys.ENTER).perform() # Close mic
        sleep(1)
        
        # Join the lesson
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        sleep(1)
        
        self.isEntered = True

    def exitLesson(self):
        if not self.isEntered:
            return
        self.isEntered = False
        
    def main(self):
        print("[PROGRAM] Program started...")
        self.readConfig()
        self.setDriver()
        
        if self.tryNow:
            self.enterLesson()
            self.isEntered = True
        
        
        while True:
            now = datetime.datetime.now()
            if [now.hour, now.minute] in self.enterTimes:
                self.enterLesson()
            if [now.hour, now.minute] in self.exitTimes and self.isEntered:
                self.exitLesson()
            
            
            
link = r"https://teams.microsoft.com/l/meetup-join/19%3ameeting_NTU2ODA0ZDctNDA5NC00NWNiLThkZWItZTNlNjNhM2VlMjU2%40thread.v2/0?context=%7b%22Tid%22%3a%22c3a05a57-b7dc-4c78-b650-eb8f4697aee3%22%2c%22Oid%22%3a%2211b0287c-2d4d-432b-a43f-bc29737078a1%22%7d"
program = AutoEnter(link)
program.main()
