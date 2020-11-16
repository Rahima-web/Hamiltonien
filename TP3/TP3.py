#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 18:01:20 2020

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
    for i in range(1,nb):
        if Data['slow_sma'][i] > Data['Close'][i] and (Data['slow_sma'][i] - Data['Close'][i]) > 0.03 * Data['Close'][i]:
            A[i]=1 #achat
        if Data['slow_sma'][i] < Data['Close'][i] and (Data['slow_sma'][i] - Data['Close'][i]) < 0.02 * Data['Close'][i]:
            A[i]=-1 #vend
    return A
    

A=strategy(data)

NB_share = 30
Cash = 5000
nb = int(len(data)*0.70)

#price_trans = 0.1*30*valeurclose

def reward(A,S,i):
    # ON VEUT MAXIMISER LE CASH DU PTF: si on vend on gagne du cash et si on achète on perd du cash
    R = np.zeros((nb,1))
    for j in range(0,nb):
        if A[j] == -1:
            R[j]= S[j] * NB_share - 0.1* S[j] * NB_share
        if A[i] == 1:
            R[j]= -S[j] * NB_share - 0.1* S[j] * NB_share
        if A[j] == 0:
            R[j]= 0
    return R[i]



R = [reward(A,Train_close,i) for i in range(0,nb)]


def ptfs(R):
    ptf = np.zeros((nb,1))
    ptf[0] = Cash
    for j in range(0,nb-1):
         ptf[j+1] = ptf[j] + R[j]      
    return ptf

    
ptf = ptfs(R)

alpha = 0.4
gamma = 0.9

def Q_learnig(S,A):
    Q = np.zeros((nb,1))
    Q_prec = Q
    for itera in range(10):        
        for i in range(0,nb):
            
            break















#n = len(Train_date)

#def policy(S): 
#    A = np.zeros((n,1))
#    for i in range(0,n):
#        if S[i] > np.mean(S):
#            A[i] = -1 #sell
#        if S[i] < np.mean(S):
#            A[i] = 1 #buy
#        if S[i] == np.mean(S):
#            A[i] = 0 #hold
#    return A
#
#
#A = policy(Train_close)
#NB_share = 30
#Cash = 5000

#def reward(A,S,i):
#    R = np.zeros((n,1))
#    for j in range(0,n):
#        if A[j] == -1:
#            R[j]= -S[j] * NB_share
#        if A[i] == 1:
#            R[j]= S[j] * NB_share    
#        if A[j] == 0:
#            R[j]= 0
#    return R[i]
#
#
#R = [reward(A,Train_close,i) for i in range(0,n)]
#
#def ptfs(R,i):
#    ptf = np.zeros((n,1))
#    ptf[0] = Cash
#    if i == 0: 
#        ptf[0] = Cash
#    else:
#        for j in range(0,n-1):
#            ptf[j+1] = ptf[j] + R[j]
#    return ptf[i]
#
#    
#ptf = [ptfs(R,i) for i in range(0,n)]
#
#alpha = 0.4
#gamma = 0.9
#
#def Q_learnig(S,A):
#    Q = np.zeros((n,1))
#    Q_prec = Q
#    for itera in range(10):        
#        for i in range(0,n):
#            
#            break
