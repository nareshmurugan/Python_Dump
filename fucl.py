Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import chrome
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
ebacd
fghij
olmkn
trpqs
xywuv
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py", line 1, in <module>
    a=int(input())
ValueError: invalid literal for int() with base 10: 'ebacd'
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
dfass
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py", line 2, in <module>
    b=int(input())
ValueError: invalid literal for int() with base 10: 'dfass'
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lc
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    lc
NameError: name 'lc' is not defined
>>> l
[['e', 'b', 'a', 'c', 'd'], ['f', 'g', 'h', 'i', 'j'], ['o', 'l', 'm', 'k', 'n'], ['t', 'r', 'p', 'q', 's'], ['x', 'y', 'w', 'u', 'v']]
>>> dic
{97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z'}
>>> for i in l
SyntaxError: invalid syntax
>>> for i in l:
	print(i)

	
['e', 'b', 'a', 'c', 'd']
['f', 'g', 'h', 'i', 'j']
['o', 'l', 'm', 'k', 'n']
['t', 'r', 'p', 'q', 's']
['x', 'y', 'w', 'u', 'v']
>>> for i in l:
	print(i.sort())

	
None
None
None
None
None
>>> for i in l:
	print(i)

	
['a', 'b', 'c', 'd', 'e']
['f', 'g', 'h', 'i', 'j']
['k', 'l', 'm', 'n', 'o']
['p', 'q', 'r', 's', 't']
['u', 'v', 'w', 'x', 'y']
>>> lll=[]
>>> for i in l:
	lll.append(list(list(i[0])))

	
>>> lll
[['a'], ['f'], ['k'], ['p'], ['u']]
>>> lll=[]
>>> for i in l:
	lll.append(list(i[0]))

	
>>> lll
[['a'], ['f'], ['k'], ['p'], ['u']]
>>> lll=[]
>>> for i in l:
	lll.append(list(i[0]))

	
>>> lll
[['a'], ['f'], ['k'], ['p'], ['u']]
>>> lll=[]
>>> for i in l:
	lll.append(i[0])

	
>>> 
>>> 
>>> lll
['a', 'f', 'k', 'p', 'u']
>>> lll=[]
>>> for i in l:
	for j in range(b):
		lll.append(i[j])

		
>>> lll
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
>>> for i in lll:
	print(i)

	
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
>>> for i in l:
	for j in range(b):
		lll.append(i[j])

		
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> lll
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
>>> lll=[]
>>> for i in l:
	k=[]
	for j in range(b):
		k.append(i[j])
		lll.append(k)

		
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> lll=[]
>>> 
>>> 
>>> 
>>> for i in l:
	k=[]
	for j in range(b):
		k.append(i[j])
		lll.append(k)

>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> set(lll)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    set(lll)
TypeError: unhashable type: 'list'

>>> lll=[]
>>> for i in l:
	
SyntaxError: multiple statements found while compiling a single statement
>>> lll=[]
>>> for i in l:
	
SyntaxError: multiple statements found while compiling a single statement
>>> lll=[]
>>> 
>>> for i in l:
	
SyntaxError: invalid syntax
>>> >>> for i in l:
	
SyntaxError: invalid syntax
>>> lll=[]
>>> for i in l:
	
SyntaxError: multiple statements found while compiling a single statement
>>> lll=[]
>>> for i in l:
	
SyntaxError: multiple statements found while compiling a single statement
>>> lll=[]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py", line 17, in <module>
    k.append(i[j])
TypeError: list indices must be integers or slices, not str
>>> 
>>> 
>>> lll
[]
>>> l
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> str(l)
"[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]"
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['a'], ['f'], ['k'], ['p'], ['u']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py

Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py", line 1, in <module>
    a=int(input())
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py

Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py", line 1, in <module>
    a=int(input())
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['u']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> set(str(lll))
{']', 'v', '[', ',', "'", 'w', 'x', ' ', 'y', 'u'}
>>> set(lll)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    set(lll)
TypeError: unhashable type: 'list'
>>> set(lll)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    set(lll)
TypeError: unhashable type: 'list'
>>> 
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py", line 17, in <module>
    k.append(i[j])
NameError: name 'j' is not defined
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py", line 18, in <module>
    k.append(i[j])
NameError: name 'j' is not defined
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['a'], ['f'], ['k'], ['p'], ['u']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['a'], ['g'], ['m'], ['s'], ['y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py", line 19, in <module>
    k.append(i[o])
TypeError: 'int' object is not subscriptable
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py", line 19, in <module>
    k.append(i[o])
IndexError: list index out of range
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['a'], ['g'], ['m'], ['s'], ['y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> a=set([1,2,3],[2,3,4])
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a=set([1,2,3],[2,3,4])
TypeError: set expected at most 1 argument, got 2
>>> a=set({[1,2,3],[2,3,4]})
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a=set({[1,2,3],[2,3,4]})
TypeError: unhashable type: 'list'
>>> a=set({(1,2,3),(2,3,4)})
>>> 
>>> a
{(1, 2, 3), (2, 3, 4)}
>>> t=[]
>>> for i in a:
	t.append(i)

	
>>> t
[(1, 2, 3), (2, 3, 4)]
>>> {(1, 2, 3), (2, 3, 4)}
{(1, 2, 3), (2, 3, 4)}

>>> 
>>> 
>>> 
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> tuple(lll)
(['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'])
>>> ll=[]
>>> ll=()
>>> tuple()
()
>>> ll=tuple()
>>> ll
()
>>> ll=(1,2,3)
>>> ll.insert(0,1)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    ll.insert(0,1)
AttributeError: 'tuple' object has no attribute 'insert'
>>> ll.update(0,1)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    ll.update(0,1)
AttributeError: 'tuple' object has no attribute 'update'
>>> l
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> llll
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    llll
NameError: name 'llll' is not defined
>>> ll
(1, 2, 3)
>>> a=(x for x in lll)
>>> a
<generator object <genexpr> at 0x000001EF37E495F0>
>>> tuple(a)
(['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'])
>>> a=list((x for x in lll))
>>> 
>>> a
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> b=()
>>> b=[]
>>> for i in lll:
	b.append(tuple(i))

	
>>> b
[('a', 'b', 'c', 'd', 'e'), ('a', 'b', 'c', 'd', 'e'), ('a', 'b', 'c', 'd', 'e'), ('a', 'b', 'c', 'd', 'e'), ('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), ('f', 'g', 'h', 'i', 'j'), ('f', 'g', 'h', 'i', 'j'), ('f', 'g', 'h', 'i', 'j'), ('f', 'g', 'h', 'i', 'j'), ('k', 'l', 'm', 'n', 'o'), ('k', 'l', 'm', 'n', 'o'), ('k', 'l', 'm', 'n', 'o'), ('k', 'l', 'm', 'n', 'o'), ('k', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('p', 'q', 'r', 's', 't'), ('p', 'q', 'r', 's', 't'), ('p', 'q', 'r', 's', 't'), ('p', 'q', 'r', 's', 't'), ('u', 'v', 'w', 'x', 'y'), ('u', 'v', 'w', 'x', 'y'), ('u', 'v', 'w', 'x', 'y'), ('u', 'v', 'w', 'x', 'y'), ('u', 'v', 'w', 'x', 'y')]
>>> set(b)
{('k', 'l', 'm', 'n', 'o'), ('f', 'g', 'h', 'i', 'j'), ('a', 'b', 'c', 'd', 'e'), ('p', 'q', 'r', 's', 't'), ('u', 'v', 'w', 'x', 'y')}
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> b
[('a', 'b', 'c', 'd', 'e'), ('a', 'b', 'c', 'd', 'e'), ('a', 'b', 'c', 'd', 'e'), ('a', 'b', 'c', 'd', 'e'), ('a', 'b', 'c', 'd', 'e'), ('f', 'g', 'h', 'i', 'j'), ('f', 'g', 'h', 'i', 'j'), ('f', 'g', 'h', 'i', 'j'), ('f', 'g', 'h', 'i', 'j'), ('f', 'g', 'h', 'i', 'j'), ('k', 'l', 'm', 'n', 'o'), ('k', 'l', 'm', 'n', 'o'), ('k', 'l', 'm', 'n', 'o'), ('k', 'l', 'm', 'n', 'o'), ('k', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('p', 'q', 'r', 's', 't'), ('p', 'q', 'r', 's', 't'), ('p', 'q', 'r', 's', 't'), ('p', 'q', 'r', 's', 't'), ('u', 'v', 'w', 'x', 'y'), ('u', 'v', 'w', 'x', 'y'), ('u', 'v', 'w', 'x', 'y'), ('u', 'v', 'w', 'x', 'y'), ('u', 'v', 'w', 'x', 'y')]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> b
{('k', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'v', 'w', 'x', 'y'), ('f', 'g', 'h', 'i', 'j'), ('a', 'b', 'c', 'd', 'e')}
>>> list(b)
[('k', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'v', 'w', 'x', 'y'), ('f', 'g', 'h', 'i', 'j'), ('a', 'b', 'c', 'd', 'e')]
>>> g=[]
>>> for i in b:
	g.append(i)

	
>>> 
>>> g
[('k', 'l', 'm', 'n', 'o'), ('p', 'q', 'r', 's', 't'), ('u', 'v', 'w', 'x', 'y'), ('f', 'g', 'h', 'i', 'j'), ('a', 'b', 'c', 'd', 'e')]
>>> g=[]
>>> for i in b:
	g.append(list(i))

	
>>> g
[['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['f', 'g', 'h', 'i', 'j'], ['a', 'b', 'c', 'd', 'e']]
>>> g=[]
>>> for i in b:
	g.append(list(i))
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> ll
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> ss
['u', 'v', 'w', 'x', 'y']
>>> dd
['p', 'q', 'r', 's', 't']
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> d
[None, None, None, None, None]
>>> s
[None, None, None, None, None]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> ll
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> g
[['f', 'g', 'h', 'i', 'j'], ['a', 'b', 'c', 'd', 'e'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> ll_
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> g_
[['f', 'g', 'h', 'i', 'j'], ['a', 'b', 'c', 'd', 'e'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py", line 28, in <module>
    ll=ll_
NameError: name 'll_' is not defined
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> ll
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> ll_
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> ll
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> ll_
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> ll
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> ll_
(['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'])
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> ll_
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> ll
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> ss
['u', 'v', 'w', 'x', 'y']
>>> gg
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    gg
NameError: name 'gg' is not defined
>>> d
[]
>>> dd
['u', 'v', 'w', 'x', 'y']
>>> ll_
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> gg_
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    gg_
NameError: name 'gg_' is not defined
>>> g_
[['f', 'g', 'h', 'i', 'j'], ['p', 'q', 'r', 's', 't'], ['k', 'l', 'm', 'n', 'o'], ['a', 'b', 'c', 'd', 'e'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> ll
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> s
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> d
[['a', 'b', 'c', 'd', 'e'], ['p', 'q', 'r', 's', 't'], ['f', 'g', 'h', 'i', 'j'], ['u', 'v', 'w', 'x', 'y'], ['k', 'l', 'm', 'n', 'o']]
>>> ll
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]

>>> g
[['a', 'b', 'c', 'd', 'e'], ['p', 'q', 'r', 's', 't'], ['f', 'g', 'h', 'i', 'j'], ['u', 'v', 'w', 'x', 'y'], ['k', 'l', 'm', 'n', 'o']]
>>> b
{('a', 'b', 'c', 'd', 'e'), ('p', 'q', 'r', 's', 't'), ('f', 'g', 'h', 'i', 'j'), ('u', 'v', 'w', 'x', 'y'), ('k', 'l', 'm', 'n', 'o')}
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> b
{('a', 'b', 'c', 'd', 'e'), ('p', 'q', 'r', 's', 't'), ('f', 'g', 'h', 'i', 'j'), ('u', 'v', 'w', 'x', 'y'), ('k', 'l', 'm', 'n', 'o')}
>>> ll
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> g
[['a', 'b', 'c', 'd', 'e'], ['p', 'q', 'r', 's', 't'], ['f', 'g', 'h', 'i', 'j'], ['u', 'v', 'w', 'x', 'y'], ['k', 'l', 'm', 'n', 'o']]
>>> 
KeyboardInterrupt
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> ll
[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
>>> g
[['p', 'q', 'r', 's', 't'], ['f', 'g', 'h', 'i', 'j'], ['u', 'v', 'w', 'x', 'y'], ['k', 'l', 'm', 'n', 'o'], ['a', 'b', 'c', 'd', 'e']]
>>> b
{('p', 'q', 'r', 's', 't'), ('f', 'g', 'h', 'i', 'j'), ('u', 'v', 'w', 'x', 'y'), ('k', 'l', 'm', 'n', 'o'), ('a', 'b', 'c', 'd', 'e')}
>>> lll
[['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y'], ['u', 'v', 'w', 'x', 'y']]
>>> 
= RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\Grid_challenge.py
1
5
ebacd
fghij
olmkn
trpqs
xywuv
>>> lll
[['e', 'b', 'a', 'c', 'd'], ['e', 'b', 'a', 'c', 'd'], ['e', 'b', 'a', 'c', 'd'], ['e', 'b', 'a', 'c', 'd'], ['e', 'b', 'a', 'c', 'd'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['f', 'g', 'h', 'i', 'j'], ['o', 'l', 'm', 'k', 'n'], ['o', 'l', 'm', 'k', 'n'], ['o', 'l', 'm', 'k', 'n'], ['o', 'l', 'm', 'k', 'n'], ['o', 'l', 'm', 'k', 'n'], ['t', 'r', 'p', 'q', 's'], ['t', 'r', 'p', 'q', 's'], ['t', 'r', 'p', 'q', 's'], ['t', 'r', 'p', 'q', 's'], ['t', 'r', 'p', 'q', 's'], ['x', 'y', 'w', 'u', 'v'], ['x', 'y', 'w', 'u', 'v'], ['x', 'y', 'w', 'u', 'v'], ['x', 'y', 'w', 'u', 'v'], ['x', 'y', 'w', 'u', 'v']]
>>> ll
[['e', 'b', 'a', 'c', 'd'], ['f', 'g', 'h', 'i', 'j'], ['o', 'l', 'm', 'k', 'n'], ['t', 'r', 'p', 'q', 's'], ['x', 'y', 'w', 'u', 'v']]
>>> g
[['o', 'l', 'm', 'k', 'n'], ['e', 'b', 'a', 'c', 'd'], ['f', 'g', 'h', 'i', 'j'], ['t', 'r', 'p', 'q', 's'], ['x', 'y', 'w', 'u', 'v']]
>>> b
{('o', 'l', 'm', 'k', 'n'), ('e', 'b', 'a', 'c', 'd'), ('f', 'g', 'h', 'i', 'j'), ('t', 'r', 'p', 'q', 's'), ('x', 'y', 'w', 'u', 'v')}
>>> 