import requests
from bs4 import BeautifulSoup
import pandas as pd


# extract


def extract(page):
    headers = {'User-Agent':''}
    url = f'http={page}'
    r = requests.get(url,headers)
    soup = BeautifulSoup(r.content,'html_parser')
    
    return soup

# transform
def transform(soup):
    divs = soup.find_all('div',class_='')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_='company').text.strip()
        try:
            salary = item.find('span', class_='salaryText').text.strip
        except:
            salary =' '
        summary = item.find('div', class_='summary').text.strip().replace('\n','')
        
        # store in dictionary
        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }
        joblist.append(job)
    return
    
    
    
# load

#main



content = extract(0)
transform(content)


# for i in range(0,40,10):

df = pd.dataframe(joblist)
print(df.head())
df.to.csv('jobs.csv')

        


