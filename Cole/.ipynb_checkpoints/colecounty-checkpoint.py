from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from datetime import datetime
import openpyxl

source = requests.get('https://colecounty.org/794/COVID-19')

content = source.content

soup = BeautifulSoup(content, 'lxml')

table = soup.find('table')

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in tr]
    # print(row)

# print('Total Cases')
total_cases = table_rows[1].find('td').find_all('span')[-2].text
# print(total_cases)

total_cases_added = table_rows[1].find('td').find_all('span')[-1].text
# print(total_cases_added)

# print('Total Deaths')
total_deaths = table_rows[1].find_all('td')[-1].find_all('span')[3].text
# print(total_deaths)

total_deaths_added = table_rows[1].find_all('td')[-1].find_all('span')[-1].text
# print(total_deaths_added)

# print('LTC Cases')
ltc_cases = table_rows[3].find('td').find_all('span')[3].text
# print(ltc_cases)

ltc_cases_added = table_rows[3].find('td').find_all('span')[-1].text
# print(ltc_cases_added)

# print('LTC Deaths')
ltc_deaths = table_rows[-1].find_all('td')[-1].find_all('span')[4].text
# print(ltc_deaths)

ltc_deaths_added = table_rows[-1].find_all('td')[-1].find_all('span')[-1].text
# print(ltc_deaths_added)

thisdict = {
    'Total Cases': total_cases,
    'Cases Added': total_cases_added,
    'Deaths': total_deaths,
    'Deaths Added': total_deaths_added,
    'LTC Cases': ltc_cases,
    'LTC Cases Added': ltc_cases_added,
    'LTC Deaths': ltc_deaths,
    'LTC Deaths Added': ltc_deaths_added
}

df = pd.DataFrame(list(thisdict.items()), columns = ['Cole County','--',])
df.insert(0, 'Timestamp', datetime.now().replace(microsecond=0))
print(df)

df.to_csv('mo-covid.csv')
