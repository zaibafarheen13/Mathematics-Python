# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 09:01:45 2021

@author: Zaiba Farheen
MATHEMATICS-PAPER 5
EXPERIMENT-05
CURL,DIVERGENCE,GRADIENT AND LAPLACIAN
"""
#%%
#ques 1
from sympy.physics.vector import ReferenceFrame
from sympy.physics.vector import divergence,curl
R=ReferenceFrame('R')
F=(R[1]**2-R[2]**2+3*R[2]*R[1]-2*R[0])*R.x+(3*R[0]*R[2]+2*R[0]*R[1])*R.y+(3*R[0]*R[1]-2*R[0]*R[2]+2*R[2])*R.z
A=divergence(F,R)
B=curl(F,R)
print("Divergence of vector function F is",A)
print("Curl of vector function F is",B)
print("Vector is both solenoidal and irrotational")
#%%
#ques 2
from sympy.physics.vector import ReferenceFrame
from sympy.physics.vector import divergence,gradient
R=ReferenceFrame('R')
F=(R[0]**2*R[1])+(R[2]**2*R[1])+(R[2]**3*R[0])
C=gradient(F,R)
D=divergence(C,R)
#Laplacian is divergence of gradient
print("Gradient of function F is",C)
print("Laplacian of the function F is",D)
#%%
#ques 3
from sympy.physics.vector import ReferenceFrame
from sympy.physics.vector import divergence,gradient,curl
R=ReferenceFrame('R')
F=(R[0]+R[1]*R[2])*R.x+(R[1]+R[2]*R[0])*R.y+(R[2]+R[0]*R[1])*R.z
f=R[0]**2+R[1]**2+R[2]**2
A=divergence(F,R)
B=curl(F,R)
C=gradient(f,R)
D=divergence(C,R)
#Laplacian is divergence of gradient
print("Divergence of vector function F is",A)
print("Curl of vector function F is",B)
print("Gradient of function F is",C)
print("Laplacian of the function F is",D)

