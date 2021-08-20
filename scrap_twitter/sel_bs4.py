import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def checkTwitter():
    url = "https://twitter.com/Paulagat10/status/1424472836178026504"
    WEBDRIVER_PATH = "D:\Software\driver_chrome\chromedriver.exe"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--enable-javascript")
    driver = webdriver.Chrome(WEBDRIVER_PATH, options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(2)
    print(driver.page_source)
    driver.quit()
    

if __name__ == "__main__":
    checkTwitter()
