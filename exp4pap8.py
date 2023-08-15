# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 08:39:04 2022

@author: Zaiba Farheen
MATHEMATICS PAPER 8
EXPERIMENT 4
SOLUTION TO SYSTEM OF LINEAR EQUATIONS-JACOBI'S METHOD
"""
#%%
#ques 1
from numpy import zeros,array,diag,diagflat,dot
def jacobi(A,b,x0):
  D=diag(A)
  R=A-diagflat(D)
  for i in range(10):
    x0=(b-dot(R,x0))/D
  return x0
A=array([[20,1,-2],[3,20,-1],[2,-3,20]])
b=array([17,-18,25])
x0=array([1,1,1])
sol=jacobi(A,b,x0)
print("Solution is",sol)
#%%
#ques 2
from numpy import zeros,array,diag,diagflat,dot
def jacobi(A,b,x0):
  D=diag(A)
  R=A-diagflat(D)
  for i in range(10):
    x0=(b-dot(R,x0))/D
  return x0
A=array([[10,1,1],[2,10,1],[2,2,10]])
b=array([12,13,14])
x0=array([1,1,1])
sol=jacobi(A,b,x0)
print("Solution is",sol)
#%%
#ques 3
from numpy import zeros,array,diag,diagflat,dot
def jacobi(A,b,x0):
  D=diag(A)
  R=A-diagflat(D)
  for i in range(15):
    x0=(b-dot(R,x0))/D
  return x0
A=array([[5,-1,0],[-1,5,-1],[0,1,-5]])
b=array([9,4,6])
x0=array([1,1,1])
sol=jacobi(A,b,x0)
print("Solution is",sol)