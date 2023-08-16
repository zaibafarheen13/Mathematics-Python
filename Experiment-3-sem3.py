#%%
#ques1
import itertools
Z=[0,1,2,3,4,5,6,7,8,9,10,11]
H=[0,4,8]
m=len(Z)
n=len(H)
I=m//n
l=[]
print("Index of a group is:",m//n)
for x in Z:
    c=[(x+y)%12 for y in H]
    print(c)
    l.append(sorted(c))
l.sort()
k=list(l for l,_ in itertools.groupby(l))
print()
print("Distinct left coset of H in G are",*k)


#%%
#ques2
import itertools
Z=[0,1,2,3,4,5]
H=[0,3]
m=len(Z)
n=len(H)
I=m//n
l=[]
print("Index of a group is:",m//n)
for x in Z:
    c=[(x+y)%6 for y in H]
    print(c)
    l.append(sorted(c))
l.sort()
k=list(l for l,_ in itertools.groupby(l))
print()
print("Distinct left coset of H in G are",*k)

    

    


    

    
