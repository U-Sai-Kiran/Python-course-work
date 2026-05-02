'''
Functions

1. Built-in functions
2. User defined function


User defined function
syntax

def function_name(args):
    #stmt
    return smthg

function_name(para)


def wish(name):
    print(f'good afternoon {name}!')
    print('welcome to the python class\n')

wish('sai')
wish('teja')
wish('charan')

even or odd

def is_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

num = int(input(enter the num: ")
print(is_even(num))

def avg(a,b,c):
    return a+b+c/3
a,b,c = map(int,input("enter the nums: ").split())
print(avg(a,b,c))

Prime number

def is_prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True
num = int(input("enter the num: "))
print("Prime num" if is_prime(num) else "not prime")

def display(name,email,password):
    print("name: ", name)
    print("email: ", email)
    print("password: ", password)

display("username","email@gmail.com","pass@123")
display("email@gmail.com","username","pass@123")
display("email@gmail.com","pass@123","username")

def display(name,email,password):
    print("name: ", name)
    print("email: ", email)
    print("password: ", password)

display(name="username",email="email@gmail.com",password="pass@123")
display(email="email@gmail.com",name="username",password="pass@123")
display(email="email@gmail.com",password="pass@123",name="username")


def display(name,email,password,phoneno=None):
    print("name: ", name)
    print("email: ", email)
    print("password: ", password)
    print("phone no: ", phoneno)

display("username","email@gmail.com","pass@123")
display("email@gmail.com","username","pass@123","+91 23456798765")


def display(*n):
    print(sum(n))
display(1,2,3,4,5,6)
display(9999,8765,345,433)
'''

def display(**n):
    print(n)
display(k1 = 'v1',k2 = 'v2')
display(k1 = 'v1')
display(k1 = 'v1',k2 = 'v2',k3 = 'v3')
















































