#ques 1
from sympy import *
n=symbols('n')
r=limit((1+1/n),n,oo)
print("limit of the given sequence is:",r)
if r==1 or r==-1 or r==0:
    print("Given sequence is Convergent")
elif r==oo or r==-oo:
    print("Given sequence is Divergent")
else:
    print("Given sequence is Oscillatory")
    
    
#%%
 #ques 2   
from sympy import *
n=symbols('n')
r=limit(log(n),n,oo)
print("limit of the given sequence is:",r)
if r==1 or r==-1 or r==0:
    print("Given sequence is Convergent")
elif r==oo or r==-oo:
    print("Given sequence is Divergent")
else:
    print("Given sequence is Oscillatory")
    
    
#%%
#ques 3
from sympy import *
n=symbols('n')
r=limit(n*(log(n+1)-log(n)),n,oo)
print("limit of the given sequence is:",r)
if r==1 or r==-1 or r==0:
    print("Given sequence is Convergent")
elif r==oo or r==-oo:
    print("Given sequence is Divergent")
else:
    print("Given sequence is Oscillatory")
    
    
#%%
#ques4
from sympy import *
n=symbols('n')
r=limit(-(n**2),n,oo)
print("limit of the given sequence is:",r)
if r==1 or r==-1 or r==0:
    print("Given sequence is Convergent")
elif r==oo or r==-oo:
    print("Given sequence is Divergent")
else:
    print("Given sequence is Oscillatory")
    

#%%
#ques5
from sympy import *
n=symbols('n')
r=limit(1+cos(n*pi),n,oo)
print("limit of the given sequence is:",r)
if r==1 or r==-1 or r==0:
    print("Given sequence is Convergent")
elif r==oo or r==-oo:
    print("Given sequence is Divergent")
else:
    print("Given sequence is Oscillatory")


#%%
#ques6
from sympy import *
n=symbols('n')
r=limit(1+sin((n*pi)/2),n,oo)
print("limit of the given sequence is:",r)
if r==1 or r==-1 or r==0:
    print("Given sequence is Convergent")
elif r==oo or r==-oo:
    print("Given sequence is Divergent")
else:
    print("Given sequence is Oscillatory")
    
    
    
    
    
    
    
    
    
    
    
