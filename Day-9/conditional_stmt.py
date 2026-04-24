'''
Simple if

charger = int(input("Enter the charging: "))
if charger <= 20:
    print("charge the phone or turn on the power saving mode")

products = {
    1:{'name':'bread','discount':10},
    2:{'name':'sugar','discount':0},
    3:{'name':'jam','discount':5},
    4:{'name':'butter','discount':0}
    }
print(products)
index = int(input("Enter the index: "))
if products[index]['discount']:
    print(f'{products[index]["name"]} has a discount')
'''



'''
products = {
    1:{'name':'bread','bestseller':True},
    2:{'name':'sugar','bestseller':False},
    3:{'name':'jam','bestseller':True},
    4:{'name':'butter','bestseller':False}
    }
print(products)
index = int(input("Enter the index: "))
if products[index]['bestseller']:
    print(f'{products[index]["name"]} is a bestseller')
'''



'''
#if-else

jd = {'python', 'Mysql', 'javascript', 'flask'}
skills = set(input("enter the skills: "))
if jd==skills:
    print("congrats!! your resume is shortlisted")
else:
    print(f"sorry, try again. you need this skill set: {jd-skills}")
'''



'''
plan = False
if plan:
    print("Ads won't run. You can watch the video without interuption")
else:
    print("Ads will run. Subscribe to youtube premium")
'''



'''
#if-elif-else

fare = 0
wheels = int(input("Enter the wheels: "))
if wheels == 2:
    print("your bike is on the way")
elif wheels == 3:
    print("your auto is on the way")
elif wheels == 4:
    print("your cab is on the way")
else:
    print("Entered the invalid input")
'''



'''
#Nested if

status = input("Enter the status: ")
if status == 'face':
    print("unlock the mobile")
else:
    print("face not reg")
    if status == 'password':
        print("unlock the mobile")
    else:
        print("incorrect password")

'''














