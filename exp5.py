# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 09:26:35 2022

@author: Zaiba Farheen
MATHEMATICS PAPER 7
EXP 5
MATRIX REPRESENTATION OF A LINEAR TRANSFORMATION
"""
#%%
#ques1
from sympy import *
import sympy as sym
x,y=symbols("x,y")
import numpy as np 
def T(x):
    x_new=0   
    x,y=x[0],x[1]   
    x_new=np.array([2*x+3*y,4*x-5*y])   
    return simplify(x_new)
u1=np.array([1,0])
u2=np.array([0,1])
v1=np.array([1,0])
v2=np.array([0,1])
eq0=np.array([v1[0]*x,v2[0]*y])
eq1=np.array([v1[1]*x,v2[1]*y])
print(eq0,eq1)
a0=np.array([T(u1)[0],T(u2)[0]])
a1=np.array([T(u1)[1],T(u2)[1]])
print(a0[0]*x+a0[1]*y  ,'and',a1[0]*x+a1[1]*y)
print("The matrix of linear transformation is A ",Matrix([a0,a1]))

#%%
#ques2
print(2)
from sympy import*
import sympy as sym
x,y,z=symbols("x,y,z")
import numpy as np 
def T(x):
    x_new=0   
    x,y,z=x[0],x[1],x[2] 
    x_new=np.array([x-y+z , 2*x+3*y-z/2 , x+y-2*z])   
    return simplify(x_new)
u1=np.array([-1,1,0])
u2=np.array([5,-1,2])
u3=np.array([1,2,1])
v1=np.array([1,1,0])
v2=np.array([0,0,1])
v3=np.array([1,5,2])
Eq0=np.array([v1[0]*x , v2[0]*y , v3[0]*z])
Eq1=np.array([v1[1]*x , v2[1]*y , v3[1]*z])
Eq2=np.array([v1[2]*x , v2[2]*y , v3[2]*z])
eq0=Eq0[0] + Eq0[1] + Eq0[ 2]
eq1=Eq1[0] + Eq1[1] + Eq1[2]
eq2=Eq2[0] + Eq2[1] + Eq2[2]
print(eq0,eq1,eq2)
a0=np.array([T(u1)[0] , T(u2)[0] , T(u3)[0]])
a1=np.array([T(u1)[1] , T(u2)[1] , T(u3)[1]] )
a2=np.array([T(u1)[2] , T(u2)[2] , T(u3)[2]] )
print(a0,a1,a2)
sol0=solve((eq0-a0[0] ,eq1-a1[0] , eq2-a2[0]),x,y,z ,rational=True)
sol1=solve((eq0-a0[1] ,eq1-a1[1] , eq2-a2[1]),x,y,z ,rational=True)
sol2=solve((eq0-a0[2] ,eq1-a1[2] , eq2-a2[2]),x,y,z ,rational=True)
print(sol0 ,"\n", sol1 ,"\n" ,sol2)
#%%
#ques3
from sympy import*
import sympy as sym
x,y,z=symbols("x,y,z")
import numpy as np 
def T(x):
    x_new=0   
    x,y=x[0],x[1]
    x_new=np.array([-x+2*y,y,-3*x+3*y])   
    return (x_new)
u1=np.array([1,2])
u2=np.array([-2,1])
v1=np.array([-1,0,2])
v2=np.array([1,2,3])
v3=np.array([1,-1,-1])

Eq0=np.array([v1[0]*x , v2[0]*y , v3[0]*z])
Eq1=np.array([v1[1]*x , v2[1]*y , v3[1]*z])
Eq2=np.array([v1[2]*x , v2[2]*y , v3[2]*z])
eq0=Eq0[0] + Eq0[1] + Eq0[2]
eq1=Eq1[0] + Eq1[1] + Eq1[2]
eq2=Eq2[0] + Eq2[1] + Eq2[2]
print(eq0,eq1,eq2)

a0=np.array([T(u1)[0] , T(u2)[0]])
a1=np.array([T(u1)[1] , T(u2)[1]])
a2=np.array([T(u1)[2] , T(u2)[2]])
print(a0,a1,a2)
sol0=solve((eq0-a0[0] ,eq1-a1[0] , eq2-a2[0]),x,y,z,rational=True)
sol1=solve((eq0-a0[1] ,eq1-a1[1] , eq2-a2[1]),x,y,z,rational=True)

print("The matrix of linear transformation is A ",Matrix([sol0,sol1]))
#%%
#ques4
from sympy import *
import sympy as sym
x,y,z=symbols("x,y,z")
import numpy as np 
def T(x):
    x_new=0   
    x,y,z=x[0],x[1],x[2] 
    x_new=np.array([x+y,y+z])
    return (x_new)
u1=np.array([1,1,0])
u2=np.array([1,0,1])
u3=np.array([1,1,-1])
v1=np.array([2,-3])
v2=np.array([1,4])
Eq0=np.array([v1[0]*x , v2[0]*y ])
Eq1=np.array([v1[1]*x , v2[1]*y ])
eq0=Eq0[0] + Eq0[1]
eq1=Eq1[0] + Eq1[1] 
print(eq0,eq1)
a0=np.array([T(u1)[0] , T(u2)[0] , T(u3)[0]])
a1=np.array([T(u1)[1] , T(u2)[1] , T(u3)[1]] )
print(a0,a1)
sol0=solve((eq0-a0[0] ,eq1-a1[0] ),x,y,z,rational=True)
sol1=solve((eq0-a0[1] ,eq1-a1[1] ),x,y,z,rational=True)
sol2=solve((eq0-a0[2] ,eq1-a1[2]),x,y,z,rational=True)
print(sol0 ,"\n", sol1 ,"\n",sol2 )