# selenium is used for automate the task on the browser

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys

import os

from pprint import pprint

path = os.path.abspath("ghost/chromedriver2")

# chromeDriverPath = "/mnt/83cd30aa-f100-4cb2-91ba-04d2502c8b70/Projects/python/browser-automation/chromedriver"
chromeDriverPath2 = path
# firefoxDriverPath = "/mnt/83cd30aa-f100-4cb2-91ba-04d2502c8b70/Projects/python/browser-automation"

# set the webdriver
driver = webdriver.Chrome(chromeDriverPath2)
wait = WebDriverWait(driver, 600)

# open a link
driver.get("https://www.imdb.com/")
#wait.until(EC.visibility_of_element_located((By.ID, 'navbar-query')))

# now search something in imdb
searchBox = driver.find_element_by_id("navbar-query")
# wait.until(EC.presence_of_element_located((By.ID, 'search')))

searchBox.send_keys("mission impossible")

searchBox.send_keys(Keys.ENTER)

driver.get(driver.current_url)

dataList = driver.find_element_by_class_name("findList")

finalList = dataList.find_element_by_xpath("//*[@class='findList']")

print(finalList.text)

#pprint(finalList.find_elements_by_xpath("//*[@class='primary_photo']"))
