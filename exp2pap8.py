# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 08:37:41 2022

@author: Zaiba Farheen
MATH PAPER-8
EXP-2
REGULA FALSI METHOD
"""
#%%
#ques1
def f(x):
    return x**3+2*x**2-3*x-1
def RegulaFalsi(a,b):
    if(f(a)*f(b))>=0:
        print("Incorrect assumption of a and b")
        return
    c=a
    for i in range(10):
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        if f(c)==0:
            break
        elif f(c)*f(a)<0:
            b=c
            print(c)
        else:
            a=c
            print(c)
    print("Value of the root =",'%.4f'%c)
        
a=1
b=2
RegulaFalsi(a,b)
#%%
#ques2
def f(x):
    return x**3-100
def RegulaFalsi(a,b):
    if(f(a)*f(b))>=0:
        print("Incorrect assumption of a and b")
        return
    c=a
    for i in range(5):
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        if f(c)==0:
            break
        elif f(c)*f(a)<0:
            b=c
            print(c)
        else:
            a=c
            print(c)
    print("Value of the root =",'%.4f'%c)
        
a=4
b=5
RegulaFalsi(a,b)
#%%
#ques3
from math import log10
def f(x):
    return 2*x-log10(x)-7
def RegulaFalsi(a,b):
    if(f(a)*f(b))>=0:
        print("Incorrect assumption of a and b")
        return
    c=a
    for i in range(5):
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        if f(c)==0:
            break
        elif f(c)*f(a)<0:
            b=c
            print(c)
        else:
            a=c
            print(c)
    print("Value of the root =",'%.4f'%c)
        
a=2
b=3
RegulaFalsi(a,b)