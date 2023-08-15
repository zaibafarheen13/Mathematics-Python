# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:07:03 2021

@author: Zaiba Farheen
EXPERIMENT-08

"""
#%%
#ques1
from sympy import Symbol,Function,dsolve,diff
y=Function('y')
x=Symbol('x')
k=Symbol('k')
f=Function('f')
y=f(x)
y1=f(x).diff(x)
def F(y,y1):
    return (y*(1+y1**2))**0.5
dfy1=diff(F(y,y1),y1)
eq=F(y,y1)-y1*dfy1-k
solve=dsolve(eq,f(x))
a=solve[2]
print("Extremal of the given functional is y=",a.rhs)
#%%
#ques2
from sympy import Symbol,Function,dsolve,diff
x=Symbol('x')
f=Function('f')
y=Symbol('y')
k=Symbol('k')
y1=f(x).diff(x)
def F(x,y1):
    return x**-3*y1**2
dfy1=diff(F(x,y1),y1)
eq=dfy1-k
solve=dsolve(eq,f(x))
print("y=",solve.rhs)
#%%
from sympy import Symbol,Function,diff,solve
x=Symbol('x')
y=Symbol('y')
f=Function('f')
y1=f(x).diff(x)
def F(x,y):
    return x**2+y**2
dfy=diff(F(x,y),y)
eq=dfy
sol=solve(eq,y)
print("y=",sol)