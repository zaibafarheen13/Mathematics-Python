# -*- coding: utf-8 -*-
"""
Created on Mon Sep  06 03:00:30 2021

@author: Zaiba Farheen
MATHEMATICS-PAPER 6
EXPERIMENT-03
EVALUATION OF DOUBLE INTEGRAL WITH CONSTANT LIMITS
"""
#%% mathpap5exp3
#%%
#qes1
from sympy import*
from scipy import integrate 
def f(x, y): 
  return 1/(1+x+y)
def limits_y(): 
  return [0,1] 
def limits_x(y): 
  return [0,1]
ans,err=integrate.nquad(f, [limits_x,limits_y])
print(round(ans,3))
#%%
#ques2
from sympy import*
from scipy import integrate 
def f(x, y): 
  return x*y+exp(y)
def limits_y(): 
  return [3, 4] 
def limits_x(y): 
  return [1, 2]
ans,err=integrate.nquad(f, [limits_x,limits_y])
print(round(ans,3))
#%%
#ques3
from sympy import*
from scipy import integrate 
def f(x, y): 
  return sin(x)*cos(y)
def limits_y(): 
  return [0,pi/2] 
def limits_x(y): 
  return [0,pi/6]
ans,err=integrate.nquad(f, [limits_x,limits_y])
print(round(ans,3))
#%%
#ques4
from sympy import*
from scipy import integrate 
a=1
b=1
def f(x, y): 
  return (x**2+y**2)
def limits_y(): 
  return [0,b] 
def limits_x(y): 
  return [0,a]
ans,err=integrate.nquad(f, [limits_x,limits_y])
print(round(ans,3))
#Alternate code
#from sympy import *
#x,y,a,b=symbols('x,y,a,b')
#ans=integrate(x**2+y**2,(x,0,a),(y,0,b))
#print(ans)
#%%
#ques4 optional
from sympy import*
x,y,a,b=symbols('x,y,a,b')
ans=integrate(x**2+y**2,(x,0,a),(y,0,b))
print(ans)