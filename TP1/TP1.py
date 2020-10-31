#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:33:37 2020

@author: rahimamohamed
"""

import numpy as np
import pandas as pd

" Variable declaration " 

r=0.05 # Interest rate
T=50 #Maturity
X = [] # le capital investit
W = [] # l'optimal cumulative reward
A = [] # l'action au temps t
Ro = [] # Cumulative reward

" Bang Bang Controller " 

def BangBang_Controller():
    Bang=1
    for i in range (1,T):
        if r>= 1/Bang:
            Bang=(1+r) * Bang
        if r< 1/Bang:
            Bang = 1 + Bang
    return Bang

#x = BangBang_Controller()
#print(x)