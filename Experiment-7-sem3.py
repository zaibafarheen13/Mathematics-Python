#%%
#ques 1
from sympy import *
x=symbols('x')
def f1(x):
       return 1-x
def f2(x):
    return x**2+3
a=1
lhd=limit((f1(x)-f2(a))/(x-a),x,a,dir="-")
print("Left Hand Derivative is",lhd)
rhd=limit((f2(x)-f2(a))/(x-a),x,a,dir="+")
print("Right Hand Derivative is",rhd)
if lhd==rhd:
    print("Given function is defferentiable at point",a)
else:
    print("Given function is not differentiable at point",a)
    
   
#%%
#ques 2
from sympy import *
x=symbols('x')
def f1(x):
       return x**2
def f2(x):
    return 6*x-9
a=3
lhd=limit((f1(x)-f2(a))/(x-a),x,a,dir="-")
print("Left Hand Derivative is",lhd)
rhd=limit((f2(x)-f2(a))/(x-a),x,a,dir="+")
print("Right Hand Derivative is",rhd)
if lhd==rhd:
    print("Given function is defferentiable at point",a)
else:
    print("Given function is not differentiable at point",a)
    
 
#%%
#ques 3
from sympy import *
x=symbols('x')
def f1(x):
       return sin(x)
def f2(x):
    return sin(x)
a=pi/2
lhd=limit((f1(x)-f2(a))/(x-a),x,a,dir="-")
print("Left Hand Derivative is",lhd)
rhd=limit((f2(x)-f2(a))/(x-a),x,a,dir="+")
print("Right Hand Derivative is",rhd)
if lhd==rhd:
    print("Given function is defferentiable at point",a)
else:
    print("Given function is not differentiable at point",a)
    
   

