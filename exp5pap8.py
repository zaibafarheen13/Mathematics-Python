# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:20:12 2022

@author: Zaiba Farheen
MATHS PAPER 8
EXPERIMENT-05
RANGE-KUTTA 4TH ORDER METHOD TO SOLVE DIFFERENTIAL EQUATION
"""
#%%
#ques 1
x0=1
y0=2
h=0.2

def f(x,y):
    return x*y

k1=h*f(x0,y0)
k2=h*f(x0+h/2,y0+k1/2)
k3=h*f(x0+h/2,y0+k2/2)
k4=h*f(x0+h,y0+k3)
k=(k1+2*k2+2*k3+k4)/6
print('k1=',round(k1,4))
print('k2=',round(k2,4))
print('k3=',round(k3,4))
print('k4=',round(k4,4))
print('k=',round(k,4))
y1=y0+k
print('y1=',round(y1,4))
#%%
#ques 2
x0=0
y0=1
h=0.2

def f(x,y):
    return 3*x+y/2

k1=h*f(x0,y0)
k2=h*f(x0+h/2,y0+k1/2)
k3=h*f(x0+h/2,y0+k2/2)
k4=h*f(x0+h,y0+k3)
k=(k1+2*k2+2*k3+k4)/6
print('k1=',round(k1,4))
print('k2=',round(k2,4))
print('k3=',round(k3,4))
print('k4=',round(k4,4))
print('k=',round(k,4))
y1=y0+k
print('y1=',round(y1,4))
#%%
#ques 3
x0=0
y0=1
h=0.2

def f(x,y):
    return (y-x)/(y+x)

k1=h*f(x0,y0)
k2=h*f(x0+h/2,y0+k1/2)
k3=h*f(x0+h/2,y0+k2/2)
k4=h*f(x0+h,y0+k3)
k=(k1+2*k2+2*k3+k4)/6
print('k1=',round(k1,4))
print('k2=',round(k2,4))
print('k3=',round(k3,4))
print('k4=',round(k4,4))
print('k=',round(k,4))
y1=y0+k
print('y1=',round(y1,4))
#%%
#ques 4
x0=0
y0=1
h=0.2

def f(x,y):
    return x+y**2

k1=h*f(x0,y0)
k2=h*f(x0+h/2,y0+k1/2)
k3=h*f(x0+h/2,y0+k2/2)
k4=h*f(x0+h,y0+k3)
k=(k1+2*k2+2*k3+k4)/6
print('k1=',round(k1,4))
print('k2=',round(k2,4))
print('k3=',round(k3,4))
print('k4=',round(k4,4))
print('k=',round(k,4))
y1=y0+k
print('y1=',round(y1,4))

x1=0.2
y1=1.2735
h=0.2

def f(x1,y1):
    return x1+y1**2

k1=h*f(x1,y1)
k2=h*f(x1+h/2,y1+k1/2)
k3=h*f(x1+h/2,y1+k2/2)
k4=h*f(x1+h,y1+k3)
k=(k1+2*k2+2*k3+k4)/6
print('k1=',round(k1,4))
print('k2=',round(k2,4))
print('k3=',round(k3,4))
print('k4=',round(k4,4))
print('k=',round(k,4))
y2=y1+k
print('y2=',round(y2,4))