#open close write read append
'''
file = open('pfs-52.txt','r')
print(file.read())
file.close()

file = open('pfs-52.txt','r')
print(file.readlines())
file.close()

file = open('pfs-52.txt','r')
print(file.readline())
file.close()


file = open('pfs-52.txt','r')
print(file.readline())
file.seek(0)
print(file.readlines())
file.seek(0)
print(file.read())

file.close()


with open('pfs-52.txt','r') as file:
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    print(file.read())


with open('pfs-52.txt','w') as file:
    file.write('brock,hardy,steve,austin')


with open('pfs-52.txt','a') as file:
    file.write('batch-52')


try:
    with open('pfs-.txt','r+') as file:
        file.write('batch-52')
        file.seek(0)
        print(file.read())
except Exception as e:
    print(f"Error occured: {e}")
'''


try:
    with open('names.txt','w+') as file:
        for i in range(5):
            name = input("enter the names: ")
            marks = int(input("enter the marks: "))
            file.write(f'{name} : {marks}')
        file.seek(0)
        print(file.read())
except Exception as e:
    print(f'error occured: {e}')


















