#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 18:01:20 2020

@author: rahimamohamed
"""

from datetime import datetime 
import numpy as np
import pandas as pd

" VARIABLE DECLARATION" 


" QUESTION 1: Download of the file" 

data = pd.read_csv("https://raw.githubusercontent.com/Rahima-web/Hamiltonien/67773738288686dd932eb87932fd551b65b45f5d/TP3/bank_of_america.csv",sep=",",header=0)
data['Date']=[datetime.strptime(x, '%m/%d/%Y') for x in data['Date'].str.slice(0,11)]
data = data.drop(['Open', 'High','Low','Volume','Adj Close'], axis=1)
data=data.to_numpy()


" QUESTION 2: Separate the dataset in two parts: training and test datasets." 

nb = int(len(data()*0.7))
Train_date = data[0:nb,0]
Train_close = data[0:nb,1]

Test_date = data[nb:len(data),0]
Test_close = data[nb:len(data),0]
" QUESTION 3: Portfolio function" 