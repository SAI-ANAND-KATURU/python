Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #upper()
>>> a="codegnan"
>>> a.upper()
'CODEGNAN'
>>> b="HELLO"
>>> b.lower()
'hello'
>>> 
>>> a="python course"
>>> #capitalize
>>> a.capitalize()
'Python course'
>>> #title
>>> a.title()
'Python Course'
>>> b="i am in class"
>>> b.upper()
'I AM IN CLASS'
>>> b.capitalize()
'I am in class'
>>> b.title()
'I Am In Class'
>>> a="code"
>>> a.isupper()
False
>>> a.islower()
True
>>> a.isalpha()
True
>>> b="code gnan"
>>> b.isalpha()
False
>>> c="codegnan"
>>> c.isalpha()
True
>>> c="123456"
>>> c.isdigit()
True
>>> a="sai123"
>>> a.isalnum()
True
>>> a="Sai@123"
>>> a.isalnum()
False
