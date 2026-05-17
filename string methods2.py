Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #split()
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> b="i am in python class"
>>> b.split()
['i', 'am', 'in', 'python', 'class']
>>> #join
>>> a="vja","hyd",vzg"
SyntaxError: unterminated string literal (detected at line 1)
>>> a="vja","hyd","vzg"
>>> "".join(a)
'vjahydvzg'
>>> " ".join(a)
'vja hyd vzg'
>>> "\t".join(a)
'vja\thyd\tvzg'
>>> "\n".join(a)
'vja\nhyd\nvzg'
>>> #concatenation
>>> a="python"
>>> b="course"
>>> print(a+b)
pythoncourse
>>> print(a+" "+b)
python course
>>> 
>>> fname="sai"
>>> lname="anand"
>>> print(fname+lname)
saianand
>>> print(fname+" "+lname)
sai anand
>>> print(fname.title()+" "+lname.title())
Sai Anand
>>> print((fname+" "+lname).title())
Sai Anand
>>> print((fname+" "+lname).capitalize())
Sai anand
>>> 
>>> #formatting
>>> a=2
>>> b=7
>>> print(a+b)
9
print("the sum is",a+b)
the sum is 9
print("the sum is",a+b)#wrong
the sum is 9
print("the sum is ,a+b")#this one is wrong not above
the sum is ,a+b
#dot format
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {}\n{}".format(a,b))
hello motu
patlu
print("hello {}\n hello {}".format(a,b))
hello motu
 hello patlu
#fstring
 
a"chota"
SyntaxError: invalid syntax
a="chota"
b="bheem"
print("hello {a}{b}")
hello {a}{b}
print(f"hello {a}{b}")
hello chotabheem
print(f"hello {a} hello {b}")
hello chota hello bheem
