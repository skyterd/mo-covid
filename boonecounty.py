from bs4 import BeautifulSoup
from selenium import webdriver # module containing implementations of browser drivers
from webdriver_manager.chrome import ChromeDriverManager # Chrome driver
from selenium.webdriver.common.by import By # method for locating elements by their attributes
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://gocolumbiamo.maps.arcgis.com/apps/opsdashboard/index.html#/4e1e87a1755c4b309eb94c0edc2b1446')
# need to delay code for the page to load properly
time.sleep(10)

assert "(Mobile)" in driver.title
# its finding the table and identifying as a list but not printing list
# boone = driver.find_elements_by_class_name("flex-horizontal feature-list-item ember-view")

# line = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/margin-container/full-container/div[2]/margin-container/full-container/div/div[2]/nav')
#
# print(boone)
#
driver.quit()
