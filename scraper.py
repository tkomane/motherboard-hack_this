#!/usr/bin/env python3

"""
A Python script for scraping websites.

Michael's idea was to scrape a jail roster website,
whereas I'll be scraping the IMDb top 250, to discover
which years where 'the best' for movies (according to IMDb voters)

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

# First we trim the specific table we want
table = soup.find('table', attrs={'data-caller-name': 'chart-top250movie'})

# Now I'm trimming the specific tag with my dates
target = table.findAll('span', attrs={'class': 'secondaryInfo'})

# This removes the tags from my dates
for i in range(len(target)):
    target[i] = target[i].string

countset = Counter(target)

print('Most common:')
for year, count in countset.most_common(10):
    print('{}: {}'.format(year, count))
