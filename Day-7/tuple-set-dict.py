Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=()
t = tuple()
type(t)
<class 'tuple'>
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t = (1,2.3,'string',[1,2,3],{1,2,3},{1:1,2:2},False)
t
(1, 2.3, 'string', [1, 2, 3], {1, 2, 3}, {1: 1, 2: 2}, False)
t[2]
'string'
t(-3:)
SyntaxError: invalid syntax
t[-3:]
({1, 2, 3}, {1: 1, 2: 2}, False)
t[1:]
(2.3, 'string', [1, 2, 3], {1, 2, 3}, {1: 1, 2: 2}, False)
t[1:-2]
(2.3, 'string', [1, 2, 3], {1, 2, 3})
t[-2:1]
()
t[1:1:-1]
()
t[1:1:6]
()
t[1:2:]
(2.3,)
'string' in t
True
'32' in t
False
'2.3' in t
False
2.3 in t
True
32 not in t
True
len(t)
7
min(t)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    min(t)
TypeError: '<' not supported between instances of 'str' and 'int'
max(t)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'str' and 'float'
l = (1,2,3,4,4,5,5,6,7,8)
len(t)
7
min(l)
1
max(l)
8
l.count(4)
2
l.index(3)
2
t= (1,2,3,[4,6])
t
(1, 2, 3, [4, 6])
t.index([4,5])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    t.index([4,5])
ValueError: tuple.index(x): x not in tuple
t(3)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    t(3)
TypeError: 'tuple' object is not callable
t[3]
[4, 6]
t.append[10]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    t.append[10]
AttributeError: 'tuple' object has no attribute 'append'
t[3].append(10)
t
(1, 2, 3, [4, 6, 10])
t.append(10)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    t.append(10)
AttributeError: 'tuple' object has no attribute 'append'
t[3].append(10)
t
(1, 2, 3, [4, 6, 10, 10])
t[3].pop()
10
''' dict
key:value
mutable
dyn:
ordered
val: dupl
key: unique'''
' dict\nkey:value\nmutable\ndyn:\nordered\nval: dupl\nkey: unique'
d={}
d = dict()
type(d)
<class 'dict'>
d = {'name':'sai', 'batch': 52, 'skills': ['python','css','html']}
d
{'name': 'sai', 'batch': 52, 'skills': ['python', 'css', 'html']}
d['name']='kiran'
d
{'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html']}
d['course']='kiran'
d
{'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'kiran'}
s={]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
s={}
s[1]={'int'}
s
{1: {'int'}}
s[1.2]={'float'}
s
{1: {'int'}, 1.2: {'float'}}
s['demo']={'string'}
s
{1: {'int'}, 1.2: {'float'}, 'demo': {'string'}}
s[1,2,3]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s[1,2,3]
KeyError: (1, 2, 3)
s[1,2,3]='value'
s
{1: {'int'}, 1.2: {'float'}, 'demo': {'string'}, (1, 2, 3): 'value'}
s[[4,5,6]]='value'
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s[[4,5,6]]='value'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
s[True] = 'yes'
s
{1: 'yes', 1.2: {'float'}, 'demo': {'string'}, (1, 2, 3): 'value'}
s[{1:1,2:2}]='dict'
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s[{1:1,2:2}]='dict'
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
s[False] = 1
s
{1: 'yes', 1.2: {'float'}, 'demo': {'string'}, (1, 2, 3): 'value', False: 1}
'name' in s
False
d
{'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'kiran'}
'name' in d
True
'kiran' in d
False
d['name']
'kiran'
d['skills']
['python', 'css', 'html']
d['course']
'kiran'
d.get('age')
d.get('batch')
52
d.get('age','age is not present')
'age is not present'
d.get('course', 'course is not present')
'kiran'
d['course']= 'PFS'
d
{'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS'}
d['age']=22
d
{'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 22}
d.update[{'k1':'v1','k2':'v2','k3':'v3'}]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    d.update[{'k1':'v1','k2':'v2','k3':'v3'}]
TypeError: 'builtin_function_or_method' object is not subscriptable
d.update({'k1':'v1','k2':'v2','k3':'v3'})
d
{'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 22, 'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
d.pop()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
d.popitem()
('k3', 'v3')
d.pop('k1'0
      
SyntaxError: '(' was never closed
d.pop('k1')
      
'v1'
d
      
{'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 22, 'k2': 'v2'}
del d['k2']
      
d
      
{'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 22}
d.clear()
      
d
      
{}
d.keys()
      
dict_keys([])
d = {'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 22}
      
d
      
{'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 22}
d.keys()
      
dict_keys(['name', 'batch', 'skills', 'course', 'age'])
>>> d.values()
...       
dict_values(['kiran', 52, ['python', 'css', 'html'], 'PFS', 22])
>>> d.items()
...       
dict_items([('name', 'kiran'), ('batch', 52), ('skills', ['python', 'css', 'html']), ('course', 'PFS'), ('age', 22)])
>>> len(d)
...       
5
>>> sorted(d)
...       
['age', 'batch', 'course', 'name', 'skills']
>>> min(d)
...       
'age'
>>> max(d)
...       
'skills'
>>> d
...       
{'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 22}
>>> d.get('year')
...       
>>> d.setdefault('year',2025)
...       
2025
>>> d
...       
{'name': 'kiran', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 22, 'year': 2025}
>>> d.get('age'0
...       
SyntaxError: '(' was never closed
>>> d.get('age')
...       
22
