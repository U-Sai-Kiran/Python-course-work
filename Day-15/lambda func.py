'''
lambda Function

syntax - lamda arguments: expression

#Using Function

def equal(s1,s2):
    if s1==s2:
        return "Equal"
    else:
        return "Not Equal"
s1 = "python"
s2 = "lang"
print(equal(s1,s2))

#Using lambda function

res = lambda s1,s2: "Equal" if s1==s2 else "Not Equal"

s1 = "python"
s2 = "lang"
print(res(s1,s2))

#Checking char is alphabet

res = lambda ch: "Alp" if ch.isalpha() else "Not Alpha"
print(res('fgh'))

#square of a number

res = lambda num: num**2
print(res(13))

res = lambda name: f'Thankyou {name} for choosing python'
print(res('sai'))


l = [1,2,3,4,5]
for i in range(len(l)):
    l[i] **= 2
print(l)

res = list(map(lambda i:i**2,l))
print(res)

l = ['sai','kiran','ram']
res = list(map(lambda i:i.upper(),l))
print(res)

vol = 'aeiouAEIOU'

res = lambda s:'Start' if s[0] in vol else 'Not Start'
print(res('abhi'))

l = [1,2,3,4,5]
res = list(map(lambda i:i+10,l))
print(res)

l = [1,2,3,4,5]
res = list(map(lambda i:i[0]*i[1],enumerate(l)))
print(res)

res = lambda s: s.split("@")[-1]
print(res("sai@codegnan.com"))

l = [1,2,3,4,15,18,33,72]
res = list(filter(lambda i:i%3==0,l))
print(res)

l = ['sai','kiran','ram','brock','lesnar']
res = list(filter(lambda i:len(i)>3,l))
print(res)

l = [1,2,3,4,15,18,33,72]
res = list(filter(lambda i:i%2==0,l))
print(res)


from functools import reduce

l=[1,3,2,4,5,6]
res = reduce(lambda sum,i:sum+i,l)
print(res)


d = {'sai':35,'kiran':39,'john':99,'brock':49,'jeff':87,'cena':65}
res = dict(sorted(d.items()))
print(res)

d = {'sai':35,'kiran':39,'john':99,'brock':49,'jeff':87,'cena':65}
res = dict(sorted(d.items(),reverse=True))
print(res)

d = {'sai':35,'kiran':39,'john':99,'brock':49,'jeff':87,'cena':65}
res = dict(sorted(d.items(),key=lambda i:i[1]))
print(res)
'''

d = {'sai':35,'kiran':39,'john':99,'brock':49,'jeff':87,'cena':65}
res = dict(sorted(d.items(),key=lambda i:i[1],reverse=True))
print(res)

































