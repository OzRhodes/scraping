# A script to scrape a medical site which 
# was a task on Upwork

import requests
from bs4 import BeautifulSoup
import pandas as pd



def get_clinic(clinic_id):
    url = f'https://{clinic_id}.portal.athenahealth.com'
    response = requests.get(url)
    soup = BeautifulSoup(response, 'html.parser')
    clinic_name = soup.find_all('h1', [-1].text.strip())
    return clinic_name
    

clinic_list=[]

for clinic_id in range (start,end+1):
    data_dict = {}
    data_dict['clinic_id'] = clinic_id
    data_dict['clinic_name'] = get_clinic(clinic_id)
    if 'Payment ' not in data_dict['clinic_name'] and 'Sorry ' not in data_dict['clinic_name']:
        clinic_list.append(data_dict)

df = pd.DataFrame(clinic_list)
print(df)
