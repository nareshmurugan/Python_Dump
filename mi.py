Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: D:\PYTHON\naresh codes\snake game.py ================
going left
going right
going left
going up
going right
going down
going left
going up
going right
Traceback (most recent call last):
  File "D:\PYTHON\naresh codes\snake game.py", line 164, in <module>
    game.nextFrame()
  File "D:\PYTHON\naresh codes\snake game.py", line 113, in nextFrame
    game.screen.listen()
  File "D:\PYTHON\Lib\turtle.py", line 1438, in listen
    self._listen()
  File "D:\PYTHON\Lib\turtle.py", line 710, in _listen
    self.cv.focus_force()
  File "D:\PYTHON\Lib\turtle.py", line 426, in focus_force
    self._canvas.focus_force()
  File "D:\PYTHON\Lib\tkinter\__init__.py", line 737, in focus_force
    self.tk.call('focus', '-force', self._w)
_tkinter.TclError: can't invoke "focus" command: application has been destroyed
>>> 
================= RESTART: D:\PYTHON\naresh codes\snake game.py ================
Traceback (most recent call last):
  File "D:\PYTHON\naresh codes\snake game.py", line 164, in <module>
    game.nextFrame()
  File "D:\PYTHON\naresh codes\snake game.py", line 132, in nextFrame
    self.snake.drawself(self.artist)
  File "D:\PYTHON\naresh codes\snake game.py", line 96, in drawself
    segment.drawself(turtle)
  File "D:\PYTHON\naresh codes\snake game.py", line 14, in drawself
    turtle.begin_fill('red')
TypeError: begin_fill() takes 1 positional argument but 2 were given
>>> 
>>> 
>>> 
>>> 
>>> x:x*2 for x in range(10)
SyntaxError: invalid syntax
>>> (x:x*2 for x in range(10))
SyntaxError: invalid syntax
>>> (x*2 for x in range(10))
<generator object <genexpr> at 0x0000020DA5E1DE40>
>>> 0x0000020DA5E1DE40
2257640873536
>>> 
>>> type(2257640873536)
<class 'int'>
>>> (x:x*2 for x in range(10))
SyntaxError: invalid syntax
>>> l=(x*2 for x in range(10))
>>> print(l)
<generator object <genexpr> at 0x0000020DA5E1DE40>
>>> l=(x:x*2 for x in range(10))
SyntaxError: invalid syntax
>>> l=(x:x*2 for x in range(10))
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> l=[1,2,3,4,45]
>>> for i in l:
	m=dict(i)

	
Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    m=dict(i)
TypeError: 'int' object is not iterable
>>> for i in l:
	m={}
	m=dict(i)

	
Traceback (most recent call last):
  File "<pyshell#23>", line 3, in <module>
    m=dict(i)
TypeError: 'int' object is not iterable
>>> for i in l:
	m={}
	m=dict(i)

	
Traceback (most recent call last):
  File "<pyshell#25>", line 3, in <module>
    m=dict(i)
TypeError: 'int' object is not iterable
>>> for i in range(len(l)):
	m={}
	m=dict(i)

	
Traceback (most recent call last):
  File "<pyshell#27>", line 3, in <module>
    m=dict(i)
TypeError: 'int' object is not iterable
>>> for i in l:
	print(l)

	
[1, 2, 3, 4, 45]
[1, 2, 3, 4, 45]
[1, 2, 3, 4, 45]
[1, 2, 3, 4, 45]
[1, 2, 3, 4, 45]
>>> for i in l[]:
	
SyntaxError: invalid syntax
>>> for i in l:
	m=[]
	m.append(i)

	
>>> m
[45]
>>> for l in i:
	m=[]
	m.append(i)

	
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for l in i:
TypeError: 'int' object is not iterable
>>> for i in len(l):
	m=[]
	m.append(i)

	
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    for i in len(l):
TypeError: 'int' object is not iterable
>>> for i in len(l):
	m=[]
	m.append(i)

	
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    for i in len(l):
TypeError: 'int' object is not iterable
>>> for i in l:
	m=[]
	m.append(i)

	
>>> m
[45]
>>> for i in l:
	print(i)

	
1
2
3
4
45
>>> for i in l:
	m.append(i)
	print(m)
	i+=1

	
[45, 1]
[45, 1, 2]
[45, 1, 2, 3]
[45, 1, 2, 3, 4]
[45, 1, 2, 3, 4, 45]
>>> for i in l:
	m.append(i)
	print(m)
	i-=1

	
[45, 1, 2, 3, 4, 45, 1]
[45, 1, 2, 3, 4, 45, 1, 2]
[45, 1, 2, 3, 4, 45, 1, 2, 3]
[45, 1, 2, 3, 4, 45, 1, 2, 3, 4]
[45, 1, 2, 3, 4, 45, 1, 2, 3, 4, 45]
>>> for i in l:
	m.append(i)
	i+=1

	
>>> m
[45, 1, 2, 3, 4, 45, 1, 2, 3, 4, 45, 1, 2, 3, 4, 45]
>>> for i in l:
	m.append(i)

	
>>> m
[45, 1, 2, 3, 4, 45, 1, 2, 3, 4, 45, 1, 2, 3, 4, 45, 1, 2, 3, 4, 45]
>>> 
================================ RESTART: Shell ================================
>>> l=[1,2,3,4,5]
>>> m=[]
>>> for i in l:
	m.append(i)

	
>>> m
[1, 2, 3, 4, 5]
>>> for i in l
SyntaxError: invalid syntax
>>> for i in m:
	if(i<m[i]):
		print(i)

		
1
2
3
4
Traceback (most recent call last):
  File "<pyshell#71>", line 2, in <module>
    if(i<m[i]):
IndexError: list index out of range
>>> for i in m:
	if(i<l[i]):
		print(i)

		
1
2
3
4
Traceback (most recent call last):
  File "<pyshell#73>", line 2, in <module>
    if(i<l[i]):
IndexError: list index out of range
>>> for i in m:
	if(i>l[i]):
		print(i)

		
Traceback (most recent call last):
  File "<pyshell#75>", line 2, in <module>
    if(i>l[i]):
IndexError: list index out of range
>>> for i in m:
	if(i>l[i]):
		print(i)

		
Traceback (most recent call last):
  File "<pyshell#77>", line 2, in <module>
    if(i>l[i]):
IndexError: list index out of range
>>> dict()
{}
>>> 
>>> 
>>> 
>>> 
>>> for i in l:
	n={}
	n[i]=i
	print(n)

	
{1: 1}
{2: 2}
{3: 3}
{4: 4}
{5: 5}
>>> l=[1,6,7,8,9]
>>> for i in l:
	n={}
	n[i]=i
	print(n)

	
{1: 1}
{6: 6}
{7: 7}
{8: 8}
{9: 9}
>>> for i in l:
	n={}
	n[i]=l[i]
	print(n)

	
{1: 6}
Traceback (most recent call last):
  File "<pyshell#95>", line 3, in <module>
    n[i]=l[i]
IndexError: list index out of range
>>> for i&j in l:
	n={}
	n[i]=l[j]
	print(n)
	
SyntaxError: cannot assign to operator
>>> for i and j in l:
	n={}
	n[i]=l[j]
	print(n)
	
SyntaxError: invalid syntax
>>> for i in l and n:
	n={}
	n[i]=l[j]
	print(n)

	
>>> for i in l and n:
	n={}
	n[i]=l[j]
	print(n and l)

	
>>> l
[1, 6, 7, 8, 9]
>>> m
[1, 2, 3, 4, 5]
>>> for i in l:
	n[i]=l[i]
	print(n)

	
{1: 6}
Traceback (most recent call last):
  File "<pyshell#107>", line 2, in <module>
    n[i]=l[i]
IndexError: list index out of range
>>> while(i<=1):
	n[i]=l[i]
	print(n)

	
>>> n
{1: 6}
>>> n
{1: 6}
>>> i=1,while(i<=1):
	n[i]=l[i]
	print(n)
	
SyntaxError: invalid syntax
>>> i=1;while(i<=1):
	n[i]=l[i]
	print(n)
	
SyntaxError: invalid syntax
>>> 
i=1
while(i<=1):
	n[i]=l[i]
	print(n)
	
SyntaxError: multiple statements found while compiling a single statement
>>> i=1
while(i<=1):
	n[i]=l[i]
	print(n)
	
SyntaxError: multiple statements found while compiling a single statement
>>> i=1
while(i<=1):
	n[i]=l[i]
	print(n)
	
SyntaxError: multiple statements found while compiling a single statement
>>> i=1
	while(i<=1):
		n[i]=l[i]
		print(n)
		
SyntaxError: multiple statements found while compiling a single statement
>>> i=1
>>> while(i<=1):
	n[i]=l[i]
	print(n)
	i+=1

	
{1: 6}
>>> while(i<=1):
	n[i]=l[i]
	print(n)
	i+=1

	
>>> 
>>> n
{1: 6}
>>> while(i>=1):
	n[i]=l[i]
	print(n)
	i+=1

	
{1: 6, 2: 7}
{1: 6, 2: 7, 3: 8}
{1: 6, 2: 7, 3: 8, 4: 9}
Traceback (most recent call last):
  File "<pyshell#129>", line 2, in <module>
    n[i]=l[i]
IndexError: list index out of range
>>> while(i>=len(l)):
	n[i]=l[i]
	print(n)
	i+=1

	
Traceback (most recent call last):
  File "<pyshell#131>", line 2, in <module>
    n[i]=l[i]
IndexError: list index out of range
>>> for i in range(len(l)):
	n[i]=l[i]
	print(n)
	i+=1

	
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
>>> n
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
>>> for i in range(len(l)):
	n[i]=l[i]
	print(n)

	
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}

>>> for i in range(1,len(l)):
	n[i]=l[i]

	
>>> 
>>> n
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
>>> for i in range(2,len(l)):
	n[i]=l[i]

	
>>> n
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
>>> 
>>> 
>>> for i in range(len(l),len(l)):
	n[i]=l[i]

	
>>> n
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
>>> for i in range(len(l),len(l),len(l)):
	n[i]=l[i]

	
>>> n
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
>>> 
>>> 
>>> 
>>> 
>>> for i in range(len(l),len(l),len(l)):
	n[i]=l[i]
	print(n)
	i+=1

	
>>> n
{1: 6, 2: 7, 3: 8, 4: 9, 0: 1}
>>> 