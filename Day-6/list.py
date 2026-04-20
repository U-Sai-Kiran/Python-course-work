Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = "python programing lang"
s.startswith("p")
True
s.startswith("P")
False
s.startswith("ing.")
False
s.startswith("lang")
False
s.endswith("lang")
True
s.isaplha()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
s.isalpha()
False
'fdsa'.isalpha()
True
' '.isalpha()
False
'python'.isalpha()
True
'python3.14'.isalnum()
False
'python314'.isalnum()
True
'python 314'.isalnum()
False
'python'.islower()
True
'Python'.islower()
False
'PYTHON'.isupper()
True
'python 123'.islower()
True
'  '.isspace()
True
'python 123'.isspace()
False
s
'python programing lang'
s.istitle()
False
'12.9'.isdeciaml()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    '12.9'.isdeciaml()
AttributeError: 'str' object has no attribute 'isdeciaml'. Did you mean: 'isdecimal'?
'12.0'.isdecimal()
False
'321'.isdecimal()
True
'9876543'.isdigit()
True
'12.64'.isdigit()
False
'$'.isnumeric()
False
'9'.isnumeric()
True
l = [1,2,3,4,5]
l
[1, 2, 3, 4, 5]
l = list()
l
[]
type(l)
<class 'list'>
l = [6,9.0,'python',[],{},{1:1},True]
l
[6, 9.0, 'python', [], {}, {1: 1}, True]
a = [5,6,7,8]
b = [4,3,2,1]
a+b
[5, 6, 7, 8, 4, 3, 2, 1]
names = ['sai', 'teja', 'john', 'cena']
names
['sai', 'teja', 'john', 'cena']
names[0]
'sai'
names[1:3]
['teja', 'john']
names[:-4]
[]
names[-1]
'cena'
names[:-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
names[:-1]
['sai', 'teja', 'john']
names[:4:-1]
[]
names[:1:4]
['sai']
len(names)
4
sorted(names)
['cena', 'john', 'sai', 'teja']
min(names)
'cena'
max(names)
'teja'
a = {}
type(a)
<class 'dict'>
a.type()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.type()
AttributeError: 'dict' object has no attribute 'type'
a = set()
a
set()
names
['sai', 'teja', 'john', 'cena']
id(names)
2277649853248
names[3] = 'brock'
names
['sai', 'teja', 'john', 'brock']
id(names)
2277649853248
names
['sai', 'teja', 'john', 'brock']
names.append('randy')
names
['sai', 'teja', 'john', 'brock', 'randy']
names.insert(1,'randy')
names
['sai', 'randy', 'teja', 'john', 'brock', 'randy']
names.remove(5,'randy')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    names.remove(5,'randy')
TypeError: list.remove() takes exactly one argument (2 given)
names
['sai', 'randy', 'teja', 'john', 'brock', 'randy']
names.extend(['charan', 'nithin', 'punk'])
names
['sai', 'randy', 'teja', 'john', 'brock', 'randy', 'charan', 'nithin', 'punk']
names.pop(5)
'randy'
names
['sai', 'randy', 'teja', 'john', 'brock', 'charan', 'nithin', 'punk']
names.pop()
'punk'
names
['sai', 'randy', 'teja', 'john', 'brock', 'charan', 'nithin']
names.remove('john')
names
['sai', 'randy', 'teja', 'brock', 'charan', 'nithin']
del names[0]
names
['randy', 'teja', 'brock', 'charan', 'nithin']
names.clear()
names
[]
names = ['sai', 'randy', 'teja', 'john', 'brock', 'charan', 'nithin', 'punk']
names
['sai', 'randy', 'teja', 'john', 'brock', 'charan', 'nithin', 'punk']
names.index('randy')
1
names.index('punk')
7
names.sorted()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    names.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
names.sort()
names
['brock', 'charan', 'john', 'nithin', 'punk', 'randy', 'sai', 'teja']
names.sort(reverse=True)
names
['teja', 'sai', 'randy', 'punk', 'nithin', 'john', 'charan', 'brock']
>>> a = [1,2,3,4,5]
>>> b = a
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]
>>> b.append(10)
>>> b
[1, 2, 3, 4, 5, 10]
>>> a
[1, 2, 3, 4, 5, 10]
>>> c=a.copy()
>>> c
[1, 2, 3, 4, 5, 10]
>>> c.append(12)
>>> c
[1, 2, 3, 4, 5, 10, 12]
>>> a
[1, 2, 3, 4, 5, 10]
>>> b
[1, 2, 3, 4, 5, 10]
>>> sum(b)
25
>>> len(c)
7
>>> #[0,0.0,' ',[],set(),(),False]
>>> #[1,1.2,-1,'shy',True]
>>> any([0,0.0,' ',[],set(),(),False])
True
>>> any([0,1.0,' ',[],set(),(),False])
True
>>> any([0,0.0,'',[],set(),(),False])
False
>>> any([0,1.0,' ',[],set(),(),False])
True
>>> all([1,1.2,-1,'shy',True])
True
>>> all([1,1.2,0,'shy',True])
False
