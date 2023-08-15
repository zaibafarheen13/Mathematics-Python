# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:48:26 2021

@author: Zaiba Farheen
EXPERIMENT-02 
NUMERICAL INTEGRATION
"""
#%%
#ques1
from sympy import exp
def y(x):
  return exp(x)
def trapezoidal (a,b,n):
  h=(b-a)/n
  s=(y(a)+y(b))
  i=1
  while i<n:
    s+=2*y(a+i*h)
    i+=1
  return (0.5*h*s)
a=0
b=1
n=5
print("Value of integration is","%4f"%trapezoidal(a,b,n))
#%%
#ques2
def y(x):
  return (1/(1+x**2))
def trapezoidal (a,b,n):
  h=(b-a)/n
  s=(y(a)+y(b))
  i=1
  while i<n:
    s+=2*y(a+i*h)
    i+=1
  return (0.5*h*s)
a=0
b=6
n=6
print("Value of integration is","%4f"%trapezoidal(a,b,n))
#%%
#ques3
from sympy import log
def y(x):
  return log(x)
def trapezoidal (a,b,n):
  h=(b-a)/n
  s=(y(a)+y(b))
  i=1
  while i<n:
    s+=2*y(a+i*h)
    i+=1
  return (0.5*h*s)
a=4
b=5.2
n=6
print("Value of integration is","%4f"%trapezoidal(a,b,n))
#%%
#ques4
def y(x):
  return 1/(1+x)
def trapezoidal (a,b,n):
  h=(b-a)/n
  s=(y(a)+y(b))
  i=1
  while i<n:
    s+=2*y(a+i*h)
    i+=1
  return (0.5*h*s)
a=0
b=1
n=8
print("Value of integration is","%4f"%trapezoidal(a,b,n))
#%%
#ques5
def y(x):
  return x**4
def trapezoidal (a,b,n):
  h=(b-a)/n
  s=(y(a)+y(b))
  i=1
  while i<n:
    s+=2*y(a+i*h)
    i+=1
  return (0.5*h*s)
a=-3
b=3
n=6
print("Value of integration is","%4f"%trapezoidal(a,b,n))
#%%
#ques6
def y(x):
  return 1/x
def trapezoidal (a,b,n):
  h=(b-a)/n
  s=(y(a)+y(b))
  i=1
  while i<n:
    s+=2*y(a+i*h)
    i+=1
  return (0.5*h*s)
a=1
b=2
n=2
print("Value of integration is","%4f"%trapezoidal(a,b,n))


