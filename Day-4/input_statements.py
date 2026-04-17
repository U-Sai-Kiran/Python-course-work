Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name = input()
sai
>>> name
'sai'
>>> type(name)
<class 'str'>
>>> age = int(input())
12
>>> age
12
>>> age = int(input("Enter age : "))
Enter age : 12
>>> price = float(input("enter the price: "))
enter the price: 1000.05
>>> price
1000.05
>>> age
12
>>> price
1000.05
>>> names = intput("enter the names: ").split()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    names = intput("enter the names: ").split()
NameError: name 'intput' is not defined. Did you mean: 'input'?
>>> names = input("enter the names: ").split()
enter the names: john brock seth shawn
>>> names
['john', 'brock', 'seth', 'shawn']
>>> Id = list(map(int,input("Enter the Id: ").split()))
Enter the Id: 1 2 3 4
>>> Id
[1, 2, 3, 4]
>>> jersey_price = list(map(float,input("enter the price: ").split()))
enter the price: 100.05 250.34 123.34 234.56
>>> jersey_price
[100.05, 250.34, 123.34, 234.56]
Id = tuple(map(int,input("Enter the Id: ").split()))
Enter the Id: 4 5 7 2
Id
(4, 5, 7, 2)
names = set(input("enter the names: ").split())
enter the names: sai teja sree jake
names
{'sree', 'sai', 'jake', 'teja'}
names = tuple(input("enter the names: ").split())
enter the names: sai teja sree jake
names
('sai', 'teja', 'sree', 'jake')
price = tuple(map(float,input("Enter the Id: ").split(",")))
Enter the Id: 23.4 56.6 45.6 23.6
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    price = tuple(map(float,input("Enter the Id: ").split(",")))
ValueError: could not convert string to float: '23.4 56.6 45.6 23.6'
price = tuple(map(float,input("Enter the price: ").split()))
Enter the price:  23.4 56.6 45.6 23.6
price
(23.4, 56.6, 45.6, 23.6)
id = set(map(int,input("enter the id: ").split(",")))
enter the id: 76 78 65 98
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    id = set(map(int,input("enter the id: ").split(",")))
ValueError: invalid literal for int() with base 10: '76 78 65 98'
id = set(map(int,input("enter the id: ").split(,)))
SyntaxError: invalid syntax
id = set(map(int,input("enter the id: ").split()))
enter the id: 76 78 65 98
id
{65, 98, 76, 78}
price = set(map(float,input("enter the price: ").split()))
enter the price: 90.0 20.8 67.9 12.3
price
{90.0, 67.9, 20.8, 12.3}
list = eval("enter the names: ")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list = eval("enter the names: ")
  File "<string>", line 1
    enter the names: 
          ^^^
SyntaxError: invalid syntax
list = eval(["sai teja sree jake"])
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    list = eval(["sai teja sree jake"])
TypeError: eval() arg 1 must be a string, bytes or code object
list = eval([sai,teja,sree,jake])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    list = eval([sai,teja,sree,jake])
NameError: name 'sai' is not defined
list = eval(["Enter the names: "])
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    list = eval(["Enter the names: "])
TypeError: eval() arg 1 must be a string, bytes or code object
list = eval(input(["Enter the names: "]))
['Enter the names: ']sai,teja,sree,jake
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list = eval(input(["Enter the names: "]))
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'sai' is not defined
list = eval(input("Enter the names: "))
Enter the names: "sai","teja","sree","jake"
list
('sai', 'teja', 'sree', 'jake')
('sai', 'teja', 'sree', 'jake')
('sai', 'teja', 'sree', 'jake')
names = list(eval(input("Enter the names: ")))
Enter the names: sai teja sree jake
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    names = list(eval(input("Enter the names: ")))
  File "<string>", line 1
    sai teja sree jake
        ^^^^
SyntaxError: invalid syntax
names = list(eval(input("Enter the names: ")))
Enter the names: ["sai","teja","sree","jake"]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    names = list(eval(input("Enter the names: ")))
TypeError: 'tuple' object is not callable
del list
names = list(eval(input("Enter the names: ")))
Enter the names: ["sai","teja","sree","jake"]
names
['sai', 'teja', 'sree', 'jake']
a,b,c = list(map(input().split()))
1,2,3
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a,b,c = list(map(input().split()))
TypeError: map() must have at least two arguments.
1 2 3
SyntaxError: invalid syntax
a,b,c = list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
email,password = ["@gmail.com", '@123"]
                  
SyntaxError: unterminated string literal (detected at line 1)
email,password = ["@gmail.com", "@123"]
                  
email,password =input().split()
                  
sai@gmail.com @1234
email
                  
'sai@gmail.com'
password
                  
'@1234'
a = eval(input())
                  
12
a
                  
12
type(a)
                  
<class 'int'>
b = eval(input())
                  
76543.2345
b
                  
76543.2345
c = eval(input())
                  
'zxijhv'
c
                  
'zxijhv'
d = eval(input("enter the list: "))
                  
enter the list: [1,4,5,6,3,1]
d
                  
[1, 4, 5, 6, 3, 1]
e = eval(input("enter the set: "))
                  
enter the set: (2,3,4,5,5)
e
                  
(2, 3, 4, 5, 5)
f = eval(input("enter the tuple: "))
                  
enter the tuple: (5,6,34,54,323,8765)
f
                  
(5, 6, 34, 54, 323, 8765)
g = eval(input("enter the dict: "))
                  
enter the dict: {1:1,2:3,4:2,6:7}
g
                  
{1: 1, 2: 3, 4: 2, 6: 7}
h = eval(input("enter the boolean: "))
                  
enter the boolean: True
h
                  
True
name = ["sai","teja","jay"]
                  
name[1]
                  
'teja'
name[:-1]
                  
['sai', 'teja']
name[1:]
                  
['teja', 'jay']
a,b,c=10,20.4,'python'
                  
a
                  
10
b
                  
20.4
c
                  
'python'
print("a=",a,"b=",b,"c=",c)
                  
a= 10 b= 20.4 c= python
print("a=",a,"b=",b,"c=",c,sep='\n')
                  
a=
10
b=
20.4
c=
python
print("a=",a\n,"b=",b\n,"c=",c\n)
                  
SyntaxError: unexpected character after line continuation character
print("a=",a,"b=",b,"c=",c,sep='\n')
                  
a=
10
b=
20.4
c=
python
print(f'a:{},b:{},c:{}'(a,b,c))
                  
SyntaxError: f-string: valid expression required before '}'
print(f'a:{},b:{},c:{}'.format(a,b,c))
                  
SyntaxError: f-string: valid expression required before '}'
print('a:{},b:{},c:{}'.format(a,b,c))
                  
a:10,b:20.4,c:python
print('a:{a},b:{b},c:{c}')
                  
a:{a},b:{b},c:{c}
print('a:{a},b:{b},c:{c}'.(a,b,c))
                  
SyntaxError: invalid syntax
print(f'a:{a},b:{b},c:{c}')
                  
a:10,b:20.4,c:python
print(f'a:{a},b:{b},c:{c}'.format(b,c,a))
                  
a:10,b:20.4,c:python
print(f'a:{},b:{},c:{}'.format(b,c,a))
                  
SyntaxError: f-string: valid expression required before '}'
print(f'a:{},b:{},c:{}'.(b,c,a))
                  
SyntaxError: f-string: valid expression required before '}'
print('a:{},b:{},c:{}'.format(b,c,a))
                  
a:20.4,b:python,c:10
print(f'a:{c},b:{a},c:{b}'.format(a,b,c))
                  
a:python,b:10,c:20.4
