# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 09:25:50 2022

@author: Zaiba Farheen
MATHEMATICS PAPER-7
EXPERIMENT - 02
VECTOR SPACES
LINEAR INDEPENDENCE AND LINEAR DEPENDENCE
"""
#%%
#QUES1
from sympy import *
A=Matrix([[1,1,-1],[2,-3,5], [-2,1,4]])
D=A.det()
if(D==0):
    print("The given vectors are linearly Dependent ")
else:
    print("The given vectors are linearly independent as D is",D,"non zero.")
#%%
#ques3
from sympy import *
r=3
n=4
A=Matrix([[6,2,-1,2],[-1,3,5,1], [-3,7,8,3]])
R=A.rank()
print("rank of the matrix is",R)
RREF=A.rref()
print(RREF[0])
if(R==r):
  print("The given vectors are linearly Independent ")
else:
  print("The given vectors are linearly Dependent ")
  #%%
  #ques4
  from sympy import *
r=4
n=4
A=Matrix([[1,1,2,4],[2,-1,-5,2], [1,-1,4,0],[2,1,1,6]])
R=A.rank()
print("rank of the matrix is",R)
RREF=A.rref()
print(RREF[0])
if(R==r):
  print("The given vectors are linearly Independent ")
else:
  print("The given vectors are linearly Dependent ")
  #%%
  #ques2
  from sympy import *
A=Matrix([[1,-2,3],[5,6,-1], [3,2,1]])
D=A.det()
if(D==0):
    print("The given vectors are linearly Dependent ")
else:
    print("The given vectors are linearly independent as D is",D,"non zero.")
  