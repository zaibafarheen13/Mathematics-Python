# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:17:39 2021

@author: Zaiba Farheen
MATHEMATICS-PAPER 5
EXPERIMENT-06
RING HOMOMORPHISM
"""
#%%
#ques1
def f(x):
    return 3*x 
def am(x,y):
    sum=x+y
    s=sum%4
    return s
def mm(x,y):
    mul=x*y
    m=mul%4
    return m
z=[0,1,2,3]
for i in z:
    for j in z:
        a=f(am(i,j))
        b=am(f(i),f(j))
        c=f(mm(i,j))
        d=mm(f(i),f(j))
        if a==b and c==d:
            Flag=True
        else:
            Flag=False
if Flag==True:
    print("f is a homomorphism")
else:
    print("f is not a homomorphism")
#%%
#ques2
def f(x):
    return x 
def am(x,y):
    sum=x+y
    s=sum%7
    return s
def mm(x,y):
    mul=x*y
    m=mul%7
    return m
z=[0,1,2,3,4,5,6]
for i in z:
    for j in z:
        a=f(am(i,j))
        b=am(f(i),f(j))
        c=f(mm(i,j))
        d=mm(f(i),f(j))
        if a==b and c==d:
            Flag=True
        else:
            Flag=False
if Flag==True:
    print("f is a homomorphism")
else:
    print("f is not a homomorphism")
#%%
#ques3
def f(x):
    return 5*x 
def am(x,y):
    sum=x+y
    s=sum%4
    return s
def ml(x,y):
    mul=x*y
    m=mul%4
    return m
def aa(x,y):
    sum=x+y
    s=sum%10
    return s
def mm(x,y):
    mul=x*y
    m=mul%10
    return m
z1=[0,1,2,3]
z2=[0,1,2,3,4,5,6,7,8,9]
for i in z1:
    for j in z1:
        for k in z2:
            for l in z2:
                a=f(am(i,j))
                b=aa(f(k),f(l))
                c=f(ml(i,j))
                d=mm(f(k),f(l))
                if a==b and c==d:
                    Flag=True
                else:
                    Flag=False
if Flag==True:
    print("f is a homomorphism")
else:
    print("f is not a homomorphism")


