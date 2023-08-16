#%%
 #ques1  
from sympy import *
n=symbols('n')
r=limit(1/n*(n+1),n,oo)
print("limit of the given series is:",r)
if r==1 or r==-1 or r==0:
    print("Given series is Convergent")
elif r==oo or r==-oo:
    print("Given series is Divergent")
else:
    print("Given series is Oscillatory")
    
    
#%%
 #ques 2   
from sympy import *
n=symbols('n')
r=limit(n,n,oo)
print("limit of the given series is:",r)
if r==1 or r==-1 or r==0:
    print("Given series is Convergent")
elif r==oo or r==-oo:
    print("Given series is Divergent")
else:
    print("Given series is Oscillatory")
    
    


    
    
    
    
    
    
    
    
    
