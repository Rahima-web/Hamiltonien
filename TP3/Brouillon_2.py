#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:42:30 2020

@author: rahimamohamed
"""

import matplotlib.pyplot as plt
from datetime import datetime 
import numpy as np
import pandas as pd
##from pyti.bollinger_bands import lower_bollinger_band as lbb


" VARIABLE DECLARATION" 


" QUESTION 1: Download of the file" 

DATA = pd.read_csv("https://raw.githubusercontent.com/Rahima-web/Hamiltonien/67773738288686dd932eb87932fd551b65b45f5d/TP3/bank_of_america.csv",sep=",",header=0)
DATA['Date'] = [datetime.strptime(x, '%m/%d/%Y') for x in DATA['Date'].str.slice(0,11)]
DATA = DATA.drop(['Open', 'High','Low','Volume','Adj Close'], axis=1)
DATA = DATA.to_numpy()


#data['fast_sma'] = sma(data['Close'].tolist(), 10)
#data['slow_sma'] = sma(data['Close'].tolist(), 30)


" QUESTION 2: Separate the dataset in two parts: training and test datasets." 

#We are taking 70% of the DATA for the training and 30 % for the test


NB_OF_TRAIN = int(len(DATA)*0.70) 
Train_date = DATA[0:NB_OF_TRAIN,0]
Train_close = DATA[0:NB_OF_TRAIN,1]

Test_date = DATA[NB_OF_TRAIN:len(DATA),0]
Test_close = DATA[NB_OF_TRAIN:len(DATA),1]

plt.plot(Train_date,Train_close,color="blue")
plt.plot(Test_date,Test_close,color="red")
plt.show()


"""
QUESTION 3
"""

n_train = len(Train_date)
Initial_nbshare = 0
NB_of_Share = 30
Initial_Cash = 5000

"""
Here we A matrix S is defined which describes each state: 
each state corresponds to the closing price for 5 days, 
the number of shares owned, and the cash owned.
"""

def State_function(data,Nb,Cash):
    pas = 5
    close_price = []
    for i in range(1,pas):
        close_price.append(data[0:i:1])
    for i in range(pas,n_train+1):
        close_price.append(data[i-pas:i:1])
    S = [close_price,Nb,Cash]
    return S

S = State_function(Train_close,NB_of_Share,Initial_Cash) 
#print(S) 

"""
For the reward function: we calculate the 5-day simple moving average, then we set that: 
    - if the close price is 3% below the  5-day simple Moving Average, then we buy 
    - if the close price is 2% above the  5-day simple Moving Average, then we sell
"""

def Reward_function(State,a,t):
    R = 0
    Cash = State[2]
    nb = State[1]
    S = State
    #SMA = np.mean(S[0][t])
    
    ## The case where we SELL
    if (a == 1) & (nb >= 30):
        if (S[0][t][-1] >= (np.mean(S[0][t])* 0.03)): 
            R = S[0][t][-1] * NB_of_Share
            Cash+= R
            nb -= NB_of_Share
            
        #The case where where we have 0 share in our portfolio, so we can't sell   
        if (nb==0): 
                R = 0
                nb = nb
                Cash = Cash
        else:
            R = 0
            nb = nb
            Cash = Cash
            
    ## The case where we BUY, we verify that we have enough cash      
    if (a == 2) : 
        if (Cash >= S[0][t][-1] * NB_of_Share):
            if (S[0][t][-1] <= (np.mean(S[0][t]) * 1.02)): 
                R = -S[0][t][-1] * NB_of_Share
                Cash+= R
                nb += NB_of_Share
            else:
                R = 0
                nb = nb
                Cash = Cash
    
    ## The case where we HOLD        
    if (a == 0):
        R = 0
        nb = nb
        Cash = Cash
    
    ##The case where where we have 0 share in our portfolio, so we can't sell
#    if (nb==0):
#        R = -S[0][t][-1] * NB_of_Share
#        Cash+= R
#        nb += NB_of_Share
        
    return R,nb,Cash

R = Reward_function(State_function(Train_close,0,5000),2,35)

#print(R)

def Portfolio_function(old_ptf,S,a,t):
    R,Nb,Cash = Reward_function(S,a,t)
    ptf = old_ptf
    
    #the case where we at t=0, initale state
    if t == 0:
        ptf = Initial_Cash 
    else:
        ptf += Cash
    return ptf


"""
QUESTION 4
"""

alpha = 0.01
gamma = 0.9

def Research_of_max(old_cash,S,t):
    Action = np.zeros((3,1))
    Nb = S[1]
    # If the number of owned shares is equal to zero, so we buy, then a=2 
    if Nb == 0:
        a=2
        Action[a] = Portfolio_function(old_cash,S,a,t)
    else:
        for k in range(0,3):
            Action[k] = Portfolio_function(old_cash,S,k,t)
        #We reseach th eoptimal action a
        index = np.where(Action == np.max(Action))
        a = index[0][0] 
    return Action[a],a

#def Q_learning(data):
#    Q = np.zeros((n-1,3))
#    S = state(data,Nb_init,Cash_init)
#    for t in range(0,n-1):
#        for a in range(0,3):
#            R,Nb,Cash = reward(S,a,t)
#            Qmax = maxi(Cash,S,t+1)
#            for itera in range(0,20):
#                Q[t,a] = (1 - alpha) * Q[t,a] + alpha * (R + gamma * Qmax[0])                
#        
#        S = state(data,Nb,Cash)
#        _,Nb,Cash = reward(S,Qmax[1],t)
#    return Q
#
#Q = Q_learning(close_train)
#print(Q)

def Q_learning_algorithm(data):
    Q = np.zeros((n_train-1,3))
    old_NB,old_Cash = NB_of_Share,Initial_Cash
    Cashs = [old_Cash]
    for t in range(1,n_train):
        S = State_function(data,old_NB,old_Cash)
        for a in range(0,3):
            
            R,Nb,Cash = Reward_function(S,a,t-1)
            Q_max = Research_of_max(Cash,S,t)
            
            for itera in range(0,50):
                Q[t-1,a] = (1 - alpha) * Q[t-1,a] + alpha * (R + gamma * Q_max[0])                
            
        R,new_NB,new_Cash = Reward_function(State_function(data,Nb,Cash),Q_max[1],t)
        old_NB,old_Cash = new_NB,new_Cash
        Cashs.append(new_Cash)
        
    return Q,Cashs

Q,Cash = Q_learning_algorithm(Train_close)

PI=np.zeros((len(Q),1))
for i in range(0,len(Q)):
    PI[i]=np.argmax(Q[i])

    

plt.plot(Train_date [:-1],Q[:,0], label = 'A = 0')
plt.plot(Train_date [:-1],Q[:,1], label = 'A = 1')
plt.plot(Train_date [:-1],Q[:,2], label = 'A = 2')
plt.legend()
plt.show()

plt.plot(Train_date ,Cash, label = 'Cash')
plt.show()

plt.plot(Train_date [:-1],PI, label = 'policy')
plt.legend()
plt.show()

