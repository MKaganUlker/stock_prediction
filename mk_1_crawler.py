from email import header
from urllib import response
from click import option
import lxml
from lxml import html
import csv
import pandas as pd
import bs4
import requests
from bs4 import BeautifulSoup
import os
import mechanicalsoup


path=r'C:\Users\DELL\Desktop\Yeni klasör\data\mk_stocks'
header = ['Date','Last trade price','Max','Min','Avg. Price','Change Percentage','Volume','Turnover in BEST in denars','Total turnover in denars']
stocks=["ALK","KMB","MPT","TEL","TNB","TTK","GRNT","MTUR","SBT","STB"]
for j in range(10):
	url='https://www.mse.mk/en/stats/symbolhistory/'+ stocks[j]
	browser = mechanicalsoup.Browser()
	page = browser.get(url)
	form=page.soup.select("form")[1]
	for i in range(10):
		year1=str(22-i)
		year2=str(21-i)
		form.select("input")[0]["value"]="01/01/20"+year2
		form.select("input")[1]["value"]="01/01/20"+year1
		new_page=browser.submit(form,page.url)

		table = new_page.soup.find( "table", {"id":"resultsTable"} )
		rows=[]

		for row in table.findAll("tr"):
			data=[]
			for xxx in row.findAll("td"):
				z=xxx.get_text().strip()
				z=z.replace(",","")
				data.append(z)
			rows.append(data)
		rows.pop(0)
		df = pd.DataFrame(rows,columns=header)
		#data manupilations
		df.drop('Turnover in BEST in denars', inplace=True, axis=1)
		df.drop('Total turnover in denars', inplace=True, axis=1)
		df.drop('Avg. Price', inplace=True, axis=1)
		df.rename(columns = {'Last trade price':'Price','Max':'High','Min':'Low'}, inplace = True)
		temp_cols=df.columns.tolist()
		
		index=df.columns.get_loc("Change Percentage")
		new_cols=temp_cols[0:index] + temp_cols[index+1:]+temp_cols[index:index+1]
		df=df[new_cols]
		
		df=df[["Date","High","Low","Price","Volume","Change Percentage"]]
		
		df['Date']=pd.to_datetime(df.Date)
		#saving scraped data to data file
		if i==0:
			df.to_csv(os.path.join(path,stocks[j]+'.csv'),mode='a', sep=';',na_rep='N/A',index=False)
		else:
			df.to_csv(os.path.join(path,stocks[j]+'.csv'),mode='a', sep=';',na_rep='N/A',index=False,header=None)

