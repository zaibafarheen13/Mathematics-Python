# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:23:59 2021

@author: Zaiba Farheen
MATHEMATICS-PAPER 5
EXPERIMENT- 07
ISOMORPHISM
"""
#ques 1
def f(x):
    return x 
def am(x,y):
    sum=x+y
    s=sum%8
    return s
def mm(x,y):
    mul=x*y
    m=mul%8
    return m
z=[0,1,2,3,4,5,6,7]
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
#for one-one
for i in z:
    for j in z:
        if f(i)==f(j) and i==j:
            Flag_1=True
        else:
            Flag_1=False
if Flag_1==True:
    print("f is one-one")
else:
    print("f is not one-one")
#for onto
lhl=[]
rhl=[]
d=[]
for i in z:
    for j in z:
        for k in z:
            a=f(k)
            b=f(j)
            ##c=f(j)
            lhl.append(a)
            rhl.append(b)
            d.append(i)
lhl=list(set(lhl))
rhl=list(set(rhl))
if lhl==rhl:
    d=list(set(d))
    if d==z:
        Flag_2=True
    else:
        Flag_2=False
else:
    print("f is not onto")
if Flag_2==True:
    print("f is onto")
else:
    print("f is onto")
if Flag==True and Flag_1==True and Flag_2==True:
    print("f is an isomorphism")
else:
    print("f is not isomorphism")
#%%
eqs
    def f(x):
return x
def am(x,y):
sum=x+y
s=sum%8
return s
def mm(x,y):
mul=x*y
m=mul%8
return m
Z=[0,1,2,3,4,5,6,7]
for i in Z:
for j in Z:
a=f(am(i,j))
b=am(f(i),f(j))
c=f(mm(i,j))
d=mm(f(i),f(j))
if a==b and c==d:
Flag=True
else:
Flag=False
if Flag==True:
print("f is homomorphism")
else:
print("f is not a homomorphism")
for i in Z:
for j in Z:
if f(i)==f(j) and i==j:
Flag_1=True
else:
Flag_1=False
if Flag_1==True:
print("f is one-one")
else:
print("f is not one-one")
lhl=[]
rhl=[]
d=[]
for i in Z:
for j in Z:
for k in Z:
a=f(k)
b=f(j)
c=f(j)
lhl.append(a)
rhl.append(b)
d.append(i)
lhl=list(set(lhl))
rhl=list(set(rhl))
if lhl==rhl:
d=list(set(d))
if d==Z:
Flag_2=True
else:
Flag_2=False
else:
print("f is not onto")
if Flag==True:
print("f is onto")
else:
print("f is not onto")
if Flag==True and Flag_1==True and Flag_2==True:
print("f is isomorphism")
else:
print("f is not isomorphism")
