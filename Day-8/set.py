Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
'''set
mutable
no dupl
unorde
dyna
homog'''
'set\nmutable\nno dupl\nunorde\ndyna\nhomog'
s = set()
s = {1,2,3,4,1,2,3,4,1,2}
s
{1, 2, 3, 4}
s.add(100)
s
{1, 2, 3, 100, 4}
s.add(0)
s
{0, 1, 2, 3, 100, 4}
s.add(1.2)
s
{0, 1, 2, 3, 100, 4, 1.2}
s.add('string')
s
{0, 1, 2, 3, 100, 4, 1.2, 'string'}
a.add([1,2])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.add([1,2])
NameError: name 'a' is not defined
s.add([1,2])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.add([1,2])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({1,2})
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.add({1,2})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add({1:1,2:2})
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.add({1:1,2:2})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
"1" in s
False
1 in s
True
'string' in s
True
for in range(s)
SyntaxError: invalid syntax
for i in range(s):
    print(i)

    
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    for i in range(s):
TypeError: 'set' object cannot be interpreted as an integer
s
{0, 1, 2, 3, 100, 4, 1.2, 'string'}
for i in s:
    print(i)

    
0
1
2
3
100
4
1.2
string
a.union(b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.union(b)
NameError: name 'a' is not defined
a = {1,2,3,4,7,9}
b = {1,2,3,6,8,10}
a
{1, 2, 3, 4, 7, 9}
b
{1, 2, 3, 6, 8, 10}
a.union(b)
{1, 2, 3, 4, 6, 7, 8, 9, 10}
a.intersection(b)
{1, 2, 3}
a.difference(b)
{9, 4, 7}
a.issubset(b)
False
a.isdisjoint(b)
False

a | b
{1, 2, 3, 4, 6, 7, 8, 9, 10}
a - b
{9, 4, 7}
a^b
{4, 6, 7, 8, 9, 10}
a+b
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a>{1}
True
a
{1, 2, 3, 4, 7, 9}
b
{1, 2, 3, 6, 8, 10}
a.add(100)
a
{1, 2, 3, 4, 100, 7, 9}
a.update({100,120,130})
a
{1, 2, 3, 4, 100, 130, 7, 9, 120}
a.remove(100)
a
{1, 2, 3, 4, 130, 7, 9, 120}
a.pop()
1
a.clear()
a
set()
a = {20,29,28,27,25}
a
{20, 25, 27, 28, 29}
b
{1, 2, 3, 6, 8, 10}
a.intersection
<built-in method intersection of set object at 0x00000241ACE9A340>
>>> a.intersection(b)
set()
>>> a.intersection_update(b)
>>> 100
100
>>> a
set()
>>> b
{1, 2, 3, 6, 8, 10}
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b.add(1000)
>>> b
{1, 2, 3, 6, 8, 1000, 10}
>>> a.add(109)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.add(109)
NameError: name 'a' is not defined
>>> len(b)
7
>>> max(b)
1000
>>> min(b)
1
>>> sum(b)
1030
>>> sorted(b)
[1, 2, 3, 6, 8, 10, 1000]
>>> frozen  = frozenset([1,2,3])
>>> frozen.add(10)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    frozen.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
