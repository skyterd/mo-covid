from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get('')

content = source.content
