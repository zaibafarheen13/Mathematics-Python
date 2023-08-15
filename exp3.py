# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 09:12:43 2022

@author: Zaiba Farheen
"""

#%%
#ques1
from sympy import *
import numpy as  np
A=Matrix([[1,1,0],[0,1,0], [0,1,1]])
r=3
n=3
if r>n:
    print("Given vectors are Linearly dependent ")
    print("Dimension of the subspace is",A.rank())
    RREF=(A.rref())
    I=RREF[0]
    print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
   
if r==n:
    D=A.det()
    print("Determinant of the matrix is",D)
    if D==0:
        print("Given vectors are Linearly dependent ")
        print("Dimension of the subspace is",A.rank())
        RREF=(A.rref())
        I=RREF[0]
        print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
    else:
        print("Given vectors are Linearly Independent and hence forms basis")
        print("Basis vectors are the non zero rows", A.row(0),A.row(1),A.row(2))

if r<n:
    R=A.rank()
    if(R==r):
        print("The given vectors are linearly Independent  ")
        print("Basis are", A.row(0),A.row(1),A.row(2))
    else:
        print("The given vectors are linearly Dependent ")
        print("Dimension of the subspace is",A.rank())
        RREF=A.rref()
        I=RREF[0]
        print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
        #%%
        #ques2
from sympy import *
import numpy as  np
A=Matrix([[1,2,3],[3,1,0], [-2,1,3]])
r=3
n=3
if r>n:
    print("Given vectors are Linearly dependent ")
    print("Dimension of the subspace is",A.rank())
    RREF=(A.rref())
    I=RREF[0]
    print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
   
if r==n:
    D=A.det()
    print("Determinant of the matrix is",D)
    if D==0:
        print("Given vectors are Linearly dependent ")
        print("Dimension of the subspace is",A.rank())
        RREF=(A.rref())
        I=RREF[0]
        print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
    else:
        print("Given vectors are Linearly Independent and hence forms basis")
        print("Basis vectors are the non zero rows", A.row(0),A.row(1),A.row(2))

if r<n:
    R=A.rank()
    if(R==r):
        print("The given vectors are linearly Independent  ")
        print("Basis are", A.row(0),A.row(1),A.row(2))
    else:
        print("The given vectors are linearly Dependent ")
        print("Dimension of the subspace is",A.rank())
        RREF=A.rref()
        I=RREF[0]
        print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
#%%
#ques3
from sympy import *
import numpy as  np
A=Matrix([[1,-2,4,1],[2,-3,9,-1], [1,0,6,-5],[2,-5,7,5]])
r=3
n=4
if r>n:
    print("Given vectors are Linearly dependent ")
    print("Dimension of the subspace is",A.rank())
    RREF=(A.rref())
    I=RREF[0]
    print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
   
if r==n:
    D=A.det()
    print("Determinant of the matrix is",D)
    if D==0:
        print("Given vectors are Linearly dependent ")
        print("Dimension of the subspace is",A.rank())
        RREF=(A.rref())
        I=RREF[0]
        print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
    else:
        print("Given vectors are Linearly Independent and hence forms basis")
        print("Basis vectors are the non zero rows", A.row(0),A.row(1),A.row(2))

if r<n:
    R=A.rank()
    if(R==r):
        print("The given vectors are linearly Independent  ")
        print("Basis are", A.row(0),A.row(1),A.row(2))
    else:
        print("The given vectors are linearly Dependent ")
        print("Dimension of the subspace is",A.rank())
        RREF=A.rref()
        I=RREF[0]
        print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
#%%
#ques4
from sympy import *
import numpy as  np
A=Matrix([[1,2,2,1],[0,2,0,1], [1,-2,2,-1]])
r=3
n=4
if r>n:
    print("Given vectors are Linearly dependent ")
    print("Dimension of the subspace is",A.rank())
    RREF=(A.rref())
    I=RREF[0]
    print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
   
if r==n:
    D=A.det()
    print("Determinant of the matrix is",D)
    if D==0:
        print("Given vectors are Linearly dependent ")
        print("Dimension of the subspace is",A.rank())
        RREF=(A.rref())
        I=RREF[0]
        print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
    else:
        print("Given vectors are Linearly Independent and hence forms basis")
        print("Basis vectors are the non zero rows", A.row(0),A.row(1),A.row(2))

if r<n:
    R=A.rank()
    if(R==r):
        print("The given vectors are linearly Independent  ")
        print("Basis are", A.row(0),A.row(1),A.row(2))
    else:
        print("The given vectors are linearly Dependent ")
        print("Dimension of the subspace is",A.rank())
        RREF=A.rref()
        I=RREF[0]
        print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
#%%
#ques5
from sympy import *
import numpy as  np
A=Matrix([[2,7,3],[1,-1,0], [1,2,1],[0,3,1]])
r=4
n=3
if r>n:
    print("Given vectors are Linearly dependent ")
    print("Dimension of the subspace is",A.rank())
    RREF=(A.rref())
    I=RREF[0]
    print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
   
if r==n:
    D=A.det()
    print("Determinant of the matrix is",D)
    if D==0:
        print("Given vectors are Linearly dependent ")
        print("Dimension of the subspace is",A.rank())
        RREF=(A.rref())
        I=RREF[0]
        print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")
    else:
        print("Given vectors are Linearly Independent and hence forms basis")
        print("Basis vectors are the non zero rows", A.row(0),A.row(1),A.row(2))

if r<n:
    R=A.rank()
    if(R==r):
        print("The given vectors are linearly Independent  ")
        print("Basis are", A.row(0),A.row(1),A.row(2))
    else:
        print("The given vectors are linearly Dependent ")
        print("Dimension of the subspace is",A.rank())
        RREF=A.rref()
        I=RREF[0]
        print("Row Reduced Echelon Form is ",I,"and its non zero rows form basis")