# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 09:25:02 2022

@author: Zaiba Farheen
BISECTION METHOD(BOLZANO METHOD)
"""
#%%
#ques1
def f(x):
    return 10-x**2
def bisection(a,b):
    if(f(a)*f(b)>=0):
        print("Incorrect assumption of a and b")
        return
    c=a
    for i in range(10):
        c=(a+b)/2
        if f(c)==0:
            break
        elif f(c)*f(a)<0:
            b=c
            print(c)
        else:
            a=c
            print(c)
    print("Value of the root =",'%.4f'%c)
        
a=3
b=4
bisection(a,b)
#%% 
#ques2
from math import log10
def f(x):
    return x*log10(x)-1.2
def bisection(a,b):
    if(f(a)*f(b)>=0):
        print("Incorrect assumption of a and b")
        return
    c=a
    for i in range(10):
        c=(a+b)/2
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
bisection(a,b)
#%%        
#ques3
from math import *
def f(x):
    return x-cos(x)-10
def bisection(a,b):
    if(f(a)*f(b)>=0):
        print("Incorrect assumption of a and b")
        return
    c=a
    for i in range(10):
        c=(a+b)/2
        if f(c)==0:
            break
        elif f(c)*f(a)<0:
            b=c
            print(c)
        else:
            a=c
            print(c)
    print("Value of the root =",'%.4f'%c)
        
a=9
b=10
bisection(a,b)