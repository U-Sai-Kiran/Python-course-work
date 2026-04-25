'''

password = input("Enter the password: ")
if len(password)>=8:
    status = set()
    for i in password:
        if i.isupper():
            status.add("u")
        elif i.islower():
            status.add('l')
        elif i.isdigit():
            status.add('d')
        else:
            status.add('s')
    if len(status) == 4:
        print("Strong password")
    else:
        print("Weak password")
else:
    print("weak password")

#While loop

i = 10
while i<50:
    print(i)
    i+=2

i = 1
while i<11:
    if i == 5:
        break
    print(i)
    i=i+1
else:
    print("1...10 numbers are printed")

list = [1,0,2,0,0,5,0,0,3]
while 0 in list:
    list.remove(0)
print(list)


assert print(b),'you forgot to define b'
'''
a = 10
assert a == 10,'a not defined'






