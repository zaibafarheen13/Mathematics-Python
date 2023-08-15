# -*- coding: utf-8 -*-
"""
Created on Mon Aug  23 3:00:30 2021

@author: Zaiba Farheen
MATHEMATICS-PAPER 6
EXPERIMENT-02
EVALUATION OF LINE INTEGRAL WITH CHANGE OF VARIABLES
"""
#%%
#ques1
from sympy import * 
import numpy as np 
from sympy import integrate 
x,y,z,t=symbols("x,y,z,t") 
x=exp(t)
y=exp(-t)
z=t**2
F=np.array([x*y,x**2*z,x*y*z]) 
dx=diff(x,t) 
dy=diff(y,t)
dz=diff(z,t)
dr=np.array([dx,dy,dz]) 
I=np.dot(F,dr) 
k=integrate(I,(t,0,1)) 
print(k)
#%%
#ques2
from sympy import * 
import numpy as np 
from sympy import integrate 
x,y,t=symbols("x,y,t") 
a=4
b=3
x=a*cos(t)
y=b*sin(t)
F=np.array([x+2*y,4-2*x]) 
dx=diff(x,t) 
dy=diff(y,t)
dz=diff(z,t)
dr=np.array([dx,dy]) 
I=np.dot(F,dr) 
k=integrate(I,(t,0,2*pi)) 
print(k)
#%%
#ques3
from sympy import * 
import numpy as np 
from sympy import integrate 
x,y,z,t=symbols("x,y,z,t") 
x=t**2+1
y=2*t**2
z=t**3
F=np.array([3*x*y,-5*z,10*x]) 
dx=diff(x,t) 
dy=diff(y,t)
dz=diff(z,t)
dr=np.array([dx,dy,dz]) 
I=np.dot(F,dr) 
k=integrate(I,(t,0,1)) 
print(k)
#%%
#ques4
from sympy import * 
import numpy as np 
from sympy import integrate 
x,y,z,t=symbols("x,y,z,t") 
x=t
y=t
z=t
F=np.array([3*x**2+6*y,-14*y*z,20*x*z**2]) 
dx=diff(x,t) 
dy=diff(y,t)
dz=diff(z,t)
dr=np.array([dx,dy,dz]) 
I=np.dot(F,dr) 
k=integrate(I,(t,0,1)) 
print(k)

