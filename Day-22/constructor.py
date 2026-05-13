#constructor

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f' hi {self.username}, welcome to instagram. follow your 5 friend')

sai = Instagram('sai','sai@123')


#Encapsulation

class Instagram:
    def __init__(self,username,email,password):
        self.username = username #public variable
        self._email = email     #protected variable
        self.__password = password  #private variable

        
    @property
    def emailaccess(self):
        return self._email

    @emailaccess.setter
    def emailaccess(self,new_email):
        self._email = new_email

    def getpassword(self):
        return self.__password

    def setpassword(self,new_password):
        self.__password = new_password


sai = Instagram('sai','sai@gmail.com','sai123')

print('before username:', sai.username)
sai.username = 'kiran'
print('after username:', sai.username)

print('before Email:', sai.emailaccess)
sai.emailaccess = 'kiran@gmail.com'
print('after email:', sai.emailaccess)

print('before password:', sai.getpassword())
sai.setpassword('kiran321')
print('after password:', sai.getpassword())





        
