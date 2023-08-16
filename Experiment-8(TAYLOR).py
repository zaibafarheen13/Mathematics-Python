#%%
#ques 1
import sympy as sy
import numpy as np 
from sympy.functions import log
#Define the variable and the function to approximate
x=sy.Symbol('x')
function=log(1+x)
#Factorial function
def factorial(n):
    if n<=0:
        return 1
    else:
        return n*factorial(n-1)
#Taylor approximation at x0 of the function 'function'
x0=2
n=4
def taylor(function,x0,n):
    i=0
    p=0
    while i<=n:
        p=p+(function.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        i+=1
    return p
print(taylor(function,x0,n))


#%%
#ques 2
import sympy as sy
import numpy as np 
#Define the variable and the function to approximate
x=sy.Symbol('x')
function=1/x
#Factorial function
def factorial(n):
    if n<=0:
        return 1
    else:
        return n*factorial(n-1)
#Taylor approximation at x0 of the function 'function'
x0=3
n=4
def taylor(function,x0,n):
    i=0
    p=0
    while i<=n:
        p=p+(function.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        i+=1
    return p
print(taylor(function,x0,n))


#%%
#ques 3
import sympy as sy
import numpy as np 
from sympy.functions import sqrt
#Define the variable and the function to approximate
x=sy.Symbol('x')
function=1/sqrt(x)
#Factorial function
def factorial(n):
    if n<=0:
        return 1
    else:
        return n*factorial(n-1)
#Taylor approximation at x0 of the function 'function'
x0=2
n=3
def taylor(function,x0,n):
    i=0
    p=0
    while i<=n:
        p=p+(function.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        i+=1
    return p
print(taylor(function,x0,n))


#%%
#ques 4
import sympy as sy
import numpy as np 
from sympy.functions import exp
#Define the variable and the function to approximate
x=sy.Symbol('x')
function=exp(x)
#Factorial function
def factorial(n):
    if n<=0:
        return 1
    else:
        return n*factorial(n-1)
#Taylor approximation at x0 of the function 'function'
x0=2
n=4
def taylor(function,x0,n):
    i=0
    p=0
    while i<=n:
        p=p+(function.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        i+=1
    return p
print(taylor(function,x0,n))


