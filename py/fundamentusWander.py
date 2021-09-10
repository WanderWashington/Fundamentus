import requests
from bs4 import BeautifulSoup
import csv
import json
import pandas as pd


def get_data():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    url = 'http://www.fundamentus.com.br/resultado.php'
    page = requests.get(url, headers=headers)
    return page.text

def get_details(stock):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    url = 'http://www.fundamentus.com.br/detalhes.php?papel='+stock
    page = requests.get(url, headers=headers)
    return page.text

def formatData(page):
    
    soup = BeautifulSoup(page, "lxml")
    data = {}
    tb = soup.find("table")
    output_rows = []
    column_data=[]
    for table_row in tb.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            output_row.append(column.text)
        if len(output_row) == 0:
            continue
        output_rows.append(format_column(output_row))

    for row in output_rows:
        import pdb; pdb.set_trace()
        detailsPage = get_details(row["Papel"])
        soup = BeautifulSoup(page, "lxml")
        tb = soup.find("table")
    # with open("resultados.json", "w") as write_file:
    #     json.dump(output_rows, write_file)
    # df = pd.read_json('resultados.json')
    # df.to_csv('resultados.csv', sep=';',index=None)


def format_column(column):
    return {
        "Papel":column[0],
        "Cotacao":column[1],
        "P/L":column[2],
        "P/VP":column[3],
        "PSR":column[4],
        "DY":column[5],
        "P/Ativo":column[6],
        "P/Cap.Giro":column[7],
        "P/EBIT":column[8],
        "P/ACL":column[9],
        "EV/EBIT":column[10],
        "EV/EBITDA":column[11],
        "Mrg.Ebit":column[12],
        "Mrg.Liq":column[13],
        "Liq.Corr":column[14],
        "ROIC":column[15],
        "ROE":column[16],
        "Liq2meses":column[17],
        "Pat.Liq":column[18],
        "Div.Brut/Pat":column[19],
        "Cresc5Anos":column[20]
        }

if __name__ == '__main__':
    result = get_data()
    formatData(result)
