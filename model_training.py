import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler 
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import layers
import os
path=r'C:\Users\DELL\Desktop\Yeni klasör\models'

df = pd.read_csv(r'data\mk_stocks\ALK.csv')
df=df["Date;High;Low;Price;Volume;Change Percentage"].str.split(';', expand=True)
df.columns=["Date","High","Low","Price","Volume","Change Percentage"]
df = df.iloc[::-1].reset_index(drop = True)

prices = pd.to_numeric(df['Price'])
p_values = prices.values

dates = pd.to_datetime(df['Date'])
d_values = dates.values

Q1 = np.percentile(prices, 25,
                   interpolation = 'midpoint')
 
Q3 = np.percentile(prices, 75,
                   interpolation = 'midpoint')
IQR = Q3 - Q1
 
print("Old Shape: ", df.shape)
 
# Upper bound
upper = np.where(prices >= (Q3+1.5*IQR))
# Lower bound
lower = np.where(prices <= (Q1-1.5*IQR))
 
''' Removing the Outliers '''
df.replace(upper[0], prices.mean())
df.replace(lower[0], )

print("New Shape: ", df.shape)

training_data_len = math.ceil(len(p_values)* 0.8)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(p_values.reshape(-1,1))
train_data = scaled_data[0: training_data_len, :]

x_train = []
y_train = []
for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])   
x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
test_data = scaled_data[training_data_len-60: , : ]
x_test = []
y_test = p_values[training_data_len:]
for i in range(60, len(test_data)):
  x_test.append(test_data[i-60:i, 0])
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

model = keras.Sequential()
model.add(layers.LSTM(100, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(layers.LSTM(100, return_sequences=False))
model.add(layers.Dense(50))
model.add(layers.Dense(30))
model.add(layers.Dense(10))
model.add(layers.Dense(1))
model.summary()
rmse=111
while rmse>3:
  #fitting, testing, rmse calculation and saving the model
  callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)
  model.compile(optimizer='adam', loss='mean_squared_error')
  model.fit(x_train, y_train, batch_size= 32, epochs=100, callbacks=[callback])


  predictions = model.predict(x_test)
  predictions = scaler.inverse_transform(predictions)
  rmse = np.sqrt(np.mean(predictions - y_test)**2)
  print(rmse)
  print(int(rmse))


  save_path = os.path.join(path,str(int(rmse))+'model.h5')
  model.save(save_path)


data = p_values
train = data[:training_data_len]
validation = data[training_data_len:]
x=d_values[:training_data_len]
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date')
plt.ylabel('Price')
plt.plot(d_values[training_data_len:],data[training_data_len:])
plt.plot(d_values[training_data_len:],predictions)
plt.legend(['Value', 'Predictions'], loc='lower right')
plt.show()