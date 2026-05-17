Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
print(a)
10
#variables
d=50
print(d)
50
5=10
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a5=10
print(a5)
10
10a=90
SyntaxError: invalid decimal literal
#do not start with keyword such as
if=70
SyntaxError: invalid syntax
while=90
SyntaxError: invalid syntax
city="vja"
print(city)
vja
mobileno=9456789
print(mobileno)
9456789
#concatenation
fname="sai"
lname="anand"
print(fname+" "+lname)
sai anand
print(fname,lname)
sai anand
>>> #methods in one line
>>> a=10;b=20
>>> print(a+b)
30
>>> a=10
>>> b=20
>>> print(a+b)
30
>>> a,b=2,4
>>> print(a+b)
6
>>> a,b,c=50
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a,b,c=50
TypeError: cannot unpack non-iterable int object
>>> a=b=c=50
>>> print(a,b,c)
50 50 50
>>> a,b,c=4,5,6
>>> print(a,b,c)
4 5 6
>>> a=6,7,8,9
>>> print(a)
(6, 7, 8, 9)
>>> a b c =4 5 6
SyntaxError: invalid syntax
>>> a_b_c=4 5 6
SyntaxError: invalid syntax
>>> a,b,c=(6,7,8)
>>> print(a,b,c)
6 7 8
>>> z=10
>>> print(z)
10
>>> del(z)
>>> del(a)
>>> print(z)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
>>> #special char
>>> @=20
SyntaxError: invalid syntax
>>> $=9
SyntaxError: invalid syntax
#do not give space btw words
first name=sai
SyntaxError: invalid syntax
firstname="sai"
print(firstname)
sai
first_name="sai"
print(first_name)
sai
first@name="Sai"
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
mail="gh@gmail.com"
print(mail)
gh@gmail.com
