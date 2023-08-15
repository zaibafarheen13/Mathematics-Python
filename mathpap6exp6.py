# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:34:05 2021

@author: Zaiba Farheen
EXPERIMENT-06
EVALUATION OF TRIPLE INTEGRAL WITH VARIABLE LIMITS
"""
#%%
#ques1
from scipy import integrate
def f(x, y,z):
    return x + y + z
def limits_y(x,z):
    return [x-z,x+z]
def limits_x(z):
    return [0, z]
def limits_z():
    return [-1, 1]
ans,err=integrate.nquad(f, [limits_y, limits_x, limits_z])
print(round(ans,3))
#ALTERNATEques1
from sympy import*
x,y,z=symbols('x,y,z')
ans=integrate(x+y+z,(y,x-z,x+z),(x,0,z),(z,-1,1))
print(round(ans,3))
#%%
#ques2
a=1
from sympy import *
from scipy import integrate
def f(x, y,z):
    return exp(x + y + z)
def limits_z(x,y):
    return [0,x+y]
def limits_y(x):
    return [0,x]
def limits_x():
    return [0, a]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,3))
#ALTERNATEques2
from sympy import*
x,y,z,a=symbols('x,y,z,a')
ans=integrate(exp(x+y+z),(z,0,x+y),(y,0,x),(x,0,a))
print(ans)
#%%
#ques3
from scipy import integrate
def f(x, y,z):
    return x * y * z
def limits_z(x,y):
    return [0,1-x-y]
def limits_y(x):
    return [0,1-x]
def limits_x():
    return [0, 1]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,7))
#%%
#altques3
from sympy import*
x,y,z=symbols('x,y,z')
m=integrate(x*y*z,(z,0,1-x-y))
print(m)
n=integrate(m,(y,0,1-x))
print(n)
o=integrate(n,(x,0,1))
print(o)
ans=integrate(x * y * z,(z,0,1-x-y),(y,0,1-x),(x,0,1))
print(ans)
#%%
#ques4
from sympy import *
from scipy import integrate
a=1
def f(x, y,z):
    return x * y * z
def limits_z(x,y):
    return [0,(a*a-x*x-y*y)**0.5]
def limits_y(x):
    return [0,(a*a-x*x)**0.5]
def limits_x():
    return [0, a]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,6))
from sympy import*
x,y,z,a=symbols('x,y,z,a')
m=integrate(x*y*z,(z,0,(a*a-x*x-y*y)**0.5))
print(m)
n=integrate(m,(y,0,(a*a-x*x)**0.5))
print(n)
o=integrate(n,(x,0,a))
print(o)
ans=integrate(x * y * z,(z,0,(a*a-x*x-y*y)**0.5),(y,0,(a*a-x*x)**0.5),(x,0,a))
print(ans)
#%%
#ques5
from math import pi
from sympy import *
from scipy import integrate
a=1
def f(x, y,z):
    return (a*a-x*x-y*y-z*z)**-(0.5)
def limits_z(x,y):
    return [0,(a*a-x*x-y*y)**0.5]
def limits_y(x):
    return [0,(a*a-x*x)**0.5]
def limits_x():
    return [0, a]
ans,err=integrate.nquad(f, [limits_z, limits_y, limits_x])
print(round(ans,6))
#%%

