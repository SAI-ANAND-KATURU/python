Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="machine learning"
a[3:11]
'hine lea'
a[::3]
'mheeng'
a="python course"
a[9:4:3]#in positive striding big number to small number is not possible
''
a[-6:-4:-2]#in negative striding small number to big number is not possible
''
a[::1]
'python course'
a[::-1]#reverse a string
'esruoc nohtyp'
a[-6:-2]
'cour'
#string methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count():-no of repeated letters or numbers
#count is a built in method not built in function we cannot use it directly
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("k")
2
a.count("t")
5
a.count(' ')
3
a.count()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.count()
TypeError: count expected at least 1 argument, got 0
a.count(a)
1
b="star"
b.count(a)
0
#find a string we use "find()"
a="python"
s[2]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s[2]
NameError: name 's' is not defined
a[2]
't'
a.find[2]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.find[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.find(2)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.find(2)
TypeError: find() argument 1 must be str, not int
a.find("t")
2
#find():- it only find one value and doesnot find repeated characters in a string
a.find("o")
4
b="hello"
b.find("l")
2
#escape sequences
#\n->new line(backword slash)
#\t->tab space(4 to 8 spaces)
a="name\nmobileno\tmailid"
print(a)
name
mobileno	mailid
b="name:pooja\nmobileno:8908983\tmaidid"
print(b)
name:pooja
mobileno:8908983	maidid
a="city \tname\nmailid\\t"
print(a)
city 	name
mailid\t
#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
print(a)
wait until you succeed
>>> b="wait wait until you succeed"
>>> replace("wait,work")
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    replace("wait,work")
NameError: name 'replace' is not defined
>>> b.replace("wait","work",1)
'work wait until you succeed'
>>> b.replace(a)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    b.replace(a)
TypeError: replace() takes at least 2 positional arguments (1 given)
>>> b.replace("wait",a)
'wait until you succeed wait until you succeed until you succeed'
>>> b
'wait wait until you succeed'
>>> a
'wait until you succeed'
>>> #strip()
>>> #lstrip(),rstrip()
>>> a="     srikar      "
>>> a.lstrip()
'srikar      '
>>> a.rstrip()
'     srikar'
