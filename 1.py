from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

def browser_function():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True) #Essential for not closing the browser
    chr_driver = webdriver.Chrome(options=chr_options)
    chr_driver.get("https://www.redbus.in")
    try:
        element = chr_driver.find_element(By.CLASS_NAME,"rtcName")
        print("Element Found", element)

    except:
        print ("Error")

browser_function()