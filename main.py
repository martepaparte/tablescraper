import requests
from bs4 import BeautifulSoup
import pandas as pd

if __name__ == '__main__':
    url = 'https://www.sodra.lt/lt/senatves-pensijos-amziaus-lentele'
    page = requests.get(url)
    page_info = BeautifulSoup(page.text, 'lxml')
    table1 = page_info.find('table')
    headers = []
    for i in table1.find_all('tr')[1:2]:
        row_data = i.find_all('td')
        title = [j.text for j in row_data]
        headers.append(title)
    mydata = pd.DataFrame(columns=headers)
    for j in table1.find_all('tr')[2:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row
    mydata.to_csv('test2.csv', index=False)