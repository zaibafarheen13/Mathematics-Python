# -*- coding: utf-8 -*-
"""
Created on Mon Aug  16 03:30:30 2021

@author: Zaiba Farheen
MATHEMATICS-PAPER 6
EXPERIMENT-01
LINE INTEGRAL
"""
#%%
#ques1
from sympy import* 
import numpy as np 
from sympy import integrate 
x,y=symbols("x,y") 
y=x**2
F=np.array([-y,x]) 
dx=diff(x,x) 
dy=diff(y,x) 
dr=np.array([dx,dy]) 
I=np.dot(F,dr) 
k=integrate(I,(x,0,1)) 
print(k)
#%%
#ques2
from sympy import* 
import numpy as np 
from sympy import integrate 
x,y=symbols("x,y") 
y=(x**2)+1
F=np.array([3*x+y,2*y-x]) 
dx=diff(x,x) 
dy=diff(y,x) 
dr=np.array([dx,dy]) 
I=np.dot(F,dr) 
k=integrate(I,(x,0,3)) 
print(k)
#%%
#ques3from sympy import* 
import numpy as np 
from sympy import integrate 
x,y=symbols("x,y") 
y=x+1
F=np.array([2*x*y-1,x**2+1]) 
dx=diff(x,x) 
dy=diff(y,x) 
dr=np.array([dx,dy]) 
I=np.dot(F,dr) 
k=integrate(I,(x,0,2)) 
print(k)
#%%
#ques4
from sympy import* 
import numpy as np 
from sympy import integrate 
x,y=symbols("x,y") 
x=y**2
F=np.array([x+y,y-x]) 
dx=diff(x,y) 
dy=diff(y,y) 
dr=np.array([dx,dy]) 
I=np.dot(F,dr) 
k=integrate(I,(y,1,2)) 
print(k)
