import math
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler 
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import layers
import pickle
import os

def program(stock):
    path=r"C:\Users\DELL\Desktop\Yeni klasör\data"
    stocks=["ALK"]
    #for stock in stocks:
    print(type(stock))
    df = pd.read_csv(os.path.join(path,stock+'.csv'))
    df=df["Date;High;Low;Price;Volume;Change Percentage"].str.split(';', expand=True)
    df.columns=["Date","High","Low","Price","Volume","Change Percentage"]

    df = df.iloc[::-1].reset_index(drop = True)

    prices = pd.to_numeric(df['Price'])
    p_values = prices.values
    dates = pd.to_datetime(df['Date'])
    d_values = dates.values

    
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(p_values.reshape(-1,1))
    test_data = scaled_data
    x_test = []
    y_test = p_values

    for i in range(60, len(test_data)):
        x_test.append(test_data[i-60:i, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))


    save_path = r'C:\Users\DELL\Desktop\Yeni klasör\models\3model.h5'
    pk_model = keras.models.load_model(save_path)


    predictions = pk_model.predict(x_test)
    #print("x_test:",x_test)
    predictions = scaler.inverse_transform(predictions)
    rmse = np.sqrt(np.mean(predictions - y_test)**2)
    print(rmse)

    plt.figure(figsize=(16,8))
    plt.title('Model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    #plt.plot(x,train)
    plt.plot(d_values,p_values)
    plt.plot(d_values[60:],predictions)
    plt.legend(['Value', 'Predictions'], loc='lower right')
    #plt.savefig(stock+'.png')
    plt.show()