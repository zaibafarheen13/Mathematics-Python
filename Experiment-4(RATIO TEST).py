#%%
#ques1
def u(x):return pow(2,x)*factorial(x)/pow(x,x)
from sympy import *
n=symbols('n')
r=u(n+1)/u(n)
s=simplify(r)
print(s)
l=limit(s,n,oo)
print(l)
if l<1:
    print("Converges")
elif l>1:
    print("Diverges")
else:
    print("Fails")
    
    
#%%
#ques2
def u(x):return factorial(x+1)/pow(3,x)
from sympy import *
n=symbols('n')
r=u(n+1)/u(n)
s=simplify(r)
print(s)
l=limit(s,n,oo)
print(l)
if l<1:
    print("Converges")
elif l>1:
    print("Diverges")
else:
    print("Fails")


#%%
#ques3
def u(x):return factorial(x)/pow(5,x)
from sympy import *
n=symbols('n')
r=u(n+1)/u(n)
s=simplify(r)
print(s)
l=limit(s,n,oo)
print(l)
if l<1:
    print("Converges")
elif l>1:
    print("Diverges")
else:
    print("Fails")
    
    
#%%
#ques4
def u(x):return x**2/factorial(x)
from sympy import *
n=symbols('n')
r=u(n+1)/u(n)
s=simplify(r)
print(s)
l=limit(s,n,oo)
print(l)
if l<1:
    print("Converges")
elif l>1:
    print("Diverges")
else:
    print("Fails")
    
    
#%%
#ques5
def u(x):return 1/(pow(x,2)+1)
from sympy import *
n=symbols('n')
r=u(n+1)/u(n)
s=simplify(r)
print(s)
l=limit(s,n,oo)
print(l)
if l<1:
    print("Converges")
elif l>1:
    print("Diverges")
else:
    print("Fails")
a=1/r
b=a-1
c=b*n
d=simplify(c)
print(d)
lim=limit(d,n,oo)
print(lim)
if lim>1:
    print("Converges")
elif lim<1:
    print("Diverges")
else:
    print("Fails")


    


    


    

    


    