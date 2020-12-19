import requests
import pandas as pd
from datetime import datetime
import dateutil.parser


url = "https://services.arcgis.com/GHhNHT1xiCkCAXvo/arcgis/rest/services/COVID19_Data/FeatureServer/0/query"

params = {
    "f": "json",
    "where": "Date_of_Test BETWEEN timestamp '2020-09-17 05:00:00' AND CURRENT_TIMESTAMP",
    "returnGeometry": False,
    "spatialRel": "esriSpatialRelIntersects",
    "outFields": [
        'Date_of_Test',
        'Daily_Cases',
        'Cumulative_Cases',
        # 'Percent_Increase',
        'Five_Day_Average',
        # 'Date_of_Actual_Death',
        'Deaths_Totals',
        # 'FID',
    ],
    "orderByFields": "Date_of_Test desc",
    "resultOffset": 0,
    "resultType": "standard"
}
r = requests.get(url, params=params)
r.json()['features'][:5]
data = [d['attributes'] for d in r.json()['features']]
boco = data[:5]

df = pd.DataFrame(boco)
df = df.drop(columns=['FID'])

timestamp = data[0]['Date_of_Test']
timestamp_no_ms = int(str(timestamp)[:-3])
naive_dt = dt = datetime.fromtimestamp(timestamp_no_ms)
# print(x)

import pytz
central = pytz.timezone('US/Central')
dt = datetime.fromtimestamp(timestamp_no_ms, tz=central)
# print(dt)

# time = df['Date_of_Test']

# print(time.head())

df = df.drop(columns=['Date_of_Test'])

print(df)

df.to_csv('mo-covid.csv')