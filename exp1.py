# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 08:08:19 2022

@author: Zaiba Farheen
MATHEMATICS PAPER-7
EXPERIMENT - 01
VECTOR SPACES
LINEAR COMBINATION

"""
#%%
#ques1
import numpy as np
u=[1,2,3]
v=[2,3,7]
w=[3,5,6]
vector=[3,7,-4]
A = np.column_stack([u,v,w])
x = np.linalg.lstsq(A, vector,rcond=None)
print("C1 ,C2 and C3 are",x[0])
c1=round(x[0][0],1)
c2=round(x[0][1],1)
c3=round(x[0][2],1)

for i in range(2):
    if (u[i]*c1) + (v[i]*c2) + (w[i]*c3) == (vector[i]):
       Flag=True
    else:
       Flag=False
if Flag==True:
    print("Given vector can  be expressed as Linear Combination of vectors")
else:
    print("Given vector can't  be expressed as Linear Combination of vectors")
#%%
#ques2
import numpy as np
u=[1,-3,2]
v=[2,-1,1]
vector=[1,7,-4]
A = np.column_stack([u,v])
x = np.linalg.lstsq(A, vector,rcond=None)
print("C1 and C2 are",x[0])
c1=round(x[0][0],1)
c2=round(x[0][1],1)
#print(c1,c2)

for i in range(2):
    if (u[i]*c1)+(v[i]*c2)==vector[i]:
       Flag=True
    else:
        Flag=False
if Flag==True:
    print("Given vector can  be expressed as Linear Combination of vectors")
else:
    print("Given vector can't  be expressed as Linear Combination of vectors") 
#%%
#ques3
import numpy as np
u=[1,2,-1]
v=[6,4,2]
vector=[4,-1,8]
A = np.column_stack([u,v])
x = np.linalg.lstsq(A, vector,rcond=None)
print("C1 and C2 are",x[0])
c1=round(x[0][0],1)
c2=round(x[0][1],1)
#print(c1,c2)

for i in range(2):
    if (u[i]*c1)+(v[i]*c2)==vector[i]:
       Flag=True
    else:
        Flag=False
if Flag==True:
    print("Given vector can  be expressed as Linear Combination of vectors")
else:
    print("Given vector can't  be expressed as Linear Combination of vectors") 
#%%
#ques4
import numpy as np
u=[1,1,1]
v=[1,2,3]
w=[2,-1,1]
vector=[1,-2,5]
A = np.column_stack([u,v,w])
x = np.linalg.lstsq(A, vector,rcond=None)
print("C1 ,C2 and C3 are",x[0])
c1=round(x[0][0],1)
c2=round(x[0][1],1)
c3=round(x[0][2],1)

for i in range(2):
    if (u[i]*c1) + (v[i]*c2) + (w[i]*c3) == (vector[i]):
       Flag=True
    else:
       Flag=False
if Flag==True:
    print("Given vector can  be expressed as Linear Combination of vectors")
else:
    print("Given vector can't  be expressed as Linear Combination of vectors")