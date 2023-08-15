# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 09:10:54 2022

@author: Zaiba Farheen
MATHEMATICS PAPER-7
EXPERIMENT-04
"""
#%%
#QUES1
from sympy import *
k,a,b,c,d=symbols("k,a,b,c,d")
import numpy as np 
def transform(x):
    x_new=0   
    x,y=x[0],x[1]    
    x_new=np.array([x+y,x])   
    return simplify(x_new)
u1=np.array([a,b]) 
u2=np.array([c,d])
a1=transform(u1 + u2)
print("T(u[1])+T(u[2]) = ",a1)
a2=transform(u1)+transform(u2)
print("T(u[1]+u[2]) = ",a2)
p1=transform(k*u1)
print("T(k*u[1]) = ",p1)
p2=k*transform(u1)
print("k*T(u[1]) = ",p2)
if(a1==a2) and (p1==p2):
    print("The given mapping is a linear transformation")
else:
    print("The given mapping is not a linear transformation")
#%%
#ques2
from sympy import *
k,a,b,c,d,e,f=symbols("k,a,b,c,d,e,f")
import numpy as np 
def transform(x):
    x_new=0   
    x,y,z=x[0],x[1],x[2]   
    x_new=np.array([x**3+x*y,x*y,y*z])   
    return simplify(x_new)
u1=np.array([a,b,c]) 
u2=np.array([d,e,f])
a1=transform(u1 + u2)
print("T(u[1])+T(u[2]) = ",a1)
a2=transform(u1)+transform(u2)
print("T(u[1]+u[2]) = ",a2)
p1=transform(k*u1)
print("T(k*u[1]) = ",p1)
p2=k*transform(u1)
print("k*T(u[1]) = ",p2)
if(a1==a2) and (p1==p2):
    print("The given mapping is a linear transformation")
else:
    print("The given mapping is not a linear transformation")
#%%
#ques3
from sympy import *
a,b,c,d,e,f,k=symbols("a,b,c,d,e,f,k")
import numpy as np 
def transform(x):
    x_new=0   
    x,y,z=x[0],x[1],x[2]   
    x_new=np.array([x+2*y-3*z,4*x-5*y+6*z])   
    return simplify(x_new)
u1=np.array([a,b,c]) 
u2=np.array([d,e,f])
a1=transform(u1 + u2)
print("T(u[1])+T(u[2]) = ",a1)
a2=transform(u1)+transform(u2)
print("T(u[1]+u[2]) = ",a2)
p1=transform(k*u1)
print("T(k*u[1]) = ",p1)
p2=k*transform(u1)
print("k*T(u[1]) = ",p2)
if(a1==a2) and (p1==p2):
    print("The given mapping is a linear transformation")
else:
    print("The given mapping is not a linear transformation")
#%%
#ques4
from sympy import * 
a,b,c,d,e,f,k=symbols("a,b,c,d,e,f,k") 
import numpy as np 
def transform(x): 
  x_new=0 
  x,y=x[0],x[1] 
  x_new=np.array([x+3,2*y,x+y]) 
  return simplify(x_new) 
u1=np.array([a,b]) 
u2=np.array([c,d]) 
a1=transform(u1 + u2) 
print("T(u[1])+T(u[2]) = ",a1) 
a2=transform(u1)+transform(u2) 
print("T(u[1]+u[2]) = ",a2) 
p1=transform(k*u1) 
print("T(k*u[1]) = ",p1) 
p2=k*transform(u1) 
print("k*T(u[1]) = ",p2) 
if(a1==a2) and (p1==p2): 
  print("The given mapping is a linear transformation") 
else: 
  print("The given mapping is not a linear transformation")