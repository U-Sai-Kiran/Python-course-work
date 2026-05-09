'''
res = []
for i in range(1,11):
    res.append(i)
print(res)

List Comprehension

res = [i for i in range(1,11)]
print(res)

res = [i*2 for i in range(1,11)]
print(res)

res = [i*3 for i in range(1,11)]
print(res)

res = [i+10 for i in range(1,11)]
print(res)

res = [i for i in range(1,11) if i%2==0]
print(res)

res = [i if i%2==0 else "0" for i in range(1,11)]
print(res)

s = "python programming language"
vol = "aeiouAEIOU"
res = ["*" if i in vol else i for i in s]

print(''.join(res))

s = {i for i in range(7,71,7)}
print(s)

s = {i:i*7 for i in range(1,11)}
print(s)
'''
