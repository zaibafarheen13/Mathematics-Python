#%%
#ques1
from sympy import *
x=symbols('x')
a=2
lhl=limit(x+6,x,2,dir="-")
print("LHL of the given function is",lhl)
rhl=limit(x**2,x,2,dir="+")
print("RHL of the given function is",rhl)
if lhl==rhl:
    print("Limit exists at point",a)
else:
    print("Limit does not exists at point",a)


#%%
#ques2
from sympy import *
x=symbols('x')
a=3
lhl=limit(2*x+5,x,3,dir="-")
print("LHL of the given function is",lhl)
rhl=limit(3*x+2,x,3,dir="+")
print("RHL of the given function is",rhl)
if lhl==rhl:
    print("Limit exists at point",a)
else:
    print("Limit does not exists at point",a)


#%%
#ques3
from sympy import *
x=symbols('x')
a=-2
fa=limit(0,x,-2)
print("f(a)=",fa)
lhl=limit(3-x**2,x,-2,dir="-")
print("LHL of the given function is",lhl)
rhl=limit(11-x**2,x,-2,dir="+")
print("RHL of the given function is",rhl)
if lhl==rhl==fa:
    print("Given function is continuous at",a)
else:
    print("Given function is not continuous",a)
#for graph
import matplotlib.pyplot as plt
import numpy as np
x1=np.arange(-15,-2,1)
x2=np.arange(-2,15,1)
y1=3-x1**2
y2=11-x2**2
plt.plot(x1,y1,color='green')
plt.plot(x2,y2,color='red')
plt.show()


#%%
#ques4
from sympy import *
x=symbols('x')
a=0
fa=limit(0,x,0)
print("f(a)=",fa)
lhl=limit(x*cos(1/x),x,0,dir="-")
print("LHL of the given function is",lhl)
rhl=limit(x*cos(1/x),x,0,dir="+")
print("RHL of the given function is",rhl)
if lhl==rhl==fa:
    print("Given function is continuous at",a)
else:
    print("Given function is not continuous",a)
#for graph
import matplotlib.pyplot as plt
import numpy as np
x1=np.linspace(-4,1,1000)
x2=np.linspace(1,4,1000)
y1=x1*np.cos(1/x1)
y2=x2*np.cos(1/x2)
plt.plot(x1,y1,color='green')
plt.plot(x2,y2,color='red')
plt.show()


#%%
#ques5
from sympy import *
x=symbols('x')
a=3
fa=limit(6,x,3)
print("f(a)=",fa)
lhl=limit((x**2-9)/(x-3),x,3,dir="-")
print("LHL of the given function is",lhl)
rhl=limit((x**2-9)/(x-3),x,3,dir="+")
print("RHL of the given function is",rhl)
if lhl==rhl==fa:
    print("Given function is continuous at",a)
else:
    print("Given function is not continuous",a)
#for graph
import matplotlib.pyplot as plt
import numpy as np
x1=np.linspace(-4,0,1000)
x2=np.linspace(0,4,1000)
y1=(x1**2-9)/(x1-3)
y2=(x2**2-9)/(x2-3)
plt.plot(x1,y1,color='green')
plt.plot(x2,y2,color='red')
plt.show()
    







