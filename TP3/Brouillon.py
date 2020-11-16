#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:22:53 2020

@author: rahimamohamed
"""

import matplotlib.pyplot as plt
from datetime import datetime 
import numpy as np
import pandas as pd
from pyti.smoothed_moving_average import smoothed_moving_average as sma
from pyti.bollinger_bands import lower_bollinger_band as lbb


" VARIABLE DECLARATION" 


" QUESTION 1: Download of the file" 

data = pd.read_csv("https://raw.githubusercontent.com/Rahima-web/Hamiltonien/67773738288686dd932eb87932fd551b65b45f5d/TP3/bank_of_america.csv",sep=",",header=0)
data['Date']=[datetime.strptime(x, '%m/%d/%Y') for x in data['Date'].str.slice(0,11)]
#data = data.drop(['Open', 'High','Low','Volume','Adj Close'], axis=1)
#data=data.to_numpy()



data['fast_sma'] = sma(data['Close'].tolist(), 10)
data['slow_sma'] = sma(data['Close'].tolist(), 30)





" QUESTION 2: Separate the dataset in two parts: training and test datasets." 

nb = int(len(data)*0.70)
Train_date = data['Date'][:nb]
Train_close = data['Close'][:nb]

Test_date = data['Date'][nb:]
Test_close = data['Close'][nb:]

plt.plot(Train_date,Train_close,color="blue")
plt.plot(Test_date,Test_close,color="red")
plt.show()

" QUESTION 3: Portfolio function" 

## Trading Strategy

def strategy(Data):	
    '''If Price is 3% below Slow Moving Average, then Buy
	Put selling order for 2% above buying price'''
    nb = int(len(data)*0.70)
    A = np.zeros((nb,1))
    for i in range(1, len(Train_close)):
        if data['slow_sma'][i] > data['Close'][i] and (data['slow_sma'][i] - data['Close'][i]) > 0.03 * data['Close'][i]:
            A[i]=1
        if data['slow_sma'][i] > data['Close'][i] and (data['slow_sma'][i] - data['Close'][i]) < 0.02 * data['Close'][i]:
			A[i]=-1
    return A