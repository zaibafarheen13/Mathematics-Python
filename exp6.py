# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 09:10:02 2022

@author: Zaiba Farheen
MATH PAPER 7
EXPERIMENT 6
LINEAR TRANSFORMATION OF MATRIX
"""
#%%
#ques 1
from sympy import*
a,b,x,y=symbols("a,b,x,y")
import numpy as np
A=Matrix([[-1,0],[2,0],[1,3]])
u1=np.array([1,0])
u2=np.array([2,-1])
v1=np.array([1,2,0])
v2=np.array([0,-1,0])
v3=np.array([1,-1,1])
T0=np.array([A[0,0]*v1 , A[1,0]*v2 , A[2,0]*v3])
T1=np.array([A[0,1]*v1 , A[1,1]*v2 , A[2,1]*v3])
sumT0=T0[0]+T0[1]+T0[2]
sumT1=T1[0]+T1[1]+T1[2]
print(sumT0,sumT1)
eq=np.array([u1[0]*x + u2[0]*y ,u1[1]*x + u2[1]*y] )
p,q=eq[0],eq[1]
print(p,"and",q)
t=sumT0*p+sumT1*q
print("The linear transformation T is T(x,y)=",t)
#%%
#ques 2
from sympy import*
a,C1,C2,x,y=symbols("a,C1,C2,x,y")
import numpy as np
A=Matrix([[2,3],[4,-5]])
u1=np.array([1,-1])
u2=np.array([1,1])
v1=np.array([1,0])
v2=np.array([0,1])
T0=np.array([A[0,0]*v1 , A[1,0]*v2 ])
T1=np.array([A[0,1]*v1 , A[1,1]*v2 ])
sumT0=T0[0]+T0[1]
sumT1=T1[0]+T1[1]
print(sumT0,sumT1)
eq=np.array([u1[0]*C1 + u2[0]*C2 ,u1[1]*C1 + u2[1]*C2] )
p,q=eq[0],eq[1]
print(p,"and",q)
a=solve((p-x,q-y),C1,C2,dict=True)
c1,c2=a[0][C1] , a[0][C2]
t=sumT0*c1+sumT1*c2
print("The linear transformation T is T(x,y)=",t)
#%%
#ques 3
from sympy import*
a,C1,C2,C3,x,y,z=symbols("a,C1,C2,C3,x,y,z")
import numpy as np
A=Matrix([[1,0,1],[2,1,1],[-1,1,-2]])
u1=np.array([1,0,0])
u2=np.array([0,1,0])
u3=np.array([0,0,1])
T0=np.array([A[0,0]*u1 , A[1,0]*u2 , A[2,0]*u3])
T1=np.array([A[0,1]*u1 , A[1,1]*u2 , A[2,1]*u3])
T2=np.array([A[0,2]*u1 , A[1,2]*u2 , A[2,2]*u3])
sumT0=T0[0]+T0[1]+T0[2]
sumT1=T1[0]+T1[1]+T1[2]
sumT2=T2[0]+T2[1]+T2[2]
print(sumT0,sumT1,sumT2)
eq=np.array([u1[0]*C1 + u2[0]*C2 + u3[0]*C3,u1[1]*C1 + u2[1]*C2 + u3[1]*C3,
            u1[2]*C1 + u2[2]*C2 + u3[2]*C3])
p,q,r=eq[0],eq[1],eq[2]
print(p,"and",q,"and",r)
a=solve((p-x,q-y,r-z),C1,C2,C3,dict=True)
c1,c2,c3=a[0][C1] , a[0][C2] , a[0][C3]
t=sumT0*c1+sumT1*c2+sumT2*c3
print("The linear transformation T is T(x,y)=",t)
