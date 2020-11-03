#testedanushpourrahima
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:33:37 2020

@author: rahimamohamed
"""

"""
GROUPE : Rahima Mohamed, Mahisha Uruthirasigamani, Danush Chandrarajah  

PROBLEM :
    
An investor has a fund. It has 1 million euros at time zero. 
It pays 5% interest per year for T=50 years. 
The investor cannot withdraw the invested money. 
But, (s)he consumes a proportion (at) of the interest at time t and 
reinvests the rest. 
What should the investor do to maximize the consumption before T?

"""

import numpy as np
import matplotlib.pyplot as plt
import random

" VARIABLE DECLARATION " 

# Interest rate
r = 0.05 

# Maturity
T = 50 

# fund at t=0
X_0 = 1000000 

# Invested Capital
X_invest = [] 

# Consumed Capital
X_consum = [] 

# Cumulative Reward/Total consumption

W=0

# Sequence of actions 
A=np.zeros((T,1))


""" QUESTION 1 : Implement the Bang Bang Controller """

##----------------Bang Bang Controller--------------##

def BangBang_Controller():
    rho=1 # value of rho at (T-1)=1
    RHO=[rho]
    A[0]=1 # Valut of a at (T-1) =1
    for i in range (1,T):
        if r>= 1/rho:
            rho=(1+r) * rho
            RHO.append(rho)
            A[i]=0
        if r< 1/rho:
            rho = 1 + rho
            RHO.append(rho)
            A[i]=1
    RHO.reverse() # on reorganise donc la liste des rho
    A[:] = A[::-1] # on reorganise aussi A 
    return RHO,A

print("\n")
print ("--------------- THE SEQUENCE OF ACTIONS a --------------------")

B=BangBang_Controller()
print(B[1])

print("\n")

##----------------The invested capital--------------##

def plant_equation(A):
    X_invest= [X_0]
    for i in range (1,T):
        X_invest.append( X_invest[i-1] + r*X_invest[i-1]*(1-A[i-1]))
    return X_invest



X = plant_equation(B[1]) #B[1] : The sequence of action a

print ("--------------- EVOLUTION OF THE INVESTED CAPITAL--------------------")
print("\n")

print(X)
print("\n")  

time=[i for i in range(0,T)]

plt.plot(time,X,color = 'red')
plt.title('INVESTED CAPITAL EVOLUTION')
plt.ylabel('invested capital')
plt.xlabel('Time')
plt.show()


    
""" QUESTION 2 : Compute the corresponding total consumption and 
find the sequence of optimal actions.
"""

def consumption(A,X):
    X_consum=[]
    S=0
    for i in range (1,T+1):
        X_consum.append(r*X[i-1]*A[i-1])
        S+=X_consum[i-1]
    return X_consum,S

print ("--------------- CONSUMPTION ARRAY--------------------")
print("\n")

C=consumption(B[1],X) #B[1] : The sequence of action a
print(C[0])
print("\n")


print ("--------------- TOTAL CONSUMPTION --------------------")
print("\n")

print(C[1])
print("\n")


    
""" QUESTION 3 : Plot the consumption as a function of time
"""

print ("--------------- EVOLUTION OF CONSUMPTION --------------------")
print("\n")

plt.plot(time,C[0],color= 'green')
plt.title('CONSUMPTION EVOLUTION')
plt.ylabel('consumption')
plt.xlabel('Time')
plt.show()


""" QUESTION 4 : Plot the action sequence as a function of time.
"""

print("\n")
print ("--------------- EVOLUTION OF ACTIONS --------------------")
print("\n")

plt.plot(time,B[1],color = 'purple')
plt.title('PROPORTION (a) EVOLUTION')
plt.ylabel('proportion a')
plt.xlabel('Time')
plt.show()

gama = np.zeros((T,1))
rho= BangBang_Controller()[0]

def gamma():
    
    for i in range(1,T):
        gama[i-1] =  (1+r) * rho[i] + (1+r*rho[i])*A[i-1]
    
    return gama

Y1 = []
Y2 = []
for i in range (0,T):
    Y1.append (1+rho[i]) #a=1
 
for i in range (0,T):
    Y2.append ((1 + r)*rho[i]) #a=0

print("\n")   
print ("--------------- CONSUME AND SAVE --------------------")
print("\n")

G = gamma()
plt.plot(rho,Y1,label = 'Y1',color = 'blue')
plt.plot(rho,Y2, label = 'Y2', color ='magenta')
plt.plot(rho,G, label = 'Gamma', color= 'orange')
plt.legend()
plt.show()



""" QUESTION 5 : Choose a couple of other strategies (controllers) 
to compare their respective total consumption to that obtained using 
the bang-bang approach.
"""

print("\n")
print ("--------------- OTHER STRATEGIES --------------------")
print("\n")

##----------First stratégie: if A is always eaqual to 1----------##

print ("             IF A IS ALWAYS EQUAL TO 1 :             ")
print("\n")


A1=np.ones((T,1))
X1 = plant_equation(A1)

print ("The total consumption is:")
C1=consumption(A1,X1)
print(C1[1])

print("\n")

print ("The total consumption with bang bang controller is:")
C=consumption(B[1],X)

print(C[1])

plt.plot(time,A1,color = 'purple')
plt.title('PROPORTION (a) EVOLUTION')
plt.ylabel('proportion a')
plt.xlabel('Time')
plt.show()


##----------Seconde Stratégie: if A is increasing through the time----------##

print("\n")
print ("             IF A IS INCREASING :             ")
print("\n")

A2= np.arange(0,1,1/(T-1))
X2 = plant_equation(A2)

print ("The total consumption is:")
C2=consumption(A2,X2)

print(C2[1])

print("\n")

print ("The total consumption with bang bang controller is:")
C=consumption(B[1],X)

print(C[1])

plt.plot(time,A2,color = 'purple')
plt.title('PROPORTION (a) EVOLUTION')
plt.ylabel('proportion a')
plt.xlabel('Time')
plt.show()

##----------3rd Stratégie: if A is decreasing through the time----------##

print("\n")
print ("             IF A IS DECREASING :             ")
print("\n")

A3= np.zeros((T,1))
A3[0]=1
A3[T-1]=0
for i in range (1,T-1):
    A3[i]=A3[i-1]-1/(T-1)

X3 = plant_equation(A3)

print ("The total consumption is:")
C3=consumption(A3,X3)

print(C3[1])

print("\n")

print ("The total consumption with bang bang controller is:")
C=consumption(B[1],X)

print(C[1])

plt.plot(time,A3,color = 'purple')
plt.title('PROPORTION (a) EVOLUTION')
plt.ylabel('proportion a')
plt.xlabel('Time')
plt.show()

##----------4th Stratégie: if A is random----------##

print("\n")
print ("             IF A IS RANDOM :             ")
print("\n")

A4=np.zeros((T,1))
for i in range (0,T):
    A4[i]=random.uniform(0,1)
 
X4 = plant_equation(A4)

print ("The total consumption is:")
C4=consumption(A4,X4)

print(C4[1])

print("\n") 

print ("The total consumption with bang bang controller is:")
C=consumption(B[1],X)

print(C[1])

plt.plot(time,A4,color = 'purple')
plt.title('PROPORTION (a) EVOLUTION')
plt.ylabel('proportion a')
plt.xlabel('Time')
plt.show()

##----------5th Stratégie: if A is increasing then deacreasing----------##

print("\n")
print ("             IF A IS INCREASING THEN DECREASING :             ")
print("\n")
A5= np.arange(0,1,1/49)
A5[0]=0

for i in range (25,T):
    A5[i]=abs(A5[i-1]-1/(T-1))
    
A5[T-1]=0

X5 = plant_equation(A5)

print ("The total consumption is:")
C5=consumption(A5,X5)

print(C5[1])

print("\n")

print ("The total consumption with bang bang controller is:")
C=consumption(B[1],X)

print(C[1])

plt.plot(time,A5,color = 'purple')
plt.title('PROPORTION (a) EVOLUTION')
plt.ylabel('proportion a')
plt.xlabel('Time')
plt.show()

##----------6th Stratégie: if A is equal to 0 and 1 at t=T-1----------##

print("\n")
print ("             IF A IS EQUAL TO 0 AND 1 AT t=T-1:             ")
print("\n")

A6=np.zeros((T,1))
A6[T-1]=1

X6 = plant_equation(A6)

print ("The total consumption is:")
C6=consumption(A6,X6)

print(C6[1])

print("\n")

print ("The total consumption with bang bang controller is:")
C=consumption(B[1],X)

print(C[1])

plt.plot(time,A6,color = 'purple')
plt.title('PROPORTION (a) EVOLUTION')
plt.ylabel('proportion a')
plt.xlabel('Time')
plt.show()









