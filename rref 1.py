from sympy.interactive import printing
printing.init_printing(use_latex= True)
from sympy import Eq,solve_linear_system,Matrix
from numpy import linalg
import numpy as np
import sympy as sp
print("USING SYMPY:")
eq1=sp.Function('eq1')
eq2=sp.Function('eq2')

x,y=sp.symbols('x y')

eq1=Eq(2*x-y , -4)
eq2=Eq(3*x-1 , -2)
display(eq1)
display(eq2)
