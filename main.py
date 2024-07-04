import datetime
import configparser
import logging
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.webdriver_tools import actionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Logging configuration
if not os.path.exists('logs'):
    os.makedirs('logs')
    
logging.basicConfig(
    filename=os.path.join('logs', 'automation_log.log'),
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

class AutoEnter:
    def __init__(self):
        self.link = None
        self.enterTimes = []
        self.exitTimes = []
        self.driver = None
        self.isEntered = False
        self.nameSurname = ""
        self.tryNow = False
        
    def readConfig(self):
        try:
            logging.info("Reading configuration file...")
            config = configparser.RawConfigParser()
            config.read('config.ini', encoding='utf-8')
            
            name = config['Account']['name']
            surname = config['Account']['surname']
            self.nameSurname = name + " " + surname
            
            enter_times = config['Times']['enter_times'].replace(" ","").split(",")
            exit_times = config['Times']['exit_times'].replace(" ","").split(",")
            
            self.link = config['Lesson']['link'].replace('"', '')
            
            self.tryNow = config.getboolean('Settings', 'tryNow')
            
            for i in range(len(enter_times)):
                hour, minute = map(int, enter_times[i].split("."))
                self.enterTimes.append([hour, minute])
            for i in range(len(exit_times)):
                hour, minute = map(int, exit_times[i].split("."))
                self.exitTimes.append([hour, minute])
            
            logging.info(f"Configuration loaded: name={self.nameSurname}, enterTimes={self.enterTimes}, exitTimes={self.exitTimes}, tryNow={self.tryNow}")
        except Exception as e:
            logging.error(f"Error reading configuration: {e}")
            raise
        
        return self.enterTimes, self.exitTimes
    
    def setDriver(self):
        logging.info("Setting up the driver...")
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
        
        logging.info("Driver set up completed.")
        
        return self.driver
    
    def enterLesson(self):
        if self.isEntered: return
        
        logging.info("Entering the lesson...")
        
        driver = self.driver
        driver.get(self.link)
        logging.info("Navigated to the link.")
        sleep(5)
        
        # Continue with browser
        actionChains(driver, Keys.TAB)
        actionChains(driver, Keys.ENTER)
        logging.info("Clicked 'Continue with browser' button.")
        sleep(10)
        
        # Enter name
        for i in range(30): 
            ActionChains(driver).send_keys(Keys.BACK_SPACE).perform()
            sleep(0.1)
        ActionChains(driver).send_keys(self.nameSurname).perform()
        logging.info(f"Entered name: {self.nameSurname}")
        sleep(2)
        
        # Close camera and mic. popups
        actionChains(driver, Keys.TAB)
        # actionChains(driver, Keys.ENTER) # Close camera
        actionChains(driver, Keys.TAB)
        actionChains(driver, Keys.TAB)
        actionChains(driver, Keys.TAB)
        actionChains(driver, Keys.ENTER) # Close mic
        logging.info("Closed camera and mic popups.")
        sleep(2)

        # Join the lesson
        actionChains(driver, Keys.TAB)
        actionChains(driver, Keys.TAB)
        actionChains(driver, Keys.ENTER)
        logging.info("Clicked 'Join' button.")
        
        self.isEntered = True

    def exitLesson(self):
        if not self.isEntered: return
        
        logging.info("Exiting the lesson...")
        
        driver = self.driver
        
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL)
        actions.key_down(Keys.SHIFT)
        actions.send_keys('h')
        actions.key_up(Keys.SHIFT)
        actions.key_up(Keys.CONTROL)
        actions.perform()
        logging.info("Pressed Ctrl+Shift+H to leave the meeting.")
        sleep(2)
        
        self.isEntered = False
        
    def main(self):
        logging.info("Program started.")
        self.readConfig()
        self.setDriver()
        
        if self.tryNow:
            logging.info("TryNow option is enabled. Entering the lesson now.")
            self.enterLesson()
            self.isEntered = True

            sleep(10)
            
            self.exitLesson()
            self.isEntered = False
        
        while True:
            now = datetime.datetime.now()
            if [now.hour, now.minute] in self.enterTimes:
                logging.info(f"Current time {now.hour}:{now.minute} matches enter time. Entering the lesson.")
                self.enterLesson()
            if [now.hour, now.minute] in self.exitTimes and self.isEntered:
                logging.info(f"Current time {now.hour}:{now.minute} matches exit time. Exiting the lesson.")
                self.exitLesson()

program = AutoEnter()
program.main()
