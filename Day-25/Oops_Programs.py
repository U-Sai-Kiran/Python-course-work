'''
from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,phoneno):
        self.name = name
        self.phoneno = phoneno

    @abstractmethod
    def displayinfo(self):
        pass

class Teacher(Person):
    def __init__(self,name,phoneno,subject,salary):
        super().__init__(name,phoneno)
        self.subject = subject
        self.salary = salary

    def displayinfo(self):
        print("-----Teacher Information------")
        print(f"name: {self.name}")
        print(f"phoneno: {self.phoneno}")
        print(f"subject: {self.subject}")
        print(f"salary: {self.salary}")
        
              

class Student(Person):
    def __init__(self,name,phoneno,course,grade):
        super().__init__(name,phoneno)
        self.course = course
        self.grade = grade

    @staticmethod
    def check(g):
        if g == 'A':
            return "A Grade - Good, Keep it up"
        elif g == 'B':
            return "B Grade - Needs Improvement"
        elif g == 'C':
            return "C Grade - Not bad, Work hard"
        elif g == 'D':
            return "D Grade - Bad performance"
        elif g == 'F':
            return "Fail"

    def displayinfo(self):
        print("-----student Information------")
        print(f"name: {self.name}")
        print(f"phoneno: {self.phoneno}")
        print(f"course: {self.course}")
        print(f"grades: {self.check(self.grade)}")


sai = Student("sai", "9876543210", "pfs", "A")
sai.displayinfo()

print()

kiran = Teacher("kiran", "8765432190", "python", 987654)
kiran.displayinfo()
'''


'''
library management system
classes - person,student,librarian,book,library
Att - name,phone,course,borrowed_book,employee_id,section
methods - display_info(),borrow_book(),return_book(),display_info(),add_book(),
remove_book(),check_availability(),,issue_book(),search_book(),display_info()
'''

from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,phoneno):
        self.name = name
        self.phoneno = phoneno
        self.__fine = 0

    def set_fine(self,amount):
        self.__fine = amount

    def get_fine(self):
        return self.__fine

    @staticmethod
    def validate_ISBN(ISBN):
        return len(ISBN) == 10
    

    @abstractmethod
    def display_info(self):
        pass

class Student(Person):
    def __init__(self,name,phoneno,course,borrowed_book):
        super().__init__(name,phoneno)
        self.course = course
        self.borrowed_book = borrowed_book


    def display_info(self):
        print("----------student information-----------")
        print(f"name: {self.name}")
        print(f"phoneno: {self.phoneno}")
        print(f"course: {self.course}")
        print(f"borrowed_book: {self.borrowed_book}")
        
class Librarian(Person):
    def __init__(self,name,phoneno,employee_id,section):
        super().__init__(name,phoneno)
        self.employee_id = employee_id
        self.section = section

    def display_info(self):
        print("----------Librarian information-----------")
        print(f"name: {self.name}")
        print(f"phoneno: {self.phoneno}")
        print(f"employee_id: {self.employee_id}")
        print(f"section: {self.section}")

sai = Student("sai", "987654320", "pfs", "Python")
sai.display_info()

print()

kiran = Librarian("kiran", "8765432190", "CG01", "A")
kiran.display_info()

print()

ISBN = "1234567890"

if Person.validate_ISBN(ISBN):
    print("Valid ISBN")
else:
    print("Invalid ISBN")
























































