# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:13:59 2021

@author: Zaiba Farheen
MATHEMATICS-PAPER 5
EXPERIMENT-03
NUMERICAL METHODS- SIMPSON'S 1/3RD RULE
"""
#%%
#ques1
from sympy import log
def f(x):
    return log(x)
a=4
b=5.2
n=6
def simpsons(a,b,n):
    h=(b-a)/n
    x=list()
    fx=list()
    i=0
    while i<=n:
        x.append(a+i*h)
        fx.append(f(x[i]))
        i+=1
#calculating result
    ans=0
    i=0
    while i<=n:
        if i==0 or i==n:
            ans+=fx[i]
        elif i%2!=0:
            ans+=4*fx[i]
        else:
            ans+=2*fx[i]
        i+=1
    ans=ans*(h/3)
    return ans
print("Value of integral is","%.6f"% simpsons(a,b,n))
#%%
#ques2
def f(x):
    return 1/(1+x**2)
a=0
b=6
n=6
def simpsons(a,b,n):
    h=(b-a)/n
    x=list()
    fx=list()
    i=0
    while i<=n:
        x.append(a+i*h)
        fx.append(f(x[i]))
        i+=1
#calculating result
    ans=0
    i=0
    while i<=n:
        if i==0 or i==n:
            ans+=fx[i]
        elif i%2!=0:
            ans+=4*fx[i]
        else:
            ans+=2*fx[i]
        i+=1
    ans=ans*(h/3)
    return ans
print("Value of integral is","%.6f"% simpsons(a,b,n))
#%%
#ques3
from sympy import exp
def f(x):
    return exp(x)
a=0
b=1
n=4
def simpsons(a,b,n):
    h=(b-a)/n
    x=list()
    fx=list()
    i=0
    while i<=n:
        x.append(a+i*h)
        fx.append(f(x[i]))
        i+=1
#calculating result
    ans=0
    i=0
    while i<=n:
        if i==0 or i==n:
            ans+=fx[i]
        elif i%2!=0:
            ans+=4*fx[i]
        else:
            ans+=2*fx[i]
        i+=1
    ans=ans*(h/3)
    return ans
print("Value of integral is","%.6f"% simpsons(a,b,n))

