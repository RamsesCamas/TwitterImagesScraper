from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from getpass import getpass
from time import sleep
from selenium.common.exceptions import NoSuchElementException

def run():
    WEBDRIVER_PATH = "D:\Software\driver_chrome\chromedriver.exe"
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    option.add_argument("--enable-javascript")
    URL_TEST = 'https://twitter.com/Paulagat10/status/1424472836178026504'

    driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH,options=option)
    driver.get(URL_TEST)

    print(driver.page_source)

if __name__ == "__main__":
    run()



#sign_in = driver.find_element_by_class_name('css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
#sign_in.click()

#username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
#username.send_keys('193230@ids.upchiapas.edu.mx')


