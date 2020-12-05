from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get('https://colecounty.org/794/COVID-19')

content = source.content

soup = BeautifulSoup(content, 'lxml')

table = soup.find('table')

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in tr]
    # print(row)

total_cases = table_rows[1].find('td').find_all('span')[-1].text
print(total_cases)

total_deaths = table_rows[1].find_all('td')[-1].find_all('span')[-1].text
print(total_deaths)

ltc_cases = table_rows[3].find('td').find_all('span')[-1].text
print(ltc_cases)

ltc_deaths = table_rows[-1].find_all('td')[-1].find_all('span')[-1].text
print(ltc_deaths)
