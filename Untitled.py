from bs4 import BeautifulSoup

from selenium import webdriver # module containing implementations of browser drivers
from webdriver_manager.chrome import ChromeDriverManager # Chrome driver
from selenium.webdriver.support import expected_conditions as EC # method for writing code that waits until conditions are met
from selenium.webdriver.support.ui import WebDriverWait # method for writing code that implements implicit or explicit waits
from selenium.webdriver.common.by import By # method for locating elements by their attributes
from selenium.webdriver import ActionChains

import pandas as pd
from datetime import datetime
import numpy as np

import matplotlib.pyplot as plt

# Initialize Chrome browser and launch the dashboard in Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.arcgis.com/apps/MapSeries/index.html?appid=478880b83d5e4d35b646d80fe6f2c2f6'
driver.get(url)

total_cases = driver.find_element_by_class_name("entryLbl")

# delay = 10
# try:
#     element_present = EC.presence_of_element_located((By.ID, 'nav-bar'))
#     WebDriverWait(driver, delay).until(element_present)
# except TimeoutException:
#     print('Timed out waiting for page to load')
#
# # Click on history of tests performed
# element1 = driver.find_element_by_id("nav-bar")
# ActionChains(driver).click(element1).perform()
