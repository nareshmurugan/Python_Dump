Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python37-32/g.py ===
#######################TO FIND THE VARIABLES X,Y&Z BY MATRIX INVERSION METHOD####################### 

ENTER A NUMBER OF THE ELEMENT M11:	7*10**4
ENTER A NUMBER OF THE ELEMENT M12:	456524
ENTER A NUMBER OF THE ELEMENT M13:	5245
ENTER A NUMBER OF THE ELEMENT M21:	234
ENTER A NUMBER OF THE ELEMENT M22:	5
ENTER A NUMBER OF THE ELEMENT M23:	2345
ENTER A NUMBER OF THE ELEMENT M31:	2345
ENTER A NUMBER OF THE ELEMENT M32:	43
ENTER A NUMBER OF THE ELEMENT M33:	5
ENTER THE CONSTANT OF C1:	345
ENTER THE CONSTANT OF C2:	43
ENTER THE CONSTANT OF C3:	5
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python37-32/g.py", line 16, in <module>
    c3=eval(input('ENTER THE CONSTANT OF C3:\t'))
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 
=== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python37-32/g.py ===
#######################TO FIND THE VARIABLES X,Y&Z BY MATRIX INVERSION METHOD####################### 

ENTER A NUMBER OF THE ELEMENT M11:	7*10
ENTER A NUMBER OF THE ELEMENT M12:	
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python37-32/g.py", line 6, in <module>
    M12=eval(input('ENTER A NUMBER OF THE ELEMENT M12:''\t'))
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 
=== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python37-32/g.py ===
#######################TO FIND THE VARIABLES X,Y&Z BY MATRIX INVERSION METHOD####################### 

ENTER A NUMBER OF THE ELEMENT M11:	7^10
ENTER A NUMBER OF THE ELEMENT M12:	4
ENTER A NUMBER OF THE ELEMENT M13:	3
ENTER A NUMBER OF THE ELEMENT M21:	54
ENTER A NUMBER OF THE ELEMENT M22:	3
ENTER A NUMBER OF THE ELEMENT M23:	5
ENTER A NUMBER OF THE ELEMENT M31:	35
ENTER A NUMBER OF THE ELEMENT M32:	35
ENTER A NUMBER OF THE ELEMENT M33:	3
ENTER THE CONSTANT OF C1:	53
ENTER THE CONSTANT OF C2:	3
ENTER THE CONSTANT OF C3:	2
##############STEP1:	THE EXPRESSION TO SOLVE THE EQUATIONS BY MATRIX INVERSTION METHOD############## 

XA=B
X=A^-1*B
WE WANT TO FIND FIRST A^1
WE KNOW THAT A^1=1/|A|*ADJ(A)
A= 	 [13, 4, 3]
	 [54, 3, 5]
	 [54, 3, 5] 

|A|= 13 * ( 3 * 3 - 35 * 5 ) - 4 * ( 54 * 3 - 35 * 5 ) + 3 * ( 54 * 35 - 35 * 3 ) 

THEREFORE |A|= 3249
|A| IS !=0 THEREFORE A^-1 IS EXIST
######TO FIND THE XYZ VARIABLE MULTIPLE THE A^-1*B BY THE EXPRESSION XA=B ###### 

A^-1*B=				 = 1/ 3249 [-166, 93, 11] * [53]
				 = 1/ 3249 [13, -66, 97] * [3]
				 = 1/ 3249 [1785, -315, -177] * [2] 

				 = 1/ 3249 * [-8497]
				 = 1/ 3249 * [685]
				 = 1/ 3249 * [93306] 

				 = [-3]
				 = [0]
				 = [29] 

THE VALUE OF THE VARIABLE X IS: -3
THE VALUE OF THE VARIABLE Y IS: 0
THE VALUE OF THE VARIABLE Z IS: 29
DO YOU WANT TO FIND ANOTHER SOLUTION:	
=== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python37-32/g.py ===
#######################TO FIND THE VARIABLES X,Y&Z BY MATRIX INVERSION METHOD####################### 

ENTER A NUMBER OF THE ELEMENT M11:	
	=== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python37-32/g.py ===df
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python37-32/g.py", line 5, in <module>
    M11=eval(input('ENTER A NUMBER OF THE ELEMENT M11:''\t'))
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> eval(7^10)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    eval(7^10)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> eval(int(7^10))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    eval(int(7^10))
TypeError: eval() arg 1 must be a string, bytes or code object
>>> n=eval(6*8)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    n=eval(6*8)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> eval(8*7,int)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    eval(8*7,int)
TypeError: globals must be a dict
>>> 
x
4
