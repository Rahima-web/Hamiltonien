#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:21:23 2020

@author: rahimamohamed

GROUPE : Rahima Mohamed, Mahisha Uruthirasigamani, Danush Chandrarajah  

PROBLEM : You look for a parking space on the street. Each space is free with probability p = 1 − q. 
You cannot tell if a space is free until you reach it. You can not go backward. Once at a space, 
you must decide to stop or to continue. 
From position s (i.e., s spaces from your destination), the cost of stopping is s. 
The cost of passing your destination without parking is D. Construct the strategy
that will return the optimal parking space for a destination.

Note: Fix yourself (at your will) the values that you need to solve the problem

"""

import random as rd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

""" VARIABLE DECLARATION """

#number of parkinks

N = 3
p_max = 0.5
p_min = 0.2
size_min=40
size_max=300

""" QUESTION 1 : Generate several maps with different parking-space distributions. """

def Parking_Creation():
    #  The probability p that a qpace is free :
    p = rd.uniform(p_max,p_min)
    
    # Define the size of the parking :
    size = int(rd.uniform(size_min,size_max))
     
    # Create the parking : x=0 => space is not free && x=1 => space is free :
    availability  = rd.choices([0,1] , [1-p,p] , k=size)
    
    return availability,p,size


def create_all_parkings(n):
#    print("veuillez entrer le nombre de parking souhaité")
#    n=input()
#    n=int(n)
    Liste_of_Parking=[]
    for i in range(0,n):
        Liste_of_Parking.append(Parking_Creation())
    return Liste_of_Parking


""" QUESTION 2 : Implement the parking strategy shown in class for the generated maps."""

def Parking_Strategy(availability,p,size):
    D = size+1 #Cost of passing your destination without parking
    S,X,STOP,A = [],[],[],[]    #S: space; X: availability, STOP : cost of stopping; A: action to do 
    for index,x in enumerate(availability) :
        s = size-index    #space number
        S += [s]
        X += [x]
        if x==0:
            STOP += [float('nan')] #the space is not free
            A += ['Continue']
        else :
            stop = (D*p+1) * ((1-p)**s)
            STOP += [stop]  
            if  stop >= 1:
                A += ['PARKING']
                return S,X,STOP,A
            else:
                A += ['Continue']
                

def All_parking_strategy():
    H=[]
    L=create_all_parkings(N)
    for i in range (0,len(L)):
        H.append(Parking_Strategy(L[i][0],L[i][1],L[i][2]))
        
    return H


""" QUESTION 3 : Discuss your results. """


sns.set_style('darkgrid')

def traces(X,Y):
    plt.scatter(X,Y)
    plt.plot(X,[1]*len(X), 'b--')
    #plt.xlim(X[len(X)-40], 0)  # decreasing S
    plt.title('STOP CONTROLLER EVOLUTION AS A FUNCTION OF PLACE S')
    plt.xlabel('S')
    plt.ylabel('STOP CONTROLER VALUE')
    plt.tight_layout()
    plt.show()
                
###############################################################################

L=create_all_parkings(N)
for i in range(0,len(L)):
    print ("              \nPARKING NUMBER :",(i+1),"\n")
    L=create_all_parkings(N)
    H=All_parking_strategy()
    traces(H[i][0],H[i][2])
    








