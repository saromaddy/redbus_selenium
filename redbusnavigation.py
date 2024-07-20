from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import sqlalchemy

driver = webdriver.Chrome()

driver.get('https://www.redbus.in')
driver.maximize_window()
time.sleep(5)


bus_org = driver.find_elements(By.XPATH,"//div[@class = 'rtcCards']")


def apsrtc():
    apsrtc = driver.find_elements(By.XPATH, '//*[@id="Carousel"]/div[1]')
    apsrtc[0].click()
    time.sleep(5)

    vijay_hyd = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div[1]/a')
    vijay_hyd[0].click()
    time.sleep(10)
    return ("successfully opened APSRTC")


# data = {
#     'service_provider':[],
#     'busname':[],
#     'from':[], #mbwrapper has details from and to
#     'to':[], 


# }
