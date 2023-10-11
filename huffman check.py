Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sengathir
Enter the probabilities in spaces sepreated	0.5 0.125 0.125 0.0625 0.0625 0.0625 0.03125 0.03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [1, 0.125]   [16, 0.2]   [11, 0.2]   [17, 0.3, 0]   [0, 0.5, 1]   

[2, 0.125]   [2, 0.125]   [2, 0.125]   [1, 0.125]   [16, 0.2, 0]   [11, 0.2, 1]   0   

[3, 0.0625]   [13, 0.1]   [9, 0.1]   [2, 0.125, 0]   [1, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.1, 0]   [9, 0.1, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import sengathir
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 72, in <module>
    cl.append(len(y[0]))
IndexError: list index out of range
>>> cl
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    cl
NameError: name 'cl' is not defined
>>> y
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.4 0.2 0.2 0.1 0.1


[0, 0.4]   [0, 0.4]   [3, 0.4]   [7, 0.6, 0]   

[1, 0.2]   [7, 0.2]   [0, 0.4, 0]   [3, 0.4, 1]   

[2, 0.2]   [1, 0.2, 0]   [7, 0.2, 1]   0   

[3, 0.1, 0]   [2, 0.2, 1]   0   0   

[4, 0.1, 1]   0   0   0   

code word  ['00'] ['01'] ['11'] ['010'] ['110']
code length  2 2 2 3 3
Efficiency  96
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.2 0.1 0.1 0.1 


[0, 0.5]   [0, 0.5]   [0, 0.5]   [10, 0.5, 0]   

[1, 0.2]   [7, 0.2]   [3, 0.3, 0]   [0, 0.5, 1]   

[2, 0.1]   [1, 0.2, 0]   [7, 0.2, 1]   0   

[3, 0.1, 0]   [2, 0.1, 1]   0   0   

[4, 0.1, 1]   0   0   0   

Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 72, in <module>
    cl.append(len(y[0]))
IndexError: list index out of range
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\hufffinal.py ===
>>> code
[['00'], ['01'], ['11'], ['0010'], ['1010'], ['0110'], ['1110']]
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.2 0.1 0.1 0.1


[0, 0.5]   [0, 0.5]   [0, 0.5]   [10, 0.5, 0]   

[1, 0.2]   [7, 0.2]   [3, 0.3, 0]   [0, 0.5, 1]   

[2, 0.1]   [1, 0.2, 0]   [7, 0.2, 1]   0   

[3, 0.1, 0]   [2, 0.1, 1]   0   0   

[4, 0.1, 1]   0   0   0   

Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 72, in <module>
    cl.append(len(y[0]))
IndexError: list index out of range
>>> code
[[], ['000'], ['100'], ['010', '00'], ['110']]
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.3 0.3 0.3 0.4 0.6


[0, 0.6]   [7, 0.6]   [3, 0.7]   [7, 1.2, 0]   

[1, 0.4]   [0, 0.6]   [7, 0.6, 0]   [3, 0.7, 1]   

[2, 0.3]   [1, 0.4, 0]   [0, 0.6, 1]   0   

[3, 0.3, 0]   [2, 0.3, 1]   0   0   

[4, 0.3, 1]   0   0   0   

code word  ['10'] ['01'] ['11'] ['000'] ['100']
code length  2 2 2 3 3
Efficiency  58
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.3 0.2 0.2 0.1 0.1 0.l
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 6, in <module>
    a=list(map(float,input("Enter the probabilities in spaces sepreated\t").split()))
ValueError: could not convert string to float: '0.l'
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.3 0.2 0.2 0.1 0.1 0.1


[0, 0.3]   [0, 0.3]   [5, 0.3]   [10, 0.4]   [5, 0.6, 0]   

[1, 0.2]   [9, 0.2]   [0, 0.3]   [5, 0.3, 0]   [10, 0.4, 1]   

[2, 0.2]   [1, 0.2]   [9, 0.2, 0]   [0, 0.3, 1]   0   

[3, 0.1]   [2, 0.2, 0]   [1, 0.2, 1]   0   0   

[4, 0.1, 0]   [3, 0.1, 1]   0   0   0   

[5, 0.1, 1]   0   0   0   0   

code word  ['10'] ['11'] ['000'] ['100'] ['001'] ['101', '00']
code length  2 2 3 3 3 3
Efficiency  98
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.2 0.1 0.1 0.1


[0, 0.5]   [0, 0.5]   [0, 0.5]   [10, 0.5, 0]   

[1, 0.2]   [7, 0.2]   [3, 0.3, 0]   [0, 0.5, 1]   

[2, 0.1]   [1, 0.2, 0]   [7, 0.2, 1]   0   

[3, 0.1, 0]   [2, 0.1, 1]   0   0   

[4, 0.1, 1]   0   0   0   

Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 72, in <module>
    cl.append(len(y[0]))
IndexError: list index out of range
>>> code
[[], ['000'], ['100'], ['010', '00'], ['110']]
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.2 0.1 0.1 0.1


[0, 0.5]   [0, 0.5]   [0, 0.5]   [10, 0.5, 0]   

[1, 0.2]   [7, 0.2]   [3, 0.3, 0]   [0, 0.5, 1]   

[2, 0.1]   [1, 0.2, 0]   [7, 0.2, 1]   0   

[3, 0.1, 0]   [2, 0.1, 1]   0   0   

[4, 0.1, 1]   0   0   0   

Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 72, in <module>
    cl.append(len(y[0]))
IndexError: list index out of range
>>> code
[[], ['000'], ['100'], ['010', '00'], ['110']]
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.2 0.1 0.1 0.1


[0, 0.5]   [0, 0.5]   [0, 0.5]   [10, 0.5, 0]   

[1, 0.2]   [7, 0.2]   [3, 0.3, 0]   [0, 0.5, 1]   

[2, 0.1]   [1, 0.2, 0]   [7, 0.2, 1]   0   

[3, 0.1, 0]   [2, 0.1, 1]   0   0   

[4, 0.1, 1]   0   0   0   

Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 71, in <module>
    cl.append(len(y[0]))
IndexError: list index out of range
>>> code
[[], ['000'], ['100'], ['010', '00'], ['110']]
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.2 0.1 0.1 0.1
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 24, in <module>
    l[j][-2:]=[[l[j][-2][0],l[j][-2][1],0],[l[j][-1][0],l[j][-1][1],1]]
IndexError: list index out of range
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.2 0.1 0.1 0.1
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 24, in <module>
    l[j][-2:]=[[l[j][-2][0],l[j][-2][1],0],[l[j][-1][0],l[j][-1][1],1]]
IndexError: list index out of range
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.125 0.125 0.0625 0.0625 0.0625 0.0625 0.03125 0.03125 


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [36, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [1, 0.125]   [1, 0.125]   [26, 0.2]   [9, 0.2]   [27, 0.3, 0]   [0, 0.5, 1]   

[2, 0.125]   [2, 0.125]   [2, 0.125]   [2, 0.125]   [1, 0.125]   [26, 0.2, 0]   [9, 0.2, 1]   0   

[3, 0.0625]   [15, 0.1]   [11, 0.1]   [7, 0.1]   [2, 0.125, 0]   [1, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [15, 0.1]   [11, 0.1, 0]   [7, 0.1, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625]   [3, 0.0625, 0]   [15, 0.1, 1]   0   0   0   0   

[6, 0.0625]   [5, 0.0625, 0]   [4, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 0]   [6, 0.0625, 1]   0   0   0   0   0   0   

[8, 0.03125, 1]   0   0   0   0   0   0   0   

Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 72, in <module>
    cl.append(len(y[0]))
IndexError: list index out of range
>>> code
[[], ['100'], ['010'], ['0110'], ['1110'], ['00000'], ['10000'], ['01000', '110'], ['11000']]
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.125 0.125 0.0625 0.0625 0.0625 0.0625 0.03125 0.03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [36, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [1, 0.125]   [1, 0.125]   [26, 0.2]   [9, 0.2]   [27, 0.3, 0]   [0, 0.5, 1]   

[2, 0.125]   [2, 0.125]   [2, 0.125]   [2, 0.125]   [1, 0.125]   [26, 0.2, 0]   [9, 0.2, 1]   0   

[3, 0.0625]   [15, 0.1]   [11, 0.1]   [7, 0.1]   [2, 0.125, 0]   [1, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [15, 0.1]   [11, 0.1, 0]   [7, 0.1, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625]   [3, 0.0625, 0]   [15, 0.1, 1]   0   0   0   0   

[6, 0.0625]   [5, 0.0625, 0]   [4, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 0]   [6, 0.0625, 1]   0   0   0   0   0   0   

[8, 0.03125, 1]   0   0   0   0   0   0   0   

Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 76, in <module>
    cl.append(len(y[0]))
TypeError: object of type 'int' has no len()
>>> code
[[1], ['100'], ['010'], ['0110'], ['1110'], ['00000'], ['10000'], ['01000', '110'], ['11000']]
>>> y
[1]
>>> len([1])
1
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.125 0.125 0.0625 0.0625 0.0625 0.0625 0.03125 0.03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [36, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [1, 0.125]   [1, 0.125]   [26, 0.2]   [9, 0.2]   [27, 0.3, 0]   [0, 0.5, 1]   

[2, 0.125]   [2, 0.125]   [2, 0.125]   [2, 0.125]   [1, 0.125]   [26, 0.2, 0]   [9, 0.2, 1]   0   

[3, 0.0625]   [15, 0.1]   [11, 0.1]   [7, 0.1]   [2, 0.125, 0]   [1, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [15, 0.1]   [11, 0.1, 0]   [7, 0.1, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625]   [3, 0.0625, 0]   [15, 0.1, 1]   0   0   0   0   

[6, 0.0625]   [5, 0.0625, 0]   [4, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 0]   [6, 0.0625, 1]   0   0   0   0   0   0   

[8, 0.03125, 1]   0   0   0   0   0   0   0   

code word  ['1'] ['100'] ['010'] ['0110'] ['1110'] ['00000'] ['10000'] ['01000', '110'] ['11000']
code length  1 3 3 4 4 5 5 5 5
Efficiency  95
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.125 0.125 0.0625 0.0625 0.0625 0.03125 0.03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [1, 0.125]   [16, 0.2]   [11, 0.2]   [17, 0.3, 0]   [0, 0.5, 1]   

[2, 0.125]   [2, 0.125]   [2, 0.125]   [1, 0.125]   [16, 0.2, 0]   [11, 0.2, 1]   0   

[3, 0.0625]   [13, 0.1]   [9, 0.1]   [2, 0.125, 0]   [1, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.1, 0]   [9, 0.1, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   

code word  ['1'] ['100'] ['010'] ['1000'] ['0110'] ['1110'] ['00000'] ['10000']
code length  1 3 3 4 4 4 5 5
Efficiency  101
>>> ef
101
>>> al
2.3000000000000003
>>> h
2.3125
>>> h/al
1.0054347826086956
>>> h/al*100
100.54347826086956
>>> 
=== RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ===
Enter the probabilities in spaces sepreated	0.5 0.125 0.125 0.0625 0.0625 0.0625 0.03125 0.03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [1, 0.125]   [16, 0.2]   [11, 0.2]   [17, 0.3, 0]   [0, 0.5, 1]
   

[2, 0.125]   [2, 0.125]   [2, 0.125]   [1, 0.125]   [16, 0.2, 0]   [11, 0.2, 1]   0   

[3, 0.0625]   [13, 0.1]   [9, 0.1]   [2, 0.125, 0]   [1, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.1, 0]   [9, 0.1, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   

code word  ['1'] ['100'] ['010'] ['1000'] ['0110'] ['1110'] ['00000'] ['10000']
code length  1 3 3 4 4 4 5 5
Efficiency  100
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	0.5 0.2 0.1 0.1 0.1


[0, 0.5]   [0, 0.5]   [0, 0.5]   [10, 0.5, 0]   

[1, 0.2]   [7, 0.2]   [3, 0.3, 0]   [0, 0.5, 1]   

[2, 0.1]   [1, 0.2, 0]   [7, 0.2, 1]   0   

[3, 0.1, 0]   [2, 0.1, 1]   0   0   

[4, 0.1, 1]   0   0   0   

code word  ['1'] ['000'] ['100'] ['010', '00'] ['110']
code length  1 3 3 3 3
Efficiency  98
>>> 
============================= RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py =============================
Enter the probabilities in spaces sepreated	0.25 0.25 0.125 0.125 0.125 0.125


[0, 0.25]   [0, 0.25]   [0, 0.25]   [14, 0.4]   [1, 0.5, 0]   

[1, 0.25]   [1, 0.25]   [1, 0.25]   [0, 0.25, 0]   [14, 0.4, 1]   

[2, 0.125]   [9, 0.2]   [5, 0.2, 0]   [1, 0.25, 1]   0   

[3, 0.125]   [2, 0.125, 0]   [9, 0.2, 1]   0   0   

[4, 0.125, 0]   [3, 0.125, 1]   0   0   0   

[5, 0.125, 1]   0   0   0   0   

code word  ['00'] ['10'] ['001'] ['101'] ['011'] ['111', '01']
code length  2 2 3 3 3 3
Efficiency  96
>>> 
============================= RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py =============================
Enter the probabilities in spaces sepreated	0.25 0.25 0.125 0.125 0.125 0.125


[0, 0.25]   [9, 0.25]   [5, 0.25]   [1, 0.5]   [14, 0.5, 0]   

[1, 0.25]   [0, 0.25]   [9, 0.25]   [5, 0.25, 0]   [1, 0.5, 1]   

[2, 0.125]   [1, 0.25]   [0, 0.25, 0]   [9, 0.25, 1]   0   

[3, 0.125]   [2, 0.125, 0]   [1, 0.25, 1]   0   0   

[4, 0.125, 0]   [3, 0.125, 1]   0   0   0   

[5, 0.125, 1]   0   0   0   0   

code word  ['01'] ['11'] ['0'] ['1'] ['0'] ['1', '00']
code length  2 2 1 1 1 1
Efficiency  179
>>> 
============================= RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py =============================
Enter the probabilities in spaces sepreated	0.4 0.2 0.2 0.1 0.1


[0, 0.4]   [0, 0.4]   [3, 0.4]   [7, 0.6000000000000001, 0]   

[1, 0.2]   [7, 0.2]   [0, 0.4, 0]   [3, 0.4, 1]   

[2, 0.2]   [1, 0.2, 0]   [7, 0.2, 1]   0   

[3, 0.1, 0]   [2, 0.2, 1]   0   0   

[4, 0.1, 1]   0   0   0   

code word  ['0'] ['01'] ['11'] ['01'] ['11']
code length  1 2 2 2 2
Efficiency  133
>>> 
============================= RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py =============================
Enter the probabilities in spaces sepreated	.5
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py", line 13, in <module>
    p=a[-1][1]+a[-2][1];_p=a[-1][0]+a[-2][0]
IndexError: list index out of range
>>> 
============================= RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py =============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125]   [3, 0.25]   [25, 0.25, 0]   [0, 0.5, 1]   

[2, 0.125]   [2, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125, 0]   [3, 0.25, 1]   0   

[3, 0.0625]   [13, 0.0625]   [2, 0.125]   [1, 0.125, 0]   [9, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.0625, 0]   [2, 0.125, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   

Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py", line 71, in <module>
    cl.append(len(y[0]))
IndexError: list index out of range
>>> 
============================= RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py =============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125]   [3, 0.25]   [25, 0.25, 0]   [0, 0.5, 1]   

[2, 0.125]   [2, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125, 0]   [3, 0.25, 1]   0   

[3, 0.0625]   [13, 0.0625]   [2, 0.125]   [1, 0.125, 0]   [9, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.0625, 0]   [2, 0.125, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   

code word  ['1'] ['0'] ['1'] ['1', '10'] ['0'] ['1'] ['0'] ['1']
code length  1 1 1 1 1 1 1 1
Efficiency  231
>>> 
============================= RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py =============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [1, 0.125]   [1, 0.125, 1]   

[2, 0.125]   [2, 0.125]   [2, 0.125, 0]   0   

[3, 0.0625]   [3, 0.0625]   [3, 0.0625, 1]   0   

[4, 0.0625]   [4, 0.0625, 0]   0   0   

code word  ['1'] ['1'] ['0'] ['1'] ['0'] ['1'] ['0'] ['1']
code length  1 1 1 1 1 1 1 1
Efficiency  231
>>> 
============================= RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py =============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [1, 0.125]   [1, 0.125, 1]   

[2, 0.125]   [2, 0.125]   [2, 0.125, 0]   0   

[3, 0.0625]   [3, 0.0625]   [3, 0.0625, 1]   0   

[4, 0.0625]   [4, 0.0625, 0]   0   0   

code word  ['1'] ['1'] ['0'] ['1'] ['0'] ['1'] ['0'] ['1']
code length  1 1 1 1 1 1 1 1
Efficiency  231
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [1, 0.125]   [16, 0.2]   [11, 0.2]   [17, 0.3, 0]   [0, 0.5, 1]   

[2, 0.125]   [2, 0.125]   [2, 0.125]   [1, 0.125]   [16, 0.2, 0]   [11, 0.2, 1]   0   

[3, 0.0625]   [13, 0.1]   [9, 0.1]   [2, 0.125, 0]   [1, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.1, 0]   [9, 0.1, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   

code word  ['1'] ['100'] ['010'] ['1000'] ['0110'] ['1110'] ['00000'] ['10000']
code length  1 3 3 4 4 4 5 5
Efficiency  100
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 13, in <module>
    p=m.ceil(a[-1][1]+a[-2][1],1);_p=a[-1][0]+a[-2][0]
TypeError: ceil() takes exactly one argument (2 given)
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [13, 1]   [9, 1]   [5, 1]   [1, 1]   [22, 2]   [6, 2, 0]   

[1, 0.125]   [0, 0.5]   [13, 1]   [9, 1]   [5, 1]   [1, 1, 0]   [22, 2, 1]   

[2, 0.125]   [1, 0.125]   [0, 0.5]   [13, 1]   [9, 1, 0]   [5, 1, 1]   0   

[3, 0.0625]   [2, 0.125]   [1, 0.125]   [0, 0.5, 0]   [13, 1, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [2, 0.125, 0]   [1, 0.125, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   

code word  ['0'] ['1', '00'] ['0'] ['1'] ['0'] ['1', '10'] ['0'] ['1']
code length  1 1 1 1 1 1 1 1
Efficiency  231
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125]   [3, 0.25]   [25, 0.25, 0]   [0, 0.5, 1]   

[2, 0.125]   [2, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125, 0]   [3, 0.25, 1]   0   

[3, 0.0625]   [13, 0.0625]   [2, 0.125]   [1, 0.125, 0]   [9, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.0625, 0]   [2, 0.125, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   

code word  ['1'] ['0'] ['1'] ['1', '10'] ['0'] ['1'] ['0'] ['1']
code length  1 1 1 1 1 1 1 1
Efficiency  231
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	0.3 0.2 0.2 0.2 0.1
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 13, in <module>
    p=round(a[-1][1]+a[-2][1]);_p=a[-1][0]+a[-2][0]
IndexError: list index out of range
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 24, in <module>
    l[j][-2:]=[[l[j][-2][0],l[j][-2][1],0],[l[j][-1][0],l[j][-1][1],1]]
IndexError: list index out of range
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	0.3 0.2 0.2 0.2 0.1


[0, 0.3]   [7, 0.3]   [3, 0.4]   [7, 0.6, 0]   

[1, 0.2]   [0, 0.3]   [7, 0.3, 0]   [3, 0.4, 1]   

[2, 0.2]   [1, 0.2, 0]   [0, 0.3, 1]   0   

[3, 0.2, 0]   [2, 0.2, 1]   0   0   

[4, 0.1, 1]   0   0   0   

code word  ['10'] ['01'] ['11'] ['000'] ['100']
code length  2 2 2 3 3
Efficiency  97
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125]   [3, 0.25]   [25, 0.25, 0]   [0, 0.5, 1]   

[2, 0.125]   [2, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125, 0]   [3, 0.25, 1]   0   

[3, 0.0625]   [13, 0.0625]   [2, 0.125]   [1, 0.125, 0]   [9, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.0625, 0]   [2, 0.125, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   

code word  ['1'] ['0'] ['1'] ['1', '10'] ['0'] ['1'] ['0'] ['1']
code length  1 1 1 1 1 1 1 1
Efficiency  231
>>> s
[13, 0.1]
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   

[1, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125]   [3, 0.25]   [25, 0.25, 0]   [0, 0.5, 1]   

[2, 0.125]   [2, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125, 0]   [3, 0.25, 1]   0   

[3, 0.0625]   [13, 0.0625]   [2, 0.125]   [1, 0.125, 0]   [9, 0.125, 1]   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.0625, 0]   [2, 0.125, 1]   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   

code word  ['1'] ['010'] ['110'] ['10', '10'] ['01'] ['11'] ['00'] ['10']
code length  1 3 3 2 2 2 2 2
Efficiency  128
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1


[0, 0.5]   [0, 0.5]   [0, 0.5]   [10, 0.5, 0]   

[1, 0.2]   [7, 0.2]   [3, 0.30000000000000004, 0]   [0, 0.5, 1]   

[2, 0.1]   [1, 0.2, 0]   [7, 0.2, 1]   0   

[3, 0.1, 0]   [2, 0.1, 1]   0   0   

[4, 0.1, 1]   0   0   0   

code word  ['1'] ['000'] ['100'] ['010', '00'] ['110']
code length  1 3 3 3 3
Efficiency  98
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1

============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 24, in <module>
    l[j][-2:]=[[l[j][-2][0],l[j][-2][1],0],[l[j][-1][0],l[j][-1][1],1]]
IndexError: list index out of range
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 24, in <module>
    l[j][-2:]=[[l[j][-2][0],l[j][-2][1],0],[l[j][-1][0],l[j][-1][1],1]]
IndexError: list index out of range
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 26, in <module>
    l[j][-2:]=[[l[j][-2][0],l[j][-2][1],0],[l[j][-1][0],l[j][-1][1],1]]
IndexError: list index out of range
>>> l
[[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1, 0], [4, 0.1, 1]], [[0, 0.5], [7, 0.2], [1, 0.2, 0], [2, 0.1, 1]], [[0, 0.5], [3, 0.30000000000000004, 0], [7, 0.2, 1]], [[10, 0.5, 0], [0, 0.5, 1]], [[10, 1.0]]]
>>> for i in l:
	print(i)

	
[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1, 0], [4, 0.1, 1]]
[[0, 0.5], [7, 0.2], [1, 0.2, 0], [2, 0.1, 1]]
[[0, 0.5], [3, 0.30000000000000004, 0], [7, 0.2, 1]]
[[10, 0.5, 0], [0, 0.5, 1]]
[[10, 1.0]]
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1


[0, 0.5]   [0, 0.5]   [0, 0.5]   [10, 0.5, 0]   [10, 1.0]   

[1, 0.2]   [7, 0.2]   [3, 0.30000000000000004, 0]   [0, 0.5, 1]   0   

[2, 0.1]   [1, 0.2, 0]   [7, 0.2, 1]   0   0   

[3, 0.1, 0]   [2, 0.1, 1]   0   0   0   

[4, 0.1, 1]   0   0   0   0   

0   0   0   0   0   

Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 78, in <module>
    al=sum([round(float(pp[0][x][1]*cl[x]),1) for x in range(len(pp[0]))])
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 78, in <listcomp>
    al=sum([round(float(pp[0][x][1]*cl[x]),1) for x in range(len(pp[0]))])
TypeError: 'int' object is not subscriptable
>>> 
============================= RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py =============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py", line 13, in <module>
    p=round(a[-1][1]+a[-2][1]);_p=a[-1][0]+a[-2][0]
IndexError: list index out of range
>>> 
============================= RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py =============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/fffinal.py", line 13, in <module>
    p=round(a[-1][1]+a[-2][1]);_p=a[-1][0]+a[-2][0]
IndexError: list index out of range
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1


[0, 0.5]   [0, 0.5]   [0, 0.5]   [10, 0.5, 0]   [10, 1.0]   

[1, 0.2]   [7, 0.2]   [3, 0.30000000000000004, 0]   [0, 0.5, 1]   0   

[2, 0.1]   [1, 0.2, 0]   [7, 0.2, 1]   0   0   

[3, 0.1, 0]   [2, 0.1, 1]   0   0   0   

[4, 0.1, 1]   0   0   0   0   

0   0   0   0   0   

Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 78, in <module>
    al=sum([round(float(pp[0][x][1]*cl[x]),1) for x in range(len(pp[0]))])
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 78, in <listcomp>
    al=sum([round(float(pp[0][x][1]*cl[x]),1) for x in range(len(pp[0]))])
TypeError: 'int' object is not subscriptable
>>> j
[10, 1.0]
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 24, in <module>
    if len(j[1]==1.0):
TypeError: 'int' object is not subscriptable
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 24, in <module>
    if len(l[j][1]==1.0):
TypeError: object of type 'bool' has no len()
>>> 
============================ RESTART: C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py ============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\sengathir.py", line 24, in <module>
    if l[j][1]==1.0:
IndexError: list index out of range
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 6, in <module>
    a=list(map(float,input("Enter the probabilities in spaces sepreated\t").split()))
KeyboardInterrupt
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 24, in <module>
    if l[j][1]==1.0:
IndexError: list index out of range
>>> j
4
>>> l
[[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1, 0], [4, 0.1, 1]], [[0, 0.5], [7, 0.2], [1, 0.2, 0], [2, 0.1, 1]], [[0, 0.5], [3, 0.30000000000000004, 0], [7, 0.2, 1]], [[10, 0.5, 0], [0, 0.5, 1]], [[10, 1.0]]]
>>> len(l)
5
>>> l[-1]
[[10, 1.0]]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 24, in <module>
    for jj in j:
TypeError: 'int' object is not iterable
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 27, in <module>
    l[j][-2:]=[[l[j][-2][0],l[j][-2][1],0],[l[j][-1][0],l[j][-1][1],1]]
TypeError: list indices must be integers or slices, not list
>>> j
[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1], [4, 0.1]]
>>> jj
[4, 0.1]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 24, in <module>
    l[j][-2:]=[[l[j][-2][0],l[j][-2][1],0],[l[j][-1][0],l[j][-1][1],1]]
TypeError: list indices must be integers or slices, not list
>>> j
[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1], [4, 0.1]]
>>> jj
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    jj
NameError: name 'jj' is not defined
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 24, in <module>
    l[j][-2:]=[[l[j][-2][0],l[j][-2][1],0],[l[j][-1][0],l[j][-1][1],1]]
TypeError: list indices must be integers or slices, not list
>>> l
[[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1], [4, 0.1]], [[0, 0.5], [7, 0.2], [1, 0.2], [2, 0.1]], [[0, 0.5], [3, 0.30000000000000004], [7, 0.2]], [[10, 0.5], [0, 0.5]], [[10, 1.0]]]
>>> j
[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1], [4, 0.1]]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 24, in <module>
    j[-2:]=[[l[j][-2][0],l[j][-2][1],0],[l[j][-1][0],l[j][-1][1],1]]
TypeError: list indices must be integers or slices, not list
>>> j
[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1], [4, 0.1]]
>>> l
[[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1], [4, 0.1]], [[0, 0.5], [7, 0.2], [1, 0.2], [2, 0.1]], [[0, 0.5], [3, 0.30000000000000004], [7, 0.2]], [[10, 0.5], [0, 0.5]], [[10, 1.0]]]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 24, in <module>
    j[-2:]=[[j[-2][0],j[-2][1],0],[j[-1][0],j[-1][1],1]]
IndexError: list index out of range
>>> j[-2:]
[[10, 1.0]]
>>> j
[[10, 1.0]]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 24, in <module>
    j[-2:]=[[j[-2][0],j[-2][1],0],[j[-1][0],j[-1][1],1]]
IndexError: list index out of range
>>> j
[[10, 1.0]]
>>> l
[[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1, 0], [4, 0.1, 1]], [[0, 0.5], [7, 0.2], [1, 0.2, 0], [2, 0.1, 1]], [[0, 0.5], [3, 0.30000000000000004, 0], [7, 0.2, 1]], [[10, 0.5, 0], [0, 0.5, 1]], [[10, 1.0]]]
>>> for i in l:
	print(i)

	
[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1, 0], [4, 0.1, 1]]
[[0, 0.5], [7, 0.2], [1, 0.2, 0], [2, 0.1, 1]]
[[0, 0.5], [3, 0.30000000000000004, 0], [7, 0.2, 1]]
[[10, 0.5, 0], [0, 0.5, 1]]
[[10, 1.0]]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 24, in <module>
    j[-2:]=[[j[-2][0],j[-2][1],0],[j[-1][0],j[-1][1],1]]
IndexError: list index out of range
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 24, in <module>
    if j[1]==1.0:
IndexError: list index out of range
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 26, in <module>
    j[-2:]=[[j[-2][0],j[-2][1],0],[j[-1][0],j[-1][1],1]]
IndexError: list index out of range
>>> j
[[10, 1.0]]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
>>> l
[[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1, 0], [4, 0.1, 1]], [[0, 0.5], [7, 0.2], [1, 0.2, 0], [2, 0.1, 1]], [[0, 0.5], [3, 0.30000000000000004, 0], [7, 0.2, 1]], [[10, 0.5, 0], [0, 0.5, 1]], [[10, 1.0]]]
>>> j
[[10, 1.0]]
>>> for i in l:
	print(i)

	
[[0, 0.5], [1, 0.2], [2, 0.1], [3, 0.1, 0], [4, 0.1, 1]]
[[0, 0.5], [7, 0.2], [1, 0.2, 0], [2, 0.1, 1]]
[[0, 0.5], [3, 0.30000000000000004, 0], [7, 0.2, 1]]
[[10, 0.5, 0], [0, 0.5, 1]]
[[10, 1.0]]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	code
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 6, in <module>
    a=list(map(float,input("Enter the probabilities in spaces sepreated\t").split()))
ValueError: could not convert string to float: 'code'
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
>>> code
[[], ['000'], ['100'], ['010', '00'], ['110']]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125
>>> code
[[], ['010'], ['110'], ['10', '10'], ['01'], ['11'], ['00'], ['10']]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1
>>> code
[['1'], ['000'], ['100'], ['010', '00'], ['110']]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125
>>> code
[['1'], ['010'], ['110'], ['10', '10'], ['01'], ['11'], ['00'], ['10']]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125
>>> code
[['1'], ['010'], ['110'], ['10', '10'], ['01'], ['11'], ['00'], ['10']]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125
>>> code
[['1'], ['010'], ['110'], ['10', '10'], ['01'], ['11'], ['00'], ['10']]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125
>>> code
[['1'], ['010'], ['110'], ['1000', '10'], ['0100'], ['1100'], ['00000'], ['10000']]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   [28, 1.0]   

[1, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125]   [3, 0.25]   [25, 0.25, 0]   [0, 0.5, 1]   0   

[2, 0.125]   [2, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125, 0]   [3, 0.25, 1]   0   0   

[3, 0.0625]   [13, 0.0625]   [2, 0.125]   [1, 0.125, 0]   [9, 0.125, 1]   0   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.0625, 0]   [2, 0.125, 1]   0   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   0   

0   0   0   0   0   0   0   0   

Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 70, in <module>
    al=sum([round(float(pp[0][x][1]*cl[x]),1) for x in range(len(pp[0]))])
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 70, in <listcomp>
    al=sum([round(float(pp[0][x][1]*cl[x]),1) for x in range(len(pp[0]))])
TypeError: 'int' object is not subscriptable
>>> code
[['1'], ['010'], ['110'], ['1000', '10'], ['0100'], ['1100'], ['00000'], ['10000']]
>>> pp
[[[0, 0.5], [1, 0.125], [2, 0.125], [3, 0.0625], [4, 0.0625], [5, 0.0625], [6, 0.03125], [7, 0.03125], 0], [[0, 0.5], [1, 0.125], [2, 0.125], [13, 0.0625], [3, 0.0625], [4, 0.0625], [5, 0.0625], 0, 0], [[0, 0.5], [9, 0.125], [1, 0.125], [2, 0.125], [13, 0.0625], [3, 0.0625], 0, 0, 0], [[0, 0.5], [16, 0.125], [9, 0.125], [1, 0.125], [2, 0.125], 0, 0, 0, 0], [[0, 0.5], [3, 0.25], [16, 0.125], [9, 0.125], 0, 0, 0, 0, 0], [[0, 0.5], [25, 0.25], [3, 0.25], 0, 0, 0, 0, 0, 0], [[28, 0.5], [0, 0.5], 0, 0, 0, 0, 0, 0, 0], [[28, 1.0], 0, 0, 0, 0, 0, 0, 0, 0]]
>>> pp[0]
[[0, 0.5], [1, 0.125], [2, 0.125], [3, 0.0625], [4, 0.0625], [5, 0.0625], [6, 0.03125], [7, 0.03125], 0]
>>> p[0][0]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    p[0][0]
TypeError: 'float' object is not subscriptable
>>> pp[0]
[[0, 0.5], [1, 0.125], [2, 0.125], [3, 0.0625], [4, 0.0625], [5, 0.0625], [6, 0.03125], [7, 0.03125], 0]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 55, in <module>
    display()
NameError: name 'display' is not defined
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125
code word  ['1'] ['010'] ['110'] ['1000', '10'] ['0100'] ['1100'] ['00000'] ['10000']
code length  1 3 3 4 4 4 5 5
Efficiency  100
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   [28, 1.0]   

[1, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125]   [3, 0.25]   [25, 0.25, 0]   [0, 0.5, 1]   0   

[2, 0.125]   [2, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125, 0]   [3, 0.25, 1]   0   0   

[3, 0.0625]   [13, 0.0625]   [2, 0.125]   [1, 0.125, 0]   [9, 0.125, 1]   0   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.0625, 0]   [2, 0.125, 1]   0   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   0   

0   0   0   0   0   0   0   0   

code word  ['1'] ['010'] ['110'] ['1000', '10'] ['0100'] ['1100'] ['00000'] ['10000']
code length  1 3 3 4 4 4 5 5
Efficiency  100
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125
Traceback (most recent call last):
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 71, in <module>
    al=sum([round(float(pp[0][x][1]*cl[x]),1) for x in range(len(pp[0]))])
  File "C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py", line 71, in <listcomp>
    al=sum([round(float(pp[0][x][1]*cl[x]),1) for x in range(len(pp[0]))])
IndexError: list index out of range
>>> code
[['1'], ['010'], ['110'], ['0100'], ['1100'], ['00000'], ['10000']]
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   [28, 1.0]   

[1, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125]   [3, 0.25]   [25, 0.25, 0]   [0, 0.5, 1]   0   

[2, 0.125]   [2, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125, 0]   [3, 0.25, 1]   0   0   

[3, 0.0625]   [13, 0.0625]   [2, 0.125]   [1, 0.125, 0]   [9, 0.125, 1]   0   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.0625, 0]   [2, 0.125, 1]   0   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   0   

0   0   0   0   0   0   0   0   

code word  ['1'] ['010'] ['110'] 1000 ['0100'] ['1100'] ['00000'] ['10000']
code length  1 3 3 1 4 4 5 5
Efficiency  105
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 .03125 .03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   [28, 1.0]   

[1, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125]   [3, 0.25]   [25, 0.25, 0]   [0, 0.5, 1]   0   

[2, 0.125]   [2, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125, 0]   [3, 0.25, 1]   0   0   

[3, 0.0625]   [13, 0.0625]   [2, 0.125]   [1, 0.125, 0]   [9, 0.125, 1]   0   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.0625, 0]   [2, 0.125, 1]   0   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   0   

0   0   0   0   0   0   0   0   

code word  ['1'] ['010'] ['110'] ['1000'] ['0100'] ['1100'] ['00000'] ['10000']
code length  1 3 3 4 4 4 5 5
Efficiency  100
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.4 .2 .2 .1 .1


[0, 0.4]   [0, 0.4]   [3, 0.4]   [7, 0.6000000000000001, 0]   [10, 1.0]   

[1, 0.2]   [7, 0.2]   [0, 0.4, 0]   [3, 0.4, 1]   0   

[2, 0.2]   [1, 0.2, 0]   [7, 0.2, 1]   0   0   

[3, 0.1, 0]   [2, 0.2, 1]   0   0   0   

[4, 0.1, 1]   0   0   0   0   

0   0   0   0   0   

code word  ['00'] ['01'] ['11'] ['010'] ['110']
code length  2 2 2 3 3
Efficiency  96
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .2 .1 .1 .1


[0, 0.5]   [0, 0.5]   [0, 0.5]   [10, 0.5, 0]   [10, 1.0]   

[1, 0.2]   [7, 0.2]   [3, 0.30000000000000004, 0]   [0, 0.5, 1]   0   

[2, 0.1]   [1, 0.2, 0]   [7, 0.2, 1]   0   0   

[3, 0.1, 0]   [2, 0.1, 1]   0   0   0   

[4, 0.1, 1]   0   0   0   0   

0   0   0   0   0   

code word  ['1'] ['000'] ['100'] ['010'] ['110']
code length  1 3 3 3 3
Efficiency  98
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.3 .2 .2 .1 .1 .1


[0, 0.3]   [0, 0.3]   [5, 0.30000000000000004]   [10, 0.4]   [5, 0.6000000000000001, 0]   [15, 1.0]   

[1, 0.2]   [9, 0.2]   [0, 0.3]   [5, 0.30000000000000004, 0]   [10, 0.4, 1]   0   

[2, 0.2]   [1, 0.2]   [9, 0.2, 0]   [0, 0.3, 1]   0   0   

[3, 0.1]   [2, 0.2, 0]   [1, 0.2, 1]   0   0   0   

[4, 0.1, 0]   [3, 0.1, 1]   0   0   0   0   

[5, 0.1, 1]   0   0   0   0   0   

0   0   0   0   0   0   

code word  ['10'] ['11'] ['000'] ['100'] ['001'] ['101', '00', '0']
code length  2 2 3 3 3 3
Efficiency  97
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.3 .2 .2 .1 .1 .1


[0, 0.3]   [0, 0.3]   [5, 0.30000000000000004]   [10, 0.4]   [5, 0.6000000000000001, 0]   [15, 1.0]   

[1, 0.2]   [9, 0.2]   [0, 0.3]   [5, 0.30000000000000004, 0]   [10, 0.4, 1]   0   

[2, 0.2]   [1, 0.2]   [9, 0.2, 0]   [0, 0.3, 1]   0   0   

[3, 0.1]   [2, 0.2, 0]   [1, 0.2, 1]   0   0   0   

[4, 0.1, 0]   [3, 0.1, 1]   0   0   0   0   

[5, 0.1, 1]   0   0   0   0   0   

0   0   0   0   0   0   

code word  ['10'] ['11'] ['000'] ['100'] ['001'] ['101']
code length  2 2 3 3 3 3
Efficiency  97
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.3 .2 .2 .2 .1


[0, 0.3]   [7, 0.30000000000000004]   [3, 0.4]   [7, 0.6000000000000001, 0]   [10, 1.0]   

[1, 0.2]   [0, 0.3]   [7, 0.30000000000000004, 0]   [3, 0.4, 1]   0   

[2, 0.2]   [1, 0.2, 0]   [0, 0.3, 1]   0   0   

[3, 0.2, 0]   [2, 0.2, 1]   0   0   0   

[4, 0.1, 1]   0   0   0   0   

0   0   0   0   0   

code word  ['10'] ['01'] ['11'] ['000'] ['100']
code length  2 2 2 3 3
Efficiency  97
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.25 .25 .125 .125 .125 .125


[0, 0.25]   [9, 0.25]   [5, 0.25]   [1, 0.5]   [14, 0.5, 0]   [15, 1.0]   

[1, 0.25]   [0, 0.25]   [9, 0.25]   [5, 0.25, 0]   [1, 0.5, 1]   0   

[2, 0.125]   [1, 0.25]   [0, 0.25, 0]   [9, 0.25, 1]   0   0   

[3, 0.125]   [2, 0.125, 0]   [1, 0.25, 1]   0   0   0   

[4, 0.125, 0]   [3, 0.125, 1]   0   0   0   0   

[5, 0.125, 1]   0   0   0   0   0   

0   0   0   0   0   0   

code word  ['01'] ['11'] ['000'] ['100'] ['010'] ['110']
code length  2 2 3 3 3 3
Efficiency  96
>>> 
=============================== RESTART: C:/Users/ELCOT/AppData/Local/Programs/Python/Python38/subu.py ==============================
Enter the probabilities in spaces sepreated	.5 .125 .125 .0625 .0625 .0625 0.03125 0.03125


[0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [0, 0.5]   [28, 0.5, 0]   [28, 1.0]   

[1, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125]   [3, 0.25]   [25, 0.25, 0]   [0, 0.5, 1]   0   

[2, 0.125]   [2, 0.125]   [1, 0.125]   [9, 0.125]   [16, 0.125, 0]   [3, 0.25, 1]   0   0   

[3, 0.0625]   [13, 0.0625]   [2, 0.125]   [1, 0.125, 0]   [9, 0.125, 1]   0   0   0   

[4, 0.0625]   [3, 0.0625]   [13, 0.0625, 0]   [2, 0.125, 1]   0   0   0   0   

[5, 0.0625]   [4, 0.0625, 0]   [3, 0.0625, 1]   0   0   0   0   0   

[6, 0.03125, 0]   [5, 0.0625, 1]   0   0   0   0   0   0   

[7, 0.03125, 1]   0   0   0   0   0   0   0   

0   0   0   0   0   0   0   0   

code word  ['1'] ['010'] ['110'] ['1000'] ['0100'] ['1100'] ['00000'] ['10000']
code length  1 3 3 4 4 4 5 5
Efficiency  100
>>> 