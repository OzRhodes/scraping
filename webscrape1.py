#! /usr/bin/python3
# wbScraper.py - DOwnload file from website and saves to file.
# TODO: Get address from clipboard.

from bs4 import BeautifulSoup as bs
import requests
url = 'https://sive.rs/book/OnWritingWell'
res = requests.get(url)
res.raise_for_status()
res.status_code == requests.codes.ok
print(res.text[:250000])
'''playFile = open('BoolList.html', 'wb')
for chunk in res.iter_content(250000):
    playFile.write(chunk)

playFile.close()
'''
