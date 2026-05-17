Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=5
b=9
print(a+b)
14
print(a-b)
-4
print(a*b)
45
print(a//b)
0
print(a/b)
0.5555555555555556
print(a%b)
5

#above are arithmetic operators

2.assignment operators
SyntaxError: invalid decimal literal
#assignment operators
a=6
b=4
print(a+=b)
SyntaxError: invalid syntax
b+=a
b
10
b-=3
b
7
b*=2
b
14
b//=7
b
2
b/=5
b
0.4
b**=6
b
0.0040960000000000015
b%=2
b
0.0040960000000000015

#comparision operators
a=8
b=4
a<b
False
a>b
True
a==b
False
a!=b
True
b<a
True
b<=a
True
b>=a
False
a>=b
True
a<=b
False

#logical operators
a=4
b=6
a<b and b>a
True
a<=b and b>=a
True
a!=b and b==a
False
a<b or b>a
True
a!=b or b==a
True
a<=b or b>=a
True
not True
False
not False
True

#identify operators
a=9
if type(a) is int:
    print("it's true")

...     
it's true
>>> if type(a) is not int:
...     print(true)
... 
...     
>>> 
>>> b="sai"
>>> if type(b) is not str:
...     print(true)
... 
...     
>>> if type(b) is str:
...     print("it's true")
... 
...     
it's true
>>> 
>>> #membership
>>> a=8,9,7,5,2,1,10
>>> if 9 in a:
...     print(8)
... 
...     
8
>>> if 20 in a:
...     print(20)
... 
...     
>>> if 10 in a:
...     print(10)
... 
...     
10
>>> 
>>> #ex in string
>>> a="java","python","c"
>>> if "c" in a:
...     print("true")
... 
...     
true
>>> if "c" not in a:
...     print("false")
... 
...     
