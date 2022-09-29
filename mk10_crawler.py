
import csv
import pandas as pd
import bs4
import requests
from bs4 import BeautifulSoup
import lxml
r=requests.get('https://www.mse.mk/Page.aspx/indicies/MBI10/values')

soup=bs4.BeautifulSoup(r.text,"lxml")

table = soup.find( "table", {"id":"tableMBI10"} )
rows=[]

for row in table.findAll("tr"):
	x=row.get_text().strip()
	x=x.replace(',','')
	x=x.replace('\n',';')
	rows.append(x)

df = pd.DataFrame(rows)
df.to_csv(r'C:\Users\DELL\Desktop\Yeni klasör\data\mk10_data.csv', sep=';',na_rep='N/A',index=False)
