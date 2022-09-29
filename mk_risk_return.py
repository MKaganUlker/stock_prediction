import pandas as pd
import csv
from statistics import mean
import statistics
import numpy as np

stocks=["ALK","KMB","MPT","TEL","TNB","TTK","GRNT","MTUR","SBT","STB"]
df = pd.read_csv(r'data\mk_stocks\ALK.csv')
df=df["Date;High;Low;Price;Volume;Change Percentage"].str.split(';', expand=True)
df.columns=["Date","High","Low","Price","Volume","Change Percentage"]

df2 = df.iloc[::-1].reset_index(drop = True)
first = float(df2["Price"][0])

prices=pd.to_numeric(df2["Price"])
dates=df2["Date"]
ders=[]
risks=[]
year=12
j=1
while dates[j][:4] =='20'+str(year):
    ri_arr=[]
    second=float(df2["Price"][j])
    ri=((second/first)-1)*100
    first=second
    ri_arr.append(ri)
    der=mean(ri_arr)
    ders.append(der)
    risk=statistics.stdev(ri_arr)
    risks.append(risk)
    year=+1
    j+=1
    print(ri_arr)

#print('daily expected return',der)
#print('unsystematic risk',risk)
#print(der-risk,der+risk,'62.13% chance it is going to be between these percentages')
#print(der-risk*2,der+risk*2,'93.29% chance it is going to be between these percentages')
#print(der-risk*3,der+risk*3,'99.73% chance it is going to be between these percentages')

print(ders)