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

""" VARIABLE DECLARATION """

#number of parkinks

N = 3
#p_max = 0.5
#p_min = 0.2
#size_min=40
#size_max=300
p=0.3
#size = 400

""" QUESTION 1 : Generate several maps with different parking-space distributions. """

def Parking_Creation(size,p):
    #  The probability p that a qpace is free :
    #p = rd.uniform(p_max,p_min)
    
    # Define the size of the parking :
    #size = int(rd.uniform(size_min,size_max))
     
    # Create the parking : x=0 => space is not free && x=1 => space is free :
    availability  = rd.choices([0,1] , [1-p,p] , k=size)
    
    return availability,p,size


def create_all_parkings(n,p):
#    print("veuillez entrer le nombre de parking souhaité")
#    n=input()
#    n=int(n)
    Liste_of_Parking=[]
    size=50
    #p=0.1
    for i in range(0,n):
        Liste_of_Parking.append(Parking_Creation(size,p))
        size+=100
        #p+=0.4  
    return Liste_of_Parking

#L=create_all_parkings(3,0.1)

    
    


""" QUESTION 2 : Implement the parking strategy shown in class for the generated maps."""

def Parking_Strategy(availability,p,size):
    D = size+50 #Cost of passing your destination without parking
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
                

def All_parking_strategy(n,p):
    H=[]
    L=create_all_parkings(n,p)
    for i in range (0,len(L)):
        H.append(Parking_Strategy(L[i][0],L[i][1],L[i][2]))
        
    return H

H=All_parking_strategy(N,p)
for i in range (0,len(H[0][3])):
    if H[0][3][i]=='PARKING':
        print("the index is:",i)

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
                
print("\n--------------------COMPARISON: FOR DIFFERENT P AND SIZE------------------\n")

""" pour p =0.1 """

print("                      -----------IF P=0.1-----------                 \n")
p=0.1
L=create_all_parkings(N,p)
H=All_parking_strategy(N,p)
for i in range(0,len(L)):
    print ("              \nPARKING NUMBER :",(i+1)," , WITH SIZE:",L[i][2],"\n")
#    L=create_all_parkings(N,p)
#    H=All_parking_strategy(N,p)
    traces(H[i][0],H[i][2])
    for j in range (0,len(H[i][3])):
        if H[i][3][j]=='PARKING':
            print("\n The parking place is:",j+1,"\n")
    
    


""" pour p =0.5 """
print("  \n                    -----------IF P=0.5-----------                   \n")
p=0.5
L=create_all_parkings(N,p)
H=All_parking_strategy(N,p)
for i in range(0,len(L)):
    print ("              \nPARKING NUMBER :",(i+1)," , WITH SIZE:",L[i][2],"\n")
#    L=create_all_parkings(N,p)
#    H=All_parking_strategy(N,p)
    traces(H[i][0],H[i][2])
    for j in range (0,len(H[i][3])):
        if H[i][3][j]=='PARKING':
            print("\n The parking place is:",j+1,"\n")

""" pour p =0.9 """
print(" \n                              -----------IF P=0.9-----------         \n")
p=0.9
L=create_all_parkings(N,p)
H=All_parking_strategy(N,p)
for i in range(0,len(L)):
    print ("              \nPARKING NUMBER :",(i+1)," , WITH SIZE:",L[i][2],"\n")
#    L=create_all_parkings(N,p)
#    H=All_parking_strategy(N,p)
    traces(H[i][0],H[i][2])
    for j in range (0,len(H[i][3])):
        if H[i][3][j]=='PARKING':
            print("\n The parking place is:",j+1)
    

    
    















#n=3
#
#def create_parking():
#    # Define probability p of a place is free :
#    p = rd.uniform(0.5,0.3)
#    
#    # Define the size of the parking :
#    size = int(rd.uniform(40,300))
#     
#    # Create the parking : x=0 => occupied / x=1 => free :
#    parking = rd.choices([0,1] , [1-p,p] , k=size)
#    
#    return parking,p,size
#
#
#def nb_park(n):
##    print("veuillez entrer le nombre de parking souhaité")
##    n=input()
##    n=int(n)
#    Liste_Parking=[]
#    for i in range(0,n):
#        Liste_Parking.append(create_parking())
#    return Liste_Parking
#        
##
##P1= create_parking()
##P2=create_parking()
##P3=create_parking()
#
#L=nb_park(n)
#
##Free =[]
##Not_Free =[]
##for i in range (0, len(L[0][0])):
##    if L[0][0][i]==1:
##        Free.append(L[0][0][i])
##    if L[0][0][i]==0:
##        Not_Free.append(L[0][0][i])
##
##X= [i for i in range (0,L[0][2])]
##plt.scatter(X,L[0][0])
##plt.plot(X[L[0][2]-40],L[0][0],colour = 'blue')
##plt.xlim(X[len(X)-40], 0)
##plt.tight_layout()
##plt.show()
#
#
#
#def se_garer(parking,p,size):
#    D = size+1
#    S,X,STOP,A = [],[],[],[]    
#    for index,x in enumerate(parking) :
#        s = size-index    
#        S += [s]
#        X += [x]
#        if x==0:
#            STOP += [float('nan')]
#            A += ['Continue']
#        else :
#            stop = (D*p+1) * ((1-p)**s)
#            STOP += [stop]  
#            if  stop >= 1:
#                A += ['Se gare']
#                return S,X,STOP,A
#            else:
#                A += ['Continue']
#                
#
#def h():
#    H=[]
#    for i in range (0,len(L)):
#        H.append(se_garer(L[i][0],L[i][1],L[i][2]))
#        
#    return H
#H=h()
#        
#
##se_garer(P1[0],P1[1],P1[2])
##se_garer(P2[0],P2[1],P2[2])
##se_garer(P3[0],P3[1],P3[2])
#
#
#sns.set_style('darkgrid')
#
#def traces(X,Y):
#    plt.scatter(X,Y)
#    plt.plot(X,[1]*len(X), 'b--')
#    plt.xlim(X[len(X)-40], 0)  # decreasing S
#    plt.title('Évolution du stop-controleur en fonction de S')
#    plt.xlabel('S')
#    plt.ylabel('Valeur du stop-controleur')
#    plt.tight_layout()
#    plt.show()
#                
################################################################################
#
#for i in range(0,len(L)):
#    L=nb_park(n)
#    H=h()
#    traces(H[i][0],H[i][2])
#    
#    
#    
#    
##if __name__ == '__main__':
##    
##    park,p,s = create_parking()
##    S,X,Stop,Action = se_garer(park,p,s)
##    
##    df = pd.DataFrame({'S':S,'État (x)':X,'Stop Controleur':Stop,'Action':Action})
##    traces(S,Stop)
#    
#    
#    
    
    
    
