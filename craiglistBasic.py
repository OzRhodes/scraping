
# script that scrapes the telephone numbers from craigslist Miami
# output is a CSV file with the telephone number in 
# +19095551234  format


import requests
from bs4 import BeautifulSoup
import re
import time

urls = ["https://miami.craigslist.org/brw/ctd/d/fort-lauderdale-2011-ford-fusion-4dr/7311858620.html",
"https://miami.craigslist.org/brw/ctd/d/fort-lauderdale-2016-mercedes-benz/7311856789.html",
"https://miami.craigslist.org/mdc/ctd/d/hialeah-2019-limited-4dr-suv-jeep/7311854992.html",
"https://miami.craigslist.org/brw/ctd/d/fort-lauderdale-2013-mercedes-benz-glk/7311854702.html",
"https://miami.craigslist.org/brw/cto/d/fort-lauderdale-2003-honda-cr-awd/7311838567.html",
"https://miami.craigslist.org/mdc/ctd/d/miami-2013-audi-q7-499-downeveryone/7311854285.html",
"https://miami.craigslist.org/mdc/ctd/d/miami-2015-chevrolet-suburban-499/7311853618.html",
"https://miami.craigslist.org/mdc/ctd/d/miami-2018-chevrolet-equinox-ls-skujs/7311853128.html",
"https://miami.craigslist.org/brw/ctd/d/fort-lauderdale-2018-audi-a5-coupe/7311842246.html",
"https://miami.craigslist.org/brw/ctd/d/fort-lauderdale-2008-chevrolet-chevy/7311905003.html",
"https://miami.craigslist.org/pbc/ctd/d/west-palm-beach-2014-chevy-chevrolet/7311837839.html"]

def link_finder(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    url_list =[]
    for a in soup.find_all('a', href=True):
        url_list.append(a['href'])
    
    return url_list

# The only relevant numbers are in the posting body section
def find_numbers(url):
    result= []
    reg_string = re.compile(r'\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        content = soup.find('section', id='postingbody').text
        result = reg_string.findall(content)
    except:
        pass
    try:
        content = soup.find('h1', class_='postingtitle').text
        result = reg_string.findall(content)
    except:
        pass      
        result = set(result)
        #result = list(result)
    result = clean_numbers(result)
    return result

def clean_numbers(numbers):
    result =[]
    temp =[]
    for number in numbers:    
        temp.append(re.sub('[^0-9]','', number))
    for number in temp:
        number = '+1'+number
        result.append(number)
    return result
    
    
# write as csv file for spreadsheet access
def save_to_file(numbers):
    with open('numbers.csv', 'a') as opened_file:
        for number in numbers:
            number += ',' 
            opened_file.write(number)
        

# Check the links are worth looking at
def check_captcha(link):
    content = requests.get(url).text
    return 'show contact info' in content
        

######################
#
# Main Section
#
######################

print("*****************************************")
print("*                                       *")
print("*      Number Harverster                *")
print("*                                       *")
print("*****************************************")
print(" ")
print(" ")

    # Defining Global Variables
    
    # Site specifics 
    # Target URL

url = "https://miami.craigslist.org/"
    
    # valid links for parsing
    
valid_links1 = []
valid_links2 = []
count = 0
    
    # The list of numbers
full_numbers =[]
    
    # Start the scraping process
    
first_links = link_finder(url)
    
    # check first level of links
for link in first_links:
    if link[:2] == '/d':       # Useful links are prefixed by this /d
        link = url + link
        valid_links1.append(link)

for link in valid_links1: 
    valid_links2 = link_finder(link)
    for link2 in urls: #valid_links2:
        if '/d/' in link2 and len(link2) > 50 and link2[:2] != '//':
            
            numbers = find_numbers(link2)
            print(link2)
            print(" ")
            count += len(numbers)
            print ('Numbers on page : {} '. format(len(numbers)))
            print ('Total numbers : {} '. format(count))
            print(" ")
            print(numbers)
            for number in numbers:
                if number not in full_numbers:     # Only get unique numbers
                        full_numbers.append(number)
            print (full_numbers)
            if len(full_numbers)== 1:
                save_to_file(full_numbers)
                full_numbers =[]            
                
        


    
