# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:24:19 2021

@author: Zaiba Farheen
MATHEMATICS-PAPER 6
EXPERIMENT-04
EVALUATION OF DOUBLE INTEGRAL WITH VARIABLE LIMITS
"""
#%%
#ques1
from scipy import integrate
def f(x, y):
    return x*y
def limits_y(x):
    return [0, x]
def limits_x():
   return [1, 4]
ans,err=integrate.nquad(f, [limits_y, limits_x])
print(round(ans,3))
#%%
#alt=ques2
from sympy import*
x,y=symbols('x,y')
ans=integrate(1,(x,0,sqrt(1-y**2)),(y,0,3/5))
print(round(ans,3))
#%%
#altqes1
from sympy import*
x,y=symbols('x,y')
ans=integrate(x*y,(y,0,x),(x,1,4))
print(ans)
#%%
#ques2
from scipy import integrate
def f(x, y):
    return 1
def limits_y(x):
    return [0, (1-x**2)**0.5]
def limits_x():
   return [0,3/5]
ans,err=integrate.nquad(f, [limits_y, limits_x])
print(round(ans,3))
#%%
#ques3
import math
from sympy import *
from scipy import integrate
a=1
def f(x, y):
    return (a**2-y**2-x**2)**0.5
def limits_x(y):
   return [0, (a**2-y**2)**0.5]
def limits_y():
    return [0,a]
ans,err=integrate.nquad(f, [limits_x, limits_y])
print(round(ans,3))
#print(ans)
#%%
#ques4
from sympy import*
from scipy import integrate
def f(x, y):
    return exp(x/y)
def limits_x(y):
   return [0,y]
def limits_y():
    return [0, 1]
ans,err=integrate.nquad(f, [limits_x, limits_y])
print(round(ans,3))
#%%
#ques5
from scipy import integrate
def f(x, y):
    return ((y/x)*exp(x))
def limits_y(x):
    return [x**2,x**0.5]
def limits_x():
   return [0,1]
ans,err=integrate.nquad(f, [limits_y, limits_x])
print(round(ans,3))

