# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:53:55 2022

@author: Zaiba Farheen
MATHS PAPER-7
EXPERIMENT-08
SOLUTIONS TP DIFFERENT TYPES OF NON-LINEAR PDE
"""
#%%
#ques 1
from sympy import Function, diff, Eq,pprint,solve,dsolve
from sympy.abc import x,y,u,p,q,a,b
z = Function("z")(u)
eqn=z-p*q
eqn1=eqn.subs(p,diff(z,u)).subs(q,a*diff(z,u))
pprint(eqn1)
h1=solve(eqn1,diff(z,u))
pprint(h1)
sol=dsolve(h1[0]-diff(z,u))
pprint(sol)
ans=sol.subs(u,x+a*y)
pprint("Required answer is")
pprint(ans)
#%%
#ques 2
from sympy import Function, diff, Eq,solve,dsolve
from sympy.abc import x,y,u,p,q,a,b
z = Function("z")(u)
eqn=p**2+q**2-z
eqn1=eqn.subs(p,diff(z,u)).subs(q,a*diff(z,u))
print(eqn1)
h1=solve(eqn1,diff(z,u))
print(h1)
sol=dsolve(h1[0]-diff(z,u))
print(sol)
ans=sol.subs(u,x+a*y)
print("Required answer is")
print(ans)
#%%
#ques 3
from sympy import Function, diff, Eq,pprint,solve,dsolve
from sympy.abc import x,y,u,p,q,a,b
z = Function("z")(u)
eqn=z**2*((p**2+q**2+1))-1
eqn1=eqn.subs(p,diff(z,u)).subs(q,a*diff(z,u))
print(eqn1)
h1=solve(eqn1,diff(z,u))
print(h1)
sol=dsolve(h1[0]-diff(z,u))
print(sol)
ans=sol[0].subs(u,x+a*y)
print("Required answer is")
print(ans)
#%%
#ques 4
from sympy import Function, diff, Eq,pprint,solve,dsolve
from sympy.abc import x,y,u,p,q,a,b
z = Function("z")(u)
eqn=p**3+q**3-27*z
eqn1=eqn.subs(p,diff(z,u)).subs(q,a*diff(z,u))
print(eqn1)
h1=solve(eqn1,diff(z,u))
print(h1)
sol=dsolve(h1[0]-diff(z,u))
print(sol)
ans=sol[0].subs(u,x+a*y)
print("Required answer is")
print(ans)
#%%
#ques 5
from sympy.abc import x, y, a, b, c,k,p,q
from sympy import *
lhs=p+x
rhs=q+y
r1=Eq(lhs , a)
r2=Eq(rhs , a)
h1=solve(r1,p)
h2=solve(r2,q)
print("p =",h1 ,"and","q =",h2)
z=integrate(h1[0],x)+integrate(h2[0],y)
print("The solution is",z)
#%%
#ques 6
from sympy.abc import x, y, a, b, c,k,p,q
from sympy import *
lhs=p-cos(x)
rhs=cos(y)/q
r1=Eq(lhs , a)
r2=Eq(rhs , a)
h1=solve(r1,p)
h2=solve(r2,q)
print("p =",h1 ,"and","q =",h2)
z=integrate(h1[0],x)+integrate(h2[0],y)
print("The solution is",z)
#%%
#ques 7
from sympy.abc import x, y, a, b, c,k,p,q
from sympy import *
lhs=p-sin(x)
rhs=sin(y)-q
r1=Eq(lhs , a)
r2=Eq(rhs , a)
h1=solve(r1,p)
h2=solve(r2,q)
print("p =",h1 ,"and","q =",h2)
z=integrate(h1[0],x)+integrate(h2[0],y)
print("The solution is",z)