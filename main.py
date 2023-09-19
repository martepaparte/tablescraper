import requests
from bs4 import BeautifulSoup
import pandas as pd

if __name__ == '__main__':
    url = 'https://www.sodra.lt/lt/senatves-pensijos-amziaus-lentele'
    # Get requestas
    page = requests.get(url)
    # paimamas puslapio HTML
    page_info = BeautifulSoup(page.text, 'lxml')
    # VYRAI
    table1 = page_info.find('table')
    # sukuriamas headeriu listas, kad butu juos galima pridet
    headers = []
    # pagal puslapio struktura randami lenteles headeriai
    for i in table1.find_all('tr')[1:2]:
        row_data = i.find_all('td')
        # headeriai apkarpomi nuo whitespace ir pridedami i lista
        title = [j.text.strip() for j in row_data]
        headers.append(title)
    # sukuriamas pandas dataframe lentelei saugoti
    mydata = pd.DataFrame(columns=headers)
    # pagal puslapio struktura randami lenteles duomenys, nukerpami whitespace ir issaugomi dataframe
    for j in table1.find_all('tr')[2:]:
        row_data = j.find_all('td')
        row = [i.text.strip() for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row
    mydata.to_csv('vyrai.csv', encoding="utf-8")

    # MOTERYS
    # ta pati veiksmu seka, skirtumas tik kad butu paimama sekanti lentele naudojama find_next_sibling funkcija ir tuo paciu zinoma kitas .csv pavadinimas
    table2 = page_info.find('table').find_next_sibling('table')
    headers = []
    for i in table2.find_all('tr')[1:2]:
        row_data = i.find_all('td')
        title = [j.text.strip() for j in row_data]
        headers.append(title)
    mydata = pd.DataFrame(columns=headers)
    for j in table2.find_all('tr')[2:]:
        row_data = j.find_all('td')
        row = [i.text.strip() for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row

    mydata.to_csv('moterys.csv', encoding="utf-8")
