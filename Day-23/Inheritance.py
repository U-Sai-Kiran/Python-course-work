#Single inheritance
class A:
    def printa(self):
        print("parent class - A")

class B(A):   #inheriting class A
    def printb(self):
        print("class - B")

b = B()  #object creation
b.printa()
b.printb()


#multi-level inheritance

class A:
    def printa(self):
        print("parent class - A")

class B(A):   #inheriting class A
    def printb(self):
        print("class - B")

class C(B):   #inheriting both A and B
    def printc(self):
        print("class - C")

c = C()  #object creation
c.printa()
c.printb()
c.printc()


#multiple inheritance

class A:
    def printa(self):
        print("parent class - A")

class B:   
    def printb(self):
        print("class - B")

class C:   
    def printc(self):
        print("class - C")

class D(A,B,C):     #inherits all the parent classes
    def printd(self):
        print("class -D") 

d = D()
d.printa()
d.printb()
d.printc()
d.printd()

        
#hierarchical inheritance

class A:
    def printa(self):
        print("parent class - A")

class B(A):     #inherits the parent classes
    def printb(self):
        print("class - B")

class C(A):     #inherits the parent classes
    def printc(self):
        print("class - C")

class D(A):     #inherits the parent classes
    def printd(self):
        print("class -D") 


b = B()
c = C()
d = D()
b.printa()
b.printb()
c.printa()
c.printc()
d.printa()
d.printd()



#multi-level hierarchical inheritance

class A:
    def printa(self):
        print("parent class - A")

class B(A):     #inherits the parent classes
    def printb(self):
        print("class - B")

class C(A):     #inherits the parent classes
    def printc(self):
        print("class - C")

class D(B,C):     #inherits the child classes
    def printd(self):
        print("class -D")

d = D()
d.printa()
d.printb()
d.printc()
d.printd()


#super() - it is used access parent class methods or constructor

class A:
    def display(self):
        print("class A")
        
class B(A):
    def display(self):
        super().display()
        print("class B")

b = B()
b.display()


#class method for one or more parent class

class A:
    def display(self):
        print("class A")

class C:
    def display(self):
        print("class C")
        
class B(A,C):
    def display(self):
        A.display(self)
        C.display(self)
        print("class B")

b = B()
b.display()














































