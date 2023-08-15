# -*- coding: utf-8 -*-
"""
Created on Fri Aug  27 03:30:30 2021

@author: Zaiba Farheen
MATHEMATICS-PAPER 5
EXPERIMENT-01
NUMERICAL METHODS- NEWTON- GREGORY'S FORWARD DIFFERENCE FORMULA
"""
#%%
#ques1
from sympy import factorial
x= [1,2,3,4,5,6]
n= len(x)
y= [[0 for i in range(n)]
           for j in range(n)]
y[0][0]= 1
y[1][0]= 8
y[2][0]=27
y[3][0]= 64
y[4][0]=125
y[5][0]=216
def u_cal(u,n):
  temp= u
  for i in range(1,n):
    temp= temp*(u-i)
  return temp
for i in range (1,n):
  for j in range(n-i):
    y[j][i]= y[j+1][i-1]-y[j][i-1]
for i in range(n):
  print(x[i],end= "\t");
  for j in range(n-i):
    print(y[i][j],end="\t")
  print(" ");
value=2.5;
sum= y[0][0];
u= (value-x[0])/(x[1]-x[0]);
for i in range(1,n):
  sum= sum+(u_cal(u,i)*y[0][i])/factorial(i)
print("\n Value at",value,"is",round(sum,6))
#%%
#ques2
from sympy import factorial
x= [45,50,55,60]
n= len(x)
y= [[0 for i in range(n)]
           for j in range(n)]
y[0][0]= 0.7071
y[1][0]= 0.7660
y[2][0]=0.8192
y[3][0]= 0.8660
def u_cal(u,n):
  temp= u
  for i in range(1,n):
    temp= temp*(u-i)
  return temp
for i in range (1,n):
  for j in range(n-i):
    y[j][i]= y[j+1][i-1]-y[j][i-1]
for i in range(n):
  print(x[i],end= "\t");
  for j in range(n-i):
    print(y[i][j],end="\t")
  print(" ");
value=52;
sum= y[0][0];
u= (value-x[0])/(x[1]-x[0]);
for i in range(1,n):
  sum= sum+(u_cal(u,i)*y[0][i])/factorial(i)
print("\n Value at",value,"is",round(sum,6))
#%%
#ques3
from sympy import factorial
x= [0.1,0.2,0.3,0.4,0.5]
n= len(x)
y= [[0 for i in range(n)]
           for j in range(n)]
y[0][0]= 1.10517
y[1][0]= 1.22140
y[2][0]=1.34986
y[3][0]= 1.49182
y[4][0]=1.64872
def u_cal(u,n):
  temp= u
  for i in range(1,n):
    temp= temp*(u-i)
  return temp
for i in range (1,n):
  for j in range(n-i):
    y[j][i]= y[j+1][i-1]-y[j][i-1]
for i in range(n):
  print(x[i],end= "\t");
  for j in range(n-i):
    print(y[i][j],end="\t")
  print(" ");
value=0.24;
sum= y[0][0];
u= (value-x[0])/(x[1]-x[0]);
for i in range(1,n):
  sum= sum+(u_cal(u,i)*y[0][i])/factorial(i)
print("\n Value at",value,"is",round(sum,6))
#%%
#ques4
from sympy import factorial
x= [5,10,15,20,25,30]
n= len(x)
y= [[0 for i in range(n)]
           for j in range(n)]
y[0][0]= 0.0875
y[1][0]= 0.1763
y[2][0]=0.267
y[3][0]= 0.3640
y[4][0]=0.4663
y[5][0]=0.5774
def u_cal(u,n):
  temp= u
  for i in range(1,n):
    temp= temp*(u-i)
  return temp
for i in range (1,n):
  for j in range(n-i):
    y[j][i]= y[j+1][i-1]-y[j][i-1]
for i in range(n):
  print(x[i],end= "\t");
  for j in range(n-i):
    print(y[i][j],end="\t")
  print(" ");
value=16;
sum= y[0][0];
u= (value-x[0])/(x[1]-x[0]);
for i in range(1,n):
  sum= sum+(u_cal(u,i)*y[0][i])/factorial(i)
print("\n Value at",value,"is",round(sum,6))
