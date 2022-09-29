import investpy
import csv
import os

search_result = investpy.search_quotes(text='akbank', 
                                       countries=['turkey'], n_results=1)


historical_data = search_result.retrieve_historical_data(from_date='01/12/2011', to_date='31/12/2021')

print(historical_data)