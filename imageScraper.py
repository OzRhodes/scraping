# A script to scrape a site for pngs  
# which  was a task on Upwork
# data was for ML training

import requests
from bs4 import BeautifulSoup
import pandas as pd


site_map = ''
f'https://{clinic_id}.portal.athenahealth.com'

response = requests.get(url)
xml=response
soup = BeautifulSoup(xml.text, 'xml')

site_maps = []

for loc in soup.find_all('loc'):
    addr =loc.text 
    if part in addr:
        site_maps.append()
    
# so now we have a list of site maps

site_map_1 = site_maps[0]


response = requests.get(site_map_1)
soup = BeautifulSoup(response.text, 'html.parser')

image_addr_list = []

for addr in soup.find_all('loc')
    url = addr.text
    image_addr_list.append(url)

# now we have a list of images for the first site_map

# we now need to go to each address and download the response

for image_url in image_addr_list:
    reponse = requests.get(image_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    png_url = soup.find('a', {'class', : 'download'})['href']
    image = requests.get(png_url)
    image_id = 
    image_name = image_url.split('/')[-1] + ' ' + image_url.split('/')[-1]
    with open(image_name, 'wb') as file:
        file.write(image.content)
    



'''
site map approach



'''
