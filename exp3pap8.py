# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 08:31:29 2022

@author: Zaiba Farheen
"""
#%%
#ques1
def f(x):
    return x**2-12
def df(x):
    return 2*x
def newtonRaphson(x):
    h=f(x)/df(x)
    while abs(h)>=0.0001:
        h=f(x)/df(x)
        x=x-h
        print(x)
        print("the value of the root is:","%.4f"%x)
x0=3.5
newtonRaphson(x0)
#%%
#ques2
def f(x):
    return x**3+3*x-1
def df(x):
    return 3*x**2+3
def newtonRaphson(x):
    h=f(x)/df(x)
    while abs(h)>=0.0001:
        h=f(x)/df(x)
        x=x-h
        print(x)
        print("the value of the root is:","%.4f"%x)
x0=0.5
newtonRaphson(x0)
#%%
#ques3 with sec
from math import tan
from sympy import sec
#or from sympy import sec,tan
def f(x):
    return tan(x)-x
def df(x):
    return (sec(x)**2)-1
def newtonRaphson(x):
    h=f(x)/df(x)
    while abs(h)>=0.0001:
        h=f(x)/df(x)
        x=x-h
        print(x)
        print("the value of the root is:","%.4f"%x)
x0=4.5
newtonRaphson(x0)

#ques3 with cos
from math import tan,cos
def f(x):
    return tan(x)-x
def df(x):
    return (1/(cos(x)**2))-1
def newtonRaphson(x):
    h=f(x)/df(x)
    while abs(h)>=0.0001:
        h=f(x)/df(x)
        x=x-h
        print(x)
        print("the value of the root is:","%.4f"%x)
x0=4.5
newtonRaphson(x0)
