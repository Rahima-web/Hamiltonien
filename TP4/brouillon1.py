#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:44:44 2020

@author: rahimamohamed
"""
import random as rd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

n=3

def create_parking():
    # Define probability p of a place is free :
    p = rd.uniform(0.5,0.3)
    
    # Define the size of the parking :
    size = int(rd.uniform(40,300))
     
    # Create the parking : x=0 => occupied / x=1 => free :
    parking = rd.choices([0,1] , [1-p,p] , k=size)
    
    return parking,p,size


def nb_park(n):
#    print("veuillez entrer le nombre de parking souhaité")
#    n=input()
#    n=int(n)
    Liste_Parking=[]
    for i in range(0,n):
        Liste_Parking.append(create_parking())
    return Liste_Parking
        
#
#P1= create_parking()
#P2=create_parking()
#P3=create_parking()

L=nb_park(n)

#Free =[]
#Not_Free =[]
#for i in range (0, len(L[0][0])):
#    if L[0][0][i]==1:
#        Free.append(L[0][0][i])
#    if L[0][0][i]==0:
#        Not_Free.append(L[0][0][i])
#
#X= [i for i in range (0,L[0][2])]
#plt.scatter(X,L[0][0])
#plt.plot(X[L[0][2]-40],L[0][0],colour = 'blue')
#plt.xlim(X[len(X)-40], 0)
#plt.tight_layout()
#plt.show()



def se_garer(parking,p,size):
    D = size+1
    S,X,STOP,A = [],[],[],[]    
    for index,x in enumerate(parking) :
        s = size-index    
        S += [s]
        X += [x]
        if x==0:
            STOP += [float('nan')]
            A += ['Continue']
        else :
            stop = (D*p+1) * ((1-p)**s)
            STOP += [stop]  
            if  stop >= 1:
                A += ['Se gare']
                return S,X,STOP,A
            else:
                A += ['Continue']
                

def h():
    H=[]
    for i in range (0,len(L)):
        H.append(se_garer(L[i][0],L[i][1],L[i][2]))
        
    return H
H=h()
        

#se_garer(P1[0],P1[1],P1[2])
#se_garer(P2[0],P2[1],P2[2])
#se_garer(P3[0],P3[1],P3[2])


sns.set_style('darkgrid')

def traces(X,Y):
    plt.scatter(X,Y)
    plt.plot(X,[1]*len(X), 'b--')
    plt.xlim(X[len(X)-40], 0)  # decreasing S
    plt.title('Évolution du stop-controleur en fonction de S')
    plt.xlabel('S')
    plt.ylabel('Valeur du stop-controleur')
    plt.tight_layout()
    plt.show()
                
###############################################################################

for i in range(0,len(L)):
    L=nb_park(n)
    H=h()
    traces(H[i][0],H[i][2])
    
    
    
    
#if __name__ == '__main__':
#    
#    park,p,s = create_parking()
#    S,X,Stop,Action = se_garer(park,p,s)
#    
#    df = pd.DataFrame({'S':S,'État (x)':X,'Stop Controleur':Stop,'Action':Action})
#    traces(S,Stop)
    
    
    
    
    
    
