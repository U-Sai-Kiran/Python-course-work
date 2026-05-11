#Exceptional Handling
'''
try:
    n+=10
except NameError:
    print("variable name not defined")
else:
    print("No error")
finally:
    print("end of thr program")



try:
    #n+=10
    #a= int(input("enter the integer: "))
    #l = [1,2,3,4,4]
    #print(l[10])
    #k = {1:1,2:4,3:9,4:16}
    #print(k[9])
    #c=12/0
    m=10+'a'
except NameError:
    print("variable name not defined")
except ValueError:
    print("Enter the correct datatype")
except IndexError:
    print("Index out of range")
except KeyError:
    print("key is not found")
except ZeroDivisionError:
    print("can't divisible with zero")
except TypeError:
    print("can't add 2 diff datatypes")
else:
    print("No error")
finally:
    print("end of thr program")



try:
    #n+=10
    #a= int(input("enter the integer: "))
    #l = [1,2,3,4,4]
    #print(l[10])
    #k = {1:1,2:4,3:9,4:16}
    #print(k[9])
    #c=12/0
    #m=10+'a'
except (NameError,ValueError,IndexError,KeyError,ZeroDivisionError,TypeError) as e:
    print(f"Error occured: {e}")
else:
    print("No Error")
finally:
    print("End of the program")

'''


try:
    #n+=10
    #a= int(input("enter the integer: "))
    #l = [1,2,3,4,4]
    #print(l[10])
    #k = {1:1,2:4,3:9,4:16}
    #print(k[9])
    c=12/0
    #m=10+'a'
except Exception as e:
    print(f"Error occured: {e}")
else:
    print("No Error")
finally:
    print("End of the program")






















































    

