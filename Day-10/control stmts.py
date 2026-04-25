Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = 'string'
for i in s:
    print(i)

    
s
t
r
i
n
g
l = [1,2,3,4]
for i in l:
    print(i)

    
1
2
3
4
t = (1,2,3,4)
for i in t:
    print(i)

    
1
2
3
4
se = {1,2,3,4,5}
for i in se;
SyntaxError: invalid syntax
se = {1,2,3,4,5}
for i in se:
    
SyntaxError: multiple statements found while compiling a single statement
del se
se
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    se
NameError: name 'se' is not defined. Did you mean: 's'?
se = {1,2,3,4}
for i in se:
    print(i)

    
1
2
3
4
d = {1:1,2:2,3:3,4:4}
for i in d:
    print(i,d[i])

    
1 1
2 2
3 3
4 4
for i in range(0,10,2):
    print(i)

    
0
2
4
6
8
for i in range(0,11):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
for i in range(10,0)
SyntaxError: expected ':'
for i in range(10,0):
    print(i)

    
for i in range(10,0,-1):
    print(i)

    
10
9
8
7
6
5
4
3
2
1
for i in range(10,70):
    print(i)

    
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
for i in range(12,120,12):
    print(i)

    
12
24
36
48
60
72
84
96
108
for i in range(190,18,-19):
    print(i)

    
190
171
152
133
114
95
76
57
38
19
for i in enumerate(s):
    print(i)

    
(0, 's')
(1, 't')
(2, 'r')
(3, 'i')
(4, 'n')
(5, 'g')
for i in range(len(s)):
    print(i,s[i])

    
0 s
1 t
2 r
3 i
4 n
5 g
names = ['hbk','john','brock','cena']
for i in enumerate(names):
    print(i[0],i[1])

    
0 hbk
1 john
2 brock
3 cena
for i in range(len(names)):
    print(i,names[i])

    
0 hbk
1 john
2 brock
3 cena
f = {1,2,3,4}
for i in enumerate(f):
    print(i[0],i[1],d[i[1])
          
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
for i in enumerate(f):
    print(i[0],i[1],d[i[1]])

          
0 1 1
1 2 2
2 3 3
3 4 4
d = {1:1,2:2,3:3}
          
for i in enumerate(d):
          print(i[0],i[1],d[i[1]])

          
0 1 1
1 2 2
2 3 3
f
          
{1, 2, 3, 4}
for i in enumerate(f):
          print(i[0],i[1])

          
0 1
1 2
2 3
3 4
for i in range(10):
          pass

          
for i in range(10):
          if i == 7:
          break
        
SyntaxError: expected an indented block after 'if' statement on line 2
for i in range(10):
    if i == 7:
        break
    print(i)

    
0
1
2
3
4
5
6
for i in range(10):
    if i == 4:
        continue
    print(i)

    
0
1
2
3
5
6
7
8
9
>>> 
>>> 
>>> 
>>> #for with else
>>> products = ['sugar', 'bread', 'milk', 'salt']
>>> a = 'sugar'
>>> for i in products:
...     if a == i:
...         print(i)
...     break
... else:
...     print("Not Found")
... 
...     
sugar
>>> pin = 12345
>>> 
>>> for i in range(5):
...     epin = int(input("enter the pin: "))
...     if pin == epin:
...         print("Login Successfull")
...         break
...     else:
...         print("Incorrect pin")
... else:
...     print("Try after 30 seconds")
... 
...     
enter the pin: 12345
Login Successfull
