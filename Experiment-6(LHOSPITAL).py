#%%
#ques1
from sympy import symbols,limit,sin
x=symbols('x')
ans=limit((x-sin(x))/(x**3),x,0)
print(ans)


#%%
#ques2
from sympy import symbols,limit,tan,pi
x=symbols('x')
ans=limit((tan(5*x))/tan(x),x,pi/2)
print(ans)


#%%
#ques3
from sympy import symbols,limit,tan,log
x=symbols('x')
ans=limit((x*(log(tan(x))))/x,x,0)
print(ans)


#%%
#ques4
from sympy import symbols,limit,cos
x=symbols('x')
ans=limit((cos(x))**(1/x**2),x,0)
print(ans)

#%%
#ques5
from sympy import symbols,limit,sin,tan
x=symbols('x')
ans=limit((sin(x)**(tan(x))),x,0)
print(ans)


#%%
#ques6
from sympy import symbols,limit,tan
x=symbols('x')
ans=limit((1/x)**(tan(x)),x,0)
print(ans)


#%%
#ques7
from sympy import symbols,limit,csc,cot
x=symbols('x')
ans=limit(csc(x)-cot(x),x,0)
print(ans)