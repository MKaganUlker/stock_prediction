import investpy
import csv
import os

search_result = investpy.search_quotes(text='bist 30', 
                                       countries=['turkey'], n_results=1)


historical_data = search_result.retrieve_historical_data(from_date='01/12/2011', to_date='31/12/2021')

#data manupilations
historical_data.drop('Open', inplace=True, axis=1)
historical_data.rename(columns = {'Close':'Price','Change Pct':'Change Percentage',}, inplace = True)
historical_data=historical_data.loc[::-1]
historical_data.to_csv('tr30_data.csv', sep=';',encoding='utf-8')
historical_data.to_csv(os.path.join(r'C:\Users\DELL\Desktop\Yeni klasör\data','tr30_data.csv'),mode='a', sep=';',na_rep='N/A')
information = search_result.retrieve_information()



