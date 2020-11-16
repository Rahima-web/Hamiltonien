#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 18:01:20 2020

@author: rahimamohamed
"""

from datetime import datetime 
import numpy as np
import pandas as pd
from pyti.smoothed_moving_average import smoothed_moving_average as sma

" VARIABLE DECLARATION" 


" QUESTION 1: Download of the file" 

data = pd.read_csv("https://raw.githubusercontent.com/Rahima-web/Hamiltonien/67773738288686dd932eb87932fd551b65b45f5d/TP3/bank_of_america.csv",sep=",",header=0)
data['Date']=[datetime.strptime(x, '%m/%d/%Y') for x in data['Date'].str.slice(0,11)]
data = data.drop(['Open', 'High','Low','Volume','Adj Close'], axis=1)
data=data.to_numpy()


" QUESTION 2: Separate the dataset in two parts: training and test datasets." 

nb = int(len(data)*0.75)
Train_date = data[0:nb,0]
Train_close = data[0:nb,1]

Test_date = data[nb:len(data),0]
Test_close = data[nb:len(data),0]

" QUESTION 3: Portfolio function" 

n = len(Train_date)

def policy(S): #POLICY DE MERDE TROUVER MIEUX
    A = np.zeros((n,1))
    for i in range(0,n):
        if S[i] > np.mean(S):
            A[i] = -1 #sell
        if S[i] < np.mean(S):
            A[i] = 1 #buy
        if S[i] == np.mean(S):
            A[i] = 0 #hold
    return A

A = policy(Train_close)
NB_share = 30
Cash = 5000

def reward(A,S,i):
    R = np.zeros((n,1))
    for j in range(0,n):
        if A[j] == -1:
            R[j]= -S[j] * NB_share
        if A[i] == 1:
            R[j]= S[j] * NB_share    
        if A[j] == 0:
            R[j]= 0
    return R[i]


R = [reward(A,Train_close,i) for i in range(0,n)]

def ptfs(R,i):
    ptf = np.zeros((n,1))
    ptf[0] = Cash
    if i == 0: 
        ptf[0] = Cash
    else:
        for j in range(0,n-1):
            ptf[j+1] = ptf[j] + R[j]
    return ptf[i]

    
ptf = [ptfs(R,i) for i in range(0,n)]

alpha = 0.4
gamma = 0.9

def Q_learnigDEMERDE(S,A):
    Q = np.zeros((n,1))
    Q_prec = Q
    for itera in range(10):        
        for i in range(0,n):
            
            break
