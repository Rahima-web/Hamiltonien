#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 14:13:01 2020

@author: rahimamohamed
"""

"""
GROUPE : Rahima Mohamed, Mahisha Uruthirasigamani, Danush Chandrarajah  

PROBLEM :
    
You need to sell a car. At every time t = 0, · · · , T − 1, you set a price pt
, and a customer then views the car. 
The probability that the customer buys a car at price p is D(p). 
If the car is not sold at time T, then it is sold for a fixed price WT , WT < 1.
Maximize the reward from selling the car and find the recursion for the optimal 
reward, when D(p) = (1 − p)+.
"""

import numpy as np
import matplotlib.pyplot as plt
import random

" VARIABLE DECLARATION " 

# Maturity
T = 500 

# if the car is not sell until T

W_T = 0.3

# Cumulative Reward

W=np.zeros((T,1))


#Price matrix
P = np.zeros((T,1))


time=[i for i in range(0,T)]


""" QUESTION 1 : Find the optimal strategy and the wealth 
i.e., the optimal expected cumulative reward) over time using 
the Bellman equation. 

"""

def Wealth():
    #W_T is fixed and W_0 is equal to zeros
    W[T-1]=W_T
    W[0]=0
    for i in range (T-1,0,-1):
        W[i-1]= ((1+W[i])/2.0)**2
    W[0]=0
    return W


W=Wealth()


print( "\n------Question 1 : the optimal expected cumulative reward------\n")
print (W)

def Price(W):
    P[T-1]=W_T
    for i in range (T-1,0,-1):
        P[i-1]= (1+W[i])/2.0    
    return P
P=Price(W)


""" QUESTION 2 : Plot the resulting optimal strategy and the wealth over time. """

print( "\n----------------Question 2---------------\n")
plt.plot(time,W)
plt.title('EVOLUTION OF WEALTH')
plt.ylabel('W')
plt.xlabel('Time')
plt.show()

plt.plot(time,P)
plt.title('EVOLUTION OF PRICE')
plt.ylabel('P')
plt.xlabel('Time')
plt.show()

""" QUESTION 3 : Choose a couple of other strategies and see the corresponding revenues. """


def Wealth1(P):
    W=P**2
    return W

print( "\n----------------Question 3: other strategies---------------\n")

# 1st Strategy: P is constant
    
print( "\n 1ST STRATEGY : P=0.5 \n")
P1 = np.array([0.5 for i in range(0,T)])
W1=Wealth1(P1)

plt.plot(time,W1)
plt.title('EVOLUTION OF WEALTH')
plt.ylabel('W')
plt.xlabel('Time')
plt.show()

plt.plot(time,P1)
plt.title('EVOLUTION OF PRICE')
plt.ylabel('P')
plt.xlabel('Time')
plt.show()
    
# 2nd Strategy: P is inscreasing

print( "\n 2ND STRATEGY : P IS INCREASING \n")
P2=np.linspace(0,1,T)

W2=Wealth1(P2)
print (np.where(W2==max(W2)))

plt.plot(time,W2)
plt.title('EVOLUTION OF WEALTH')
plt.ylabel('W')
plt.xlabel('Time')
plt.show()

plt.plot(time,P2)
plt.title('EVOLUTION OF PRICE')
plt.ylabel('P')
plt.xlabel('Time')
plt.show()


# 3rd Strategy: P is decreasing

print( "\n 3RD STRATEGY : P IS DECREASING \n")

P3=np.ones((T,1))

for i in range (0,T):
    P3[i]=P3[i-1]-1/(T-1)

W3=Wealth1(P3)

plt.plot(time,W3)
plt.title('EVOLUTION OF WEALTH')
plt.ylabel('W')
plt.xlabel('Time')
plt.show()

plt.plot(time,P3)
plt.title('EVOLUTION OF PRICE')
plt.ylabel('P')
plt.xlabel('Time')
plt.show()

# 4th strategy : P is Random

print( "\n 4TH STRATEGY : P IS RANDOM\n")
P4=np.zeros((T,1))
for i in range (0,T):
    P4[i]=random.uniform(0,1)

W4=Wealth1(P4)
plt.figure(figsize=(14,7))

plt.plot(time,W4)
plt.title('EVOLUTION OF WEALTH')
plt.ylabel('W')
plt.xlabel('Time')
plt.show()

plt.figure(figsize=(14,7))
plt.plot(time,P4)
plt.title('EVOLUTION OF PRICE')
plt.ylabel('P')
plt.xlabel('Time')
plt.show()


print("\n")
print ("-------------------COMPARISON--------------------")
print("\n")

print ("      WITH BELLMAN       ")
print("\nThe max of optimal cumulative reward is:" , max(W))
print("The max is reached at this index:",np.where(W==max(W)))

print("\n")

print ("      WITH P=0.25       ")
print("\nThe max of optimal cumulative reward is:",max(W1))
print("The max is reached at this index:",0)

print("\n")

print ("      WITH P INCREASING      ")
print("\nThe max of optimal cumulative reward is:", max(W2))
print("The max is reached at this index:",np.where(W2==max(W2)))

print("\n")

print ("      WITH P DECREASING      ")
print("\nThe max of optimal cumulative reward is:",max(W3))
print("The max is reached at this index:",np.where(W3==max(W3)))

print("\n")

print ("      WITH P RANDOM      ")
print("\nThe max of optimal cumulative reward is:",max(W4))
print("The max is reached at this index:",np.where(W4==max(W4)))











