from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver # module containing implementations of browser drivers
from webdriver_manager.chrome import ChromeDriverManager # Chrome driver
from selenium.webdriver.common.by import By # method for locating elements by their attributes

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://e.infogram.com/callaway-county-covid-dashboard-1hzj4o07ldrw4pw?parent_url=https%3A%2F%2Fcallawaycovid19.com%2F&src=embed#async_embed')


assert "Callaway County" in driver.title

callaway = driver.find_elements_by_class_name("__ig-alignCenter")

for text in callaway[8:10]:
    print(text.text)

driver.quit()
