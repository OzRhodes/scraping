#! /usr/bin/python3
# Download text from website and saves to file.
# TODO: Get address from clipboard.


from bs4 import BeautifulSoup as bs
import requests

url = 'https://sive.rs/book'
content = requests.get(url).text

print(content)

soup = bs(content)
print (soup)

book_list=[]
for book in soup.find_all('div', class_='abook'):
    book_list.append(book.h2.a['href'])

for book_url in book_list:
print(book_url) 


