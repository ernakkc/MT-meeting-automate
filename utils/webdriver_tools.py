from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def check_element(driver, type_, path):
    try: 
        if type_ == "xpath":
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, path)))
        elif type_ == "id":
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, path)))
        elif type_ == "class":
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, path)))
        elif type_ == "css":
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, path)))
        return True
    except NoSuchElementException:
        return False

def click(driver, type_, path):
    wait_time = 20
    if type_ == "id":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.ID, path)))
        driver.find_element(By.ID, path).click()
    elif type_ == "class":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CLASS_NAME, path)))
        driver.find_element(By.CLASS_NAME, path).click()
    elif type_ == "xpath":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, path)))
        driver.find_element(By.XPATH, path).click()
    elif type_ == "css":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, path)))
        driver.find_element(By.CSS_SELECTOR, path).click()


def send_keys(driver, type_, path, keys):
    """_summary_

    Args:
        driver (driver): driver
        type_ (search type): xpath, id, class, css
        path (search query): None
        keys (string): what to send
    """
    wait_time = 20
    if type_ == "xpath":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, path)))
        driver.find_element(By.XPATH, path).send_keys(keys)
    elif type_ == "id":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.ID, path)))
        driver.find_element(By.ID, path).send_keys(keys)
    elif type_ == "class":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CLASS_NAME, path)))
        driver.find_element(By.CLASS_NAME, path).send_keys(keys)
    elif type_ == "css":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, path)))
        driver.find_element(By.CSS_SELECTOR, path).send_keys(keys)


def get(driver, link):
    """_summary_

    Args:
        driver (driver): driver
        link (string): link
    """
    driver.get(link)


def get_text(driver, type_, path):
    """_summary_

    Args:
        driver (driver): driver
        type_ (search type): xpath, id, class, css
        path (search query): None
    """
    wait_time = 20
    if type_ == "xpath":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, path)))
        return driver.find_element(By.XPATH, path).text
    elif type_ == "id":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.ID, path)))
        return driver.find_element(By.ID, path).text
    elif type_ == "class":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CLASS_NAME, path)))
        return driver.find_element(By.CLASS_NAME, path).text
    elif type_ == "css":
        WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, path)))
        return driver.find_element(By.CSS_SELECTOR, path).text

def waitElement(driver, type_, path):
    wait_time = 20
    if type_ == "xpath":
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, path)))
    elif type_ == "id":
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.ID, path)))
    elif type_ == "class":
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CLASS_NAME, path)))
    elif type_ == "css":
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, path)))
    
def actionChains(driver, keys):
    ActionChains(driver).send_keys(keys).perform()
    sleep(2)