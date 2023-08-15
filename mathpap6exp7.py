# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:28:23 2021

@author: Zaiba Farheen
EXPERIMENT-07
CLCULUS OF VARIATIONS
EULER'S EQUATION
"""
#%%
#ques1
from sympy import Symbol,Function,diff,dsolve
f=Function('f')
x=Symbol("x")
y=Symbol("y")
y1=f(x).diff(x)
def F(x,y,y1):
    return 12*x*y + (y1)**2
Fy=diff(F(x,y,y1),y)
Fy1=diff(F(x,y,y1),y1)
ddx=diff(Fy1,x)
eq=Fy-ddx
Sol=dsolve(eq,f(x),ics={f(0):3,f(1):6})
print("Extremal of the given functional is y=",Sol.rhs)
#%%
#ques2
from sympy import Symbol,Function,diff,dsolve,sin,pi
f=Function('f')
x=Symbol("x")
y=Symbol("y")
y1=f(x).diff(x)
def F(x,y,y1):
    return 2*sin(x)*y+(y1)**2
Fy=diff(F(x,y,y1),y)
Fy1=diff(F(x,y,y1),y1)
ddx=diff(Fy1,x)
eq=Fy-ddx
Sol=dsolve(eq, f(x),ics={f(0):0,f(pi):0})
print("Extremal of the given functional is y=",Sol.rhs)
#%%
#ques3
from sympy import Symbol,Function,diff,dsolve,sqrt
f=Function('f')
x=Symbol("x")
y=Symbol("y")
y1=f(x).diff(x)
def F(x,y,y1):
    return sqrt(1+(y1)**2)
Fy=diff(F(x,y,y1),y)
Fy1=diff(F(x,y,y1),y1)
ddx=diff(Fy1,x)
eq=Fy-ddx
Sol=dsolve(eq, f(x),ics={f(0):1,f(1):2})
print("Extremal of the given functional is y=",Sol.rhs)
#%%
#ques4
from sympy import Symbol,Function,diff,dsolve
f=Function('f')
x=Symbol("x")
y=Symbol("y")
y1=f(x).diff(x)
def F(x,y,y1):
    return x+y+(y1)**2
Fy=diff(F(x,y,y1),y)
Fy1=diff(F(x,y,y1),y1)
ddx=diff(Fy1,x)
eq=Fy-ddx
Sol=dsolve(eq, f(x),ics={f(0):1,f(1):2})
print("Extremal of the given functional is y=",Sol.rhs)


