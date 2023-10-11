#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    a=s.split()
    l=[]
    for i in range(len(a)):
        l.append(a[i].title()+' ')
    ss=''
    for j in l:
        ss+=j
    print(ss)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
cap
