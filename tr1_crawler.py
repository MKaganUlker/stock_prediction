import investpy
import csv
import os
import requests

path=r'C:\Users\DELL\Desktop\Yeni klasör\data\tr_stocks'
stocks=['Akbank TAS','Arcelik AS','Aselsan', 'BIM Magazalar','Dogan Holding','Emlak Konut GYO','Erdemir','Ford Otosan','Garanti Bank',
'Gubretas','Kardemir D','Koc Holding','Koza Altin','Koza Anadolu','Pegasus','Petkim','Sabanci Holding','SASA Polyester','Sisecam',
'TAV Havalimanlar','Tekfen Holding','THY','Tofas','Tupras Turkiye','Turk Telekom','Turkcell','Turkiye Halk Bk','Turkiye Is Bankasi C',
'Vestel','Yapi ve Kredi Bankasi']

for i in range(len(stocks)):
    search_result = investpy.search_quotes(text=stocks[i], countries=['turkey'], n_results=1)
    
    historical_data = search_result.retrieve_historical_data(from_date='01/12/2011', to_date='30/12/2021')
    
    #data manupilations
    historical_data.drop('Open', inplace=True, axis=1)
    historical_data.rename(columns = {'Close':'Price','Change Pct':'Change Percentage',}, inplace = True)
    temp_cols=historical_data.columns.tolist()

    historical_data=historical_data.loc[::-1]
    historical_data.to_csv(os.path.join(path,stocks[i]+'.csv'),mode='a', sep=';',na_rep='N/A')
    information = search_result.retrieve_information()
    

