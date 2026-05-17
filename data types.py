Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=5
>>> type(a)
<class 'int'>
>>> b=7.8
>>> type(b)
<class 'float'>
>>> c="sai"
>>> type(c)
<class 'str'>
>>> d=True
>>> type(d)
<class 'bool'>
>>> e=False
>>> type(e)
<class 'bool'>
>>> z=9j
>>> type(z)
<class 'complex'>
>>> z=9+9j
>>> type(z)
<class 'complex'>
>>> z=i+9
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    z=i+9
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> #these above examples defines the datatype of variable
>>> 
>>> #datatype conversions
>>> #int
>>> int(8)
8
>>> int("sai")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int("sai")
ValueError: invalid literal for int() with base 10: 'sai'
>>> int(9+7j)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(9+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
#float
float(3)
3.0
float(2.5)
2.5
float("Anand")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    float("Anand")
ValueError: could not convert string to float: 'Anand'
float(8+9j)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    float(8+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#str
str(1)
'1'
str("nov")
'nov'
str(True)
'True'
str(False)
'False'
str(7j)
'7j'
str(7.9)
'7.9'
#complex
complex(6)
(6+0j)
complex(4.5)
(4.5+0j)
complex("Te")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    complex("Te")
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
#bool
bool(9)
True
bool(9.8)
True
bool("true)
     
SyntaxError: unterminated string literal (detected at line 1)
bool("True")
     
True
bool("false")
     
True
bool("TEl")
     
True
bool(8j)
     
True
