Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #escape sequences
>>> 
>>> #\n->new line
>>> #\t->tab space
>>> a="name\nmobileno\tmailid
SyntaxError: unterminated string literal (detected at line 1)
>>> a="name\nmobileno\tmailid"
>>> print(a)
name
mobileno	mailid
>>> print("name:sai\nmobile no:34567890\tmailid:sai@gmail.com")
name:sai
mobile no:34567890	mailid:sai@gmail.com
>>> 
>>> #replace
>>> a="wait until you succeed"
>>> a.replace("wait","work")
'work until you succeed'
>>> b=" wait wait until you succeed"
>>> b.replace("wait","work")
' work work until you succeed'
>>> b.replace("wait","work",1)
' work wait until you succeed'
>>> 
>>> #strip
>>> #lstrip.rstrip
>>> a="             sai        "
>>> a.strip()
'sai'
>>> a.lstrip()
'sai        '
>>> a.rstrip()
'             sai'
