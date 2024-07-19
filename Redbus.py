from selenium import webdriver
#required for controlling browser By and Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#required for headless part 1
from selenium.webdriver.chrome.options import Options
#New paradigm for path - required
from selenium.webdriver.chrome.service import Service

s = Service('/usr/local/bin/chromedriver')

#set some selenium chrome options - optionsal
#these options set your driver to run headless or not

chromeOptions = Options()
chromeOptions.add_argument("--start-maximized")


driver = webdriver.Chrome(service=s, options=chromeOptions)
# driver.get("https://www.redbus.in")

# def initialize_browser():
#     driver.get("https://www.redbus.in")
#     print("starting_Driver")
#     content = driver.find_element(By.CLASS_NAME, "headerText")
#     content.click()
#     # content.send_keys(Keys.RETURN)
#     while (True):
#         pass

# initialize_browser()


try:
    element = driver.find_element(By.CLASS_NAME, "rtcName")
    print("Element found:", element)
except:
    print("Error:")
    while (True):
        pass

driver.quit()