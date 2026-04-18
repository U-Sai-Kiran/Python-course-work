Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name="gkafwcljsk"
name
'gkafwcljsk'
name*2
'gkafwcljskgkafwcljsk'
name*20
'gkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljskgkafwcljsk'
a = "ds"
b = "wd"
a+b
'dswd'
a*3 b*4
SyntaxError: invalid syntax
a*3
'dsdsds'
b*4
'wdwdwdwd'
name = "brock lesnar"
name[2]
'o'
name[8]
's'
name[-3]
'n'
name[:-3]
'brock les'
name[::-1]
'ransel kcorb'
name = "sai teja sree john"
name[2:9:1]
'i teja '
name[12:18:3]
'eo'
name[12:18:1]
'e john'
name[1:18:1]
'ai teja sree john'
name[-2:-5:-2]
'hj'
'sai' in names
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    'sai' in names
NameError: name 'names' is not defined. Did you mean: 'name'?
'sai' in name
True
'charan' in name
False
len(name)
18
sorted(name)
[' ', ' ', ' ', 'a', 'a', 'e', 'e', 'e', 'h', 'i', 'j', 'j', 'n', 'o', 'r', 's', 's', 't']
max(name)
't'
min(name)
' '
ord('a')
97
ord('')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
ord(' ')
32
ord('a')
97
chr(97)
'a'
chr(38)
'&'
chr(12)
'\x0c'
ord('b')
98
sum(int(name))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    sum(int(name))
ValueError: invalid literal for int() with base 10: 'sai teja sree john'
sum(map(int,input(name)))
sai teja sree john
0
sum(map(int,input(name).split()))
sai teja sree john
0
name = "sai teja sree john"
count(map(int,input(name).split()))
SyntaxError: multiple statements found while compiling a single statement
name = "sai teja sree john"
count(input(name).split())
SyntaxError: multiple statements found while compiling a single statement
name = "sai teja sree john"
len(input(name).split())
SyntaxError: multiple statements found while compiling a single statement
name = "sai teja sree john"
len(name).split()
SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt
len(name)
18
len(name.split())
4
sum(len(name))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    sum(len(name))
TypeError: 'int' object is not iterable
sum(int(name.split()))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    sum(int(name.split()))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
sum(map(int,input(name.split())))
['sai', 'teja', 'sree', 'john']
0
name
'sai teja sree john'
name.upper()
'SAI TEJA SREE JOHN'
name.lower()
'sai teja sree john'
name.title()
'Sai Teja Sree John'
name.capitalize()
'Sai teja sree john'
name.casefold()
'sai teja sree john'
name.swapcase()
'SAI TEJA SREE JOHN'
name.capitalized()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    name.capitalized()
AttributeError: 'str' object has no attribute 'capitalized'. Did you mean: 'capitalize'?
name.lower()
'sai teja sree john'
name.capitalize()
'Sai teja sree john'
name.title()
'Sai Teja Sree John'
name.swapcase()
'SAI TEJA SREE JOHN'
"ssdfgrdcvbgfd".casefold()
'ssdfgrdcvbgfd'
name
'sai teja sree john'
name.center(50,'*')
'****************sai teja sree john****************'
name.center(50,' ')
'                sai teja sree john                '
name.ljust(50,'-')
'sai teja sree john--------------------------------'
name.rjust(50,'-')
'--------------------------------sai teja sree john'
num = 09876
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
num = 56789
num.zfill(10)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    num.zfill(10)
AttributeError: 'int' object has no attribute 'zfill'
num
56789
del.num
SyntaxError: invalid syntax
del(num)
num
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    num
NameError: name 'num' is not defined. Did you mean: 'sum'?
num = '4567'
num.zfill(10)
'0000004567'
num.zfill(2)
'4567'
num.zfill(1)
'4567'
num.zfill(6)
'004567'
num.zfill(50)
'00000000000000000000000000000000000000000000004567'
name
'sai teja sree john'
name.find('sai')
0
name.find('teja')
4
name.rfind('j')
14
name.lfind('t')
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    name.lfind('t')
AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
name.find('e')
5
name.index('s')
0
name.index('t')
4
name.index('sree')
9
name.count('a')
2
name.count('e')
3
name.replace('a','*')
's*i tej* sree john'
name.replace('a','0')
's0i tej0 sree john'
name.replace('teja','charan')
'sai charan sree john'
name.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
name.translate(name.maketrans('aeiou','12345'))
's13 t2j1 sr22 j4hn'
name
'sai teja sree john'
name.split()
['sai', 'teja', 'sree', 'john']
name.split(',')
['sai teja sree john']
name.split()
['sai', 'teja', 'sree', 'john']
name.split(' ',3)
['sai', 'teja', 'sree', 'john']
name.split(' ',2)
['sai', 'teja', 'sree john']
name.rsplit(' ',2)
['sai teja', 'sree', 'john']
s = 'python\nprogramming\nlang\n'
s
'python\nprogramming\nlang\n'
s.splitlines()
['python', 'programming', 'lang']
','.join(s)
'p,y,t,h,o,n,\n,p,r,o,g,r,a,m,m,i,n,g,\n,l,a,n,g,\n'
' '.join(s)
'p y t h o n \n p r o g r a m m i n g \n l a n g \n'
s.splitlines()
['python', 'programming', 'lang']
l = ['python', 'programming', 'lang']
','.join(l)
'python,programming,lang'
'@'.join(l)
'python@programming@lang'
name
'sai teja sree john'
name.partition('t')
('sai ', 't', 'eja sree john')
name.rpartition('e')
('sai teja sre', 'e', ' john')
name.rpartition('a')
('sai tej', 'a', ' sree john')
a = '        rain           fall          '
a
'        rain           fall          '
a.strip()
'rain           fall'
a.lstrip()
'rain           fall          '
>>> a.rstrip()
'        rain           fall'
>>> a.strip()
'rain           fall'
>>> a.replace(' ','')
'rainfall'
>>> text = 'i want to be successfull'
>>> text.encode()
b'i want to be successfull'
>>> b'i want to be successfull'.decode()
'i want to be successfull'
>>> type(text.encode())
<class 'bytes'>
>>> type(text.decode())
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    type(text.decode())
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> type(b'i want to be successfull'.decode())
<class 'str'>
>>> d = "hello Iam @&"
>>> d.encode()
b'hello Iam @&'
>>> b'hello Iam @&'.decode()
'hello Iam @&'
>>> text = "₹"
... text.encode()
SyntaxError: multiple statements found while compiling a single statement
>>> r = "$"
>>> r.encode()
b'$'
>>> t = "₹"
>>> t.encode()
b'\xe2\x82\xb9'
>>> d.encode()
b'hello Iam @&'
>>> f = 'hello 👉 வணக்கம்'
>>> f.encode()
b'hello \xf0\x9f\x91\x89 \xe0\xae\xb5\xe0\xae\xa3\xe0\xae\x95\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xae\xe0\xaf\x8d'
>>> b'hello \xf0\x9f\x91\x89 \xe0\xae\xb5\xe0\xae\xa3\xe0\xae\x95\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xae\xe0\xaf\x8d'.decode()
'hello 👉 வணக்கம்'
