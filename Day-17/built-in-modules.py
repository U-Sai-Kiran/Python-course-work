'''
import sys

print(sys.argv)
print(sys.path)
print(sys.version)

print("start")
sys.exit()
print("end")

import platform

print(platform.system())
print(platform.release())
print(platform.processor())




import math

print(math.pi)
print(math.e)

print(math.sqrt(81))
print(math.pow(6,3))

print(round(27.2))
print(round(45.9))

print(math.ceil(19.67))
print(math.floor(67.9))

print(abs(-39))
print(math.fabs(-89))

print(math.factorial(5))

print(math.gcd(30,20))

print(math.log(2,2))

print(math.sin(30))
print(math.cos(45))
print(math.tan(60))

print(math.degrees(150))
print(math.radians(150))




import random

random.seed(2)

print(random.random())
print(random.randint(12345,543543))
print(random.uniform(1,6))

l = ['sai', 'kiran', 'charan', 'teja']

print(random.choice(l))
print(random.choices(l,k=2))

print("before:",l)
random.shuffle(l)
print("After:",l)



import collections

s='python programming'
l = [1,2,3,4,98,5,6,7,89,1,2,2,3,4,4,5,5,43,2,34,56,54,32,34,5,6]

text = " in the on the at the on off in there"

print(collections.Counter(text.split()))


print(collections.Counter(s))
print(collections.Counter(l))


s = 'python perpogramming'
d=collections.defaultdict(int)
for i in s:
    d[i] += int(1)

print(d)


d=collections.deque([])

d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(6)
d.popleft()
d.append(20)
d.append(30)
d.append(40)
d.append(50)
d.append(60)
d.popleft()
d.popleft()
d.append(23)
d.popleft()
d.popleft()

print(d)


d=collections.deque([])

d.appendleft(2)
d.appendleft(3)
d.appendleft(4)
d.appendleft(5)
d.appendleft(6)
d.pop()
d.appendleft(20)
d.appendleft(30)
d.appendleft(40)
d.appendleft(50)
d.appendleft(60)
d.pop()
d.pop()
d.appendleft(23)
d.pop()
d.pop()

print(d)


import itertools

print(list(itertools.combinations('ABC',2)))
print(list(itertools.permutations('ABC',2)))
'''
















