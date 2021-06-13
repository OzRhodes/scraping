#! /usr/bin/python3
# Download text from website and saves to file.
# TODO: Get address from clipboard.


from bs4 import BeautifulSoup as bs
import requests

url = 'ADD URL HERE'
content = requests.get(url).text

#print(content)

soup = bs(content)
print (soup)
'''
book_list=[]
for book in soup.find_all('div', class_='abook'):
    book_list.append(book.h2.a['href'])

#for book_url in book_list:
#url = 'https://sive.rs/' + book_list[0]
#print(url)
content = requests.get(url).text
soup = bs(content)

notes = soup.find('title').text
notes = notes + '\n\n'

notes = notes + soup.find('p', id='booknotes').text

print(notes) 
print ('')
title = url.split('/')[-1] + '.txt'
print (title)

notesFile = open(title, 'wb')
notesFile.write(notes)

notesFile.close()

'''
