import numpy as n
import rref as R
from sympy import *
M=Matrix([[14,0,11,3],[22,23,4,7],[-12,-34,-3,-4]])
print('Matrix:{}'.format(M))
Matrix([[14, 0, 11, 3], [22, 23, 4, 7], [-12, -34, -3, -4]])
print("THE ROW LFJFAIREHGOEGHAEUTG : {}".format(R.RREF(M)))
r=R.RREF(M)
print(r)
g=n.array(r)
print(M)
