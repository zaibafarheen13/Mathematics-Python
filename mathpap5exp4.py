# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:53:30 2021

@author: Zaiba Farheen
MATHEMATICS-PAPER 5
EXPERIMENT-04
NUMERICAL METHODS- SIMPSON'S 3/8th RULE
"""
#%%
#ques1
def f(x):
    return 1/(1+x**2)
a=0
b=6
n=6
def simpsons(a,b,n):
    h=(b-a)/n
    x=list()
    fx=list()
    i=0
    while i<=n:
        x.append(a+i*h)
        fx.append(f(x[i]))
        i+=1
#calculating result
    ans=0
    i=0
    while i<=n:
        if i==0 or i==n:
            ans+=fx[i]
        elif i%3!=0:
            ans+=3*fx[i]
        else:
            ans+=2*fx[i]
        i+=1
    ans=ans*(3*h/8)
    return ans
print("Value of integral is","%.6f"% simpsons(a,b,n))
#%%
#ques2
def f(x):
    return (2*x-x**2)**0.5
a=0
b=0.3
n=6
def simpsons(a,b,n):
    h=(b-a)/n
    x=list()
    fx=list()
    i=0
    while i<=n:
        x.append(a+i*h)
        fx.append(f(x[i]))
        i+=1
#calculating result
    ans=0
    i=0
    while i<=n:
        if i==0 or i==n:
            ans+=fx[i]
        elif i%3!=0:
            ans+=3*fx[i]
        else:
            ans+=2*fx[i]
        i+=1
    ans=ans*(3*h/8)
    return ans
print("Value of integral is","%.6f"% simpsons(a,b,n))
#%%
#ques3
from sympy import log
def f(x):
    return log(x)
a=4
b=5.2
n=6
def simpsons(a,b,n):
    h=(b-a)/n
    x=list()
    fx=list()
    i=0
    while i<=n:
        x.append(a+i*h)
        fx.append(f(x[i]))
        i+=1
#calculating result
    ans=0
    i=0
    while i<=n:
        if i==0 or i==n:
            ans+=fx[i]
        elif i%3!=0:
            ans+=3*fx[i]
        else:
            ans+=2*fx[i]
        i+=1
    ans=ans*(3*h/8)
    return ans
print("Value of integral is","%.6f"% simpsons(a,b,n))
#%%
def main():
    dlist=[]
    n=int(input('enter the list size:'))
    def inputdisplist():
       
        for i in range(n):
            print('enter the element at position',i,':')
            item=int(input())
            dlist.append(item)
        
        print('user list is:',dlist)

    def seqserach(dlist,item):
        pos=0
        found=False
        while pos<len(dlist) and not found:
            if dlist[pos]==item:
                found=True
            else:
                pos=pos+1
        if found==True:
            print(item,'was found at pos',pos+1)
        else:
            print(item,'not found')
    inputdisplist()
    print('item to be searched:')
    item=int(input())
    seqserach(dlist,item)
main()
      