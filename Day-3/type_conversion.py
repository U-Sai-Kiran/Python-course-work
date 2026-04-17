Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
bool(0)
False
b=10.3
int(b)
10
complex(b)
(10.3+0j)
list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
l=10+0j
int(l)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(l)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'complex'
list(l)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list(l)
TypeError: 'complex' object is not iterable
tuple(l)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(l)
TypeError: 'complex' object is not iterable
set(l)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    set(l)
TypeError: 'complex' object is not iterable
dict(l)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(l)
TypeError: 'complex' object is not iterable
bool(l)
True
c = [1,2,3,4,5]
int(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'list'
complex(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex(c)
TypeError: complex() argument must be a string or a number, not list
tuple(c)
(1, 2, 3, 4, 5)
set(c)
{1, 2, 3, 4, 5}
dict(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dict(c)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(c)
True
t = [1,2,3,4,4,5]
int(t)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(t)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'list'
complex(t)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not list
list(t)
[1, 2, 3, 4, 4, 5]
set(t)
{1, 2, 3, 4, 5}
dict(t)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s = (2,5,7,9)
int(s)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(s)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(s)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    complex(s)
TypeError: complex() argument must be a string or a number, not tuple
str(s)
'(2, 5, 7, 9)'
list(s)
[2, 5, 7, 9]
tuple(s)
(2, 5, 7, 9)
dict(s)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
dict = {"name" : "abc", "age" : "23", "course" : "pfs"}
int(dict)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    int(dict)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(dict)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    float(dict)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(dict)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    complex(dict)
TypeError: complex() argument must be a string or a number, not dict
str(dict)
"{'name': 'abc', 'age': '23', 'course': 'pfs'}"
list(dict)
['name', 'age', 'course']
tuple(dict)
('name', 'age', 'course')
set(dict)
{'course', 'age', 'name'}
bool(dict)
True
string = ('p','y','t','h','o','n')
int(string)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    int(string)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(string)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    float(string)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(string)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    complex(string)
TypeError: complex() argument must be a string or a number, not tuple
list(string)
['p', 'y', 't', 'h', 'o', 'n']
tuple(string)
('p', 'y', 't', 'h', 'o', 'n')
set(string)
{'t', 'y', 'n', 'o', 'h', 'p'}
dict(string)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    dict(string)
TypeError: 'dict' object is not callable
bool(string)
True
''' int -> float, complex, str, bool '''
' int -> float, complex, str, bool '
#int -> float, complex, str, bool
''' int -> float, complex, str, bool '''
' int -> float, complex, str, bool '

===== RESTART: C:/Users/usiri/Desktop/Python-course-work/Day-3/type_conv.py ====
a=20
b=10
a+b
10
a-b
10
a*b
200
a/b
2.0
a//b
2
a%b
0
a**b
10240000000000
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
a+=b
a
30
a-=b
a
20
a*=b
a
200
a/=b
a
20.0
a//=b
a
2.0
a%=b
a
2.0
a and b
10
a**=b
>>> a
1024.0
>>> a+=10
>>> a
1034.0
>>> a-=10
>>> a
1024.0
>>> a*=10
>>> a
10240.0
>>> a/=10
>>> a
1024.0
>>> a//=10
>>> a
102.0
>>> a%=10
>>> a
2.0
>>> a**=10
>>> a
1024.0
>>> c = 10
>>> d = 20
>>> c
10
>>> d
20
>>> a%3==0 and b%3==0
False
>>> a%5==0 and b%5==0
False
>>> a%3==0 or b%3==0
False
>>> a%5==0 or b%5==0
True
>>> not a%3==0
True
