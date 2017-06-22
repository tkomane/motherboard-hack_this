#!/usr/bin/env python3

"""
A Python script for scraping websites.

Michael's idea was to scrape a jail roster website,
whereas I'll be scraping the IMDb top 250, to discover
what percentage of movies from each decade are represented
on the list.

By Tshiamo Komane
"""
# Parsing the HTML document
from bs4 import BeautifulSoup
from collections import Counter
import requests  # module holds functions that query the webpage

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)  # this is where we get the HTML
html = response.content  # .content clears 'response' of the junk we don't need
soup = BeautifulSoup(html, "html5lib")  # html5lib is the specific parser

# Now we trim down
table = soup.find('table', attrs={'data-caller-name': 'chart-top250movie'})
for row in table.findAll('tr'):
    for cell in row.findAll('td'):
        print(cell.text)
