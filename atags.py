'''
This script extracts full links from a website for individual investigation 
at a later date.

It could also be a function for a mor e comprehensive web scraping script.
'''


import requests
from bs4 import BeautifulSoup as bs4

url = "https://dev.to/devdefinitive/33-github-projects-i-have-bookmarked-and-you-should-298o"

response = requests.get(url)
#print(response.text)
soup = bs4(response.text, 'html.parser')
#soup.prettify())

main = soup.find_all('h3')
fulllist=dict()
for item in main:
	try:
		link = (item.find('a').findNext('a'))
		site = str(link.get('href'))
		if 'github' in (site):
			name = (link.text)
			#print(name)
			fulllist[name] = site
	
	except:
		pass

for key, value in fulllist.items():
	print (key, value)
#print(link)
	
	
	#fulllist[site] = name
	
#print(fulllist)
'''
masterlist =[]
for item in fulllist:
	if 'github' in item:
		masterlist.append(item)

print(masterlist)

aTags = main.find_all('h3')
print(aTags)
for tag in aTags:
	print(tag.get('href'))
	, {'class':'article-wrapper'})
'''
