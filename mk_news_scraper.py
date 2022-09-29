import lxml
import csv
import pandas as pd
import bs4
import requests
from bs4 import BeautifulSoup
import mechanicalsoup
stocks=["Alkaloid","Komercijalna+banka","Makedonski+Telekom","Stopanska+banka","Гранит","NLB+Banka","TTK+Banka","Makpetrol","Makedonijaturist","Stopanska+banka+AD+Skopje","Stopanska+banka+AD+Bitola"]
header=['Date','Title','Article']
for stock in stocks:
    browser = mechanicalsoup.Browser()
    date1='01.12.2011'
    data=[]
    url='https://time.mk/?q='+stock+'&search=news&order=inc&startdate='+date1+'&enddate=31.12.2021'

    while date1!='31.12.2021':
        page = browser.get(url)
        news=page.soup.findAll("div", {"class": "cluster"})
        for new in news:
            xxx=[]
            title=new.findAll("h1")[0].text.strip()
            article=new.findAll("p", {"class": "snippet"})[0].text.strip()
            date=new.findAll("span", {"class": "when"})[0].text.strip()
            if 'Global Game Jam' in title:
                continue
            #print(title)
            #print(article)
            #print('date',date)
            xxx.append(date)
            xxx.append(title)
            xxx.append(article)
            data.append(xxx)
        if  date1==date:
            year=str(int(date1[6:]))
            month=date1[3:5]
            day=str(int(date1[:2]))
            
            if (month=='01' or month=='03' or month=='05' or month=='07' or month=='08' or month=='10' or month=='12') and (day=='31'):
                month=str(int(month)+1)
                day='1'
            if (month=='04' or month=='06' or month=='09' or month=='11') and (day=='30'):
                month=str(int(month)+1)
                day='1'
            if (month=='02') and (day=='28'):
                month=str(int(month)+1)
                day='1'
            day=str(int(day)+1)
            if len(day)==1:
                day='0'+day
            if len(month)==1:
                month='0'+month

            date1=day+'.'+month+'.'+year
            date=date1
        else:
            date1=date
        url='https://time.mk/?q='+stock+'&search=news&order=inc&startdate='+date1+'&enddate=31.12.2021'


    df = pd.DataFrame(data,columns=header)
    df = df.iloc[::-1]
    df['Date']=pd.to_datetime(df.Date)
    df.drop_duplicates(subset=['Title'])
    df.to_csv(stock+'.csv',mode='a', sep=';',na_rep='N/A',index=False)

    browser.close()


