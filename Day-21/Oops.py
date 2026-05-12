class flipkart:
    #class attributes
    discount = 10
    products = ["men's footwear", "sports wear", "footwear"]

    #class methods
    @classmethod
    def showproducts(cls):
        for i in cls.products:
            print(i)

    @classmethod
    def showdiscount(cls):
        print("Discount",cls.discount)

    #instance method
    def userinfo(self,username,phoneno):
    #instance attributes
        self.username = username
        self.phoneno = phoneno
        print(f"welcome to the flipkart {self.username}. shop now")

    #static method
    @staticmethod
    def banner():
        print("10% discount is going on")

#obj defining
sai = flipkart()

#using object
sai.userinfo("Sai","987654320")

#using object
sai.banner()

#using class
flipkart.banner()

#using class
flipkart.showproducts()
flipkart.showdiscount()

#using object
sai.showproducts()
sai.showdiscount()



'''
1.class attritube - Inside the class, using classname and objectname
2.Instance attritube - Outside the class, using objectname

1.class methods - @classmethod, first para "cls", using classname and objectname
2.instance methods - self, using objectname
3.static methods - @staticmethod, using class and objectname
'''
































