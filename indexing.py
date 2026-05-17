Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="Anand"
a[3]
'n'
a="i am in cls"
a[4]+a[5]+a[6]+a[7]
' in '
a="simple is better than complex"
a[23]+a[24]+a[25]+a[25]+a[26]+a[27]+a[28]
'ompplex'
>>> a[22]+a[23]+a[24]+a[25]+a[25]+a[26]+a[27]+a[28]
'compplex'
>>> a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
>>> a[10]+a[11]+a[12]
'bet'
>>> KeyboardInterrupt
>>> a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
>>> a[0]+a[1]
'si'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]
'simple '
>>> b="vijaywada is a royal city"
>>> b[22]+b[23]+b[24]+b[25]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    b[22]+b[23]+b[24]+b[25]
IndexError: string index out of range
>>> b="vijayawada is a royal city"
... b[22]+b[23]+b[24]+b[25]
... 
SyntaxError: multiple statements found while compiling a single statement
>>> b[22]+b[23]+b[24]+b[25]
... c="vijayawada is a royal city"
SyntaxError: multiple statements found while compiling a single statement
>>> #above positive indexing
>>> 
>>> a="codegnan it solutions"
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'solutions'
>>> a[-21]+a[-20]+a[-19]+a[-18]+a[-17]+a[-16]
'codegn'
>>> 
>>> =a[-21]+a[-20]+a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'codegnan'
>>> b="vizag is a city of destiny"
>>> b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'destiny'\
>>> 'destiny'\
... b[-15]+b[-14]+b[-13]+b[-12]
SyntaxError: invalid syntax
>>> b[-15]+b[-14]+b[-13]+b[-12]
'city'
>>> b[-26]+b[-25]+b[-24]+b[-23]+b[-22]
'vizag'
