#polymorphism

#method overriding
class Hotstar:
    def login(self):
        print("you can login")
    def search(self):
        print("you can search for movies")
    def otp(self):
        print("you can verify eith otp")
    def movies(self):
        print("limited movies are available")
    def users(self):
        print("limited users")
    def videocontrollers(self):
        print("ads will run and quality is low")

class premiumHotstar(Hotstar):
    def movies(self):
        print("unlimited movies are available")
    def users(self):
        print("unlimited users")
    def videocontrollers(self):
        print("ads won't run and quality is high")

sai = Hotstar()
print("sai - Hotstar")
sai.login()
sai.search()
sai.otp()
sai.movies()
sai.users()
sai.videocontrollers()

kiran = premiumHotstar()
print("kiran - Premium Hotstar")
kiran.login()
kiran.search()
kiran.otp()
kiran.movies()
kiran.users()
kiran.videocontrollers()


#operator overloading

class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return self.num + other.num
    def __sub__(self,other):
        return self.num - other.num
    def __mul__(self,other):
        return self.num * other.num
    def __gt__(self,other):
        return self.num > other.num
    def __lt__(self,other):
        return self.num < other.num
    def __eq__(self,other):
        return self.num == other.num
    def __str__(self):
        return f"{self.num}"

a = Number(90)
b = Number(20)

print(a+b)
print(a-b)
print(a*b)
print(a>b)
print(a<b)
print(a==b)
print(a,b)




































