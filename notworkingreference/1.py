from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import sqlalchemy
import json

def work():
    driver = webdriver.Chrome()

    driver.get('https://www.redbus.in/')
    driver.maximize_window()
    time.sleep(5)

    apsrtc = driver.find_elements(By.XPATH, "/html/body/section/div[2]/main/div[3]/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
    apsrtc[0].click()
    time.sleep(5)

    driver.quit()

work()
work()