# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:21:51 2021

@author: Zaiba Farheen
EXPERIMENT-05
EVALUATION OF TRIPLE INTEGRAL WITH CONSTANT LIMITS
"""
#%%
#ques1
from scipy import integrate
def f(x, y,z):
    return x**2*y*z
def limits_z(x,y):
    return [1,2]
def limits_y(x):
    return [0, 2]
def limits_x():
    return [0, 1]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,3))
#ques1-ALTERNATE METHOD:
from scipy import integrate
def f(x, y,z):
    return x**2*y*z
def limits_z(x,y):
    return [1,2]
def limits_y(x):
    return [0, 2]
def limits_x():
    return [0, 1]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,3))
#%%
#ques2
from sympy import *
from scipy import integrate
def f(x, y,z):
    return exp(x+y+z)
def limits_z(x,y):
    return [0,1]
def limits_y(x):
    return [0, 1]
def limits_x():
    return [0, 1]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,3))
#ques2-ALTERNATE METHOD:
from scipy import integrate
def f(x, y,z):
    return exp(x+y+z)
def limits_z(x,y):
    return [0,1]
def limits_y(x):
    return [0, 1]
def limits_x():
    return [0, 1]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,3))
#%%
#ques3
from sympy import *
from scipy import integrate
def f(x, y,z):
    return x**2*y**2*z**2
def limits_z(x,y):
    return [0,1]
def limits_y(x):
    return [0, 1]
def limits_x():
    return [0, 1]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,3))
#ques3-ALTERNATE METHOD:
from scipy import integrate
def f(x, y,z):
    return x**2*y**2*z**2
def limits_z(x,y):
    return [0,1]
def limits_y(x):
    return [0, 1]
def limits_x():
    return [0, 1]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,3))
#%%
#ques4
from sympy import *
from scipy import integrate
def f(x, y,z):
    return (x/y+y/z+z/x)
def limits_z(x,y):
    return [1,2]
def limits_y(x):
    return [1,2]
def limits_x():
    return [1,2]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,3))
#ques4-ALTERNATE METHOD:
from scipy import integrate
def f(x, y,z):
    return (x/y+y/z+z/x)
def limits_z(x,y):
    return [1,2]
def limits_y(x):
    return [1,2]
def limits_x():
    return [1,2]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,3))

