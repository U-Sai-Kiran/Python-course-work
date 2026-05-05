data = {
    12345:{'pin':1234,'balance':5000,'history':[]},
    76543:{'pin':1234,'balance':7000,'history':[]},
    87652:{'pin':1234,'balance':9000,'history':[]},
    56776:{'pin':1234,'balance':4000,'history':[]},
    }

acc_num = None

def login(e_num,e_pin):
    if e_num in data and data[e_num]['pin']==e_pin:
        print("Login successfull")
        global acc_num
        acc_num = e_num
        return True
    else:
        print("invalid login")
        return False

def check_balance():
    print("Current_balance",data[acc_num]['balance'])

def deposit():
    amount = int(input("Enter the deposit amount: "))
    data[acc_num]['balance']+=amount
    data[acc_num]['history'].append(f'{amount} is deposited +++++++')
    print('deposit successfull')

def withdraw():
    amount = int(input("Enter the withdraw amount: "))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance']-=amount
        data[acc_num]['history'].append(f'{amount} is withdraw -------')
        print('withdraw successfull')
    else:
        print('insufficient balance')

def viewtransaction():
    if data[acc_num]['history']:
        print('------------ Transaction history ------------')
        for i in data[acc_num]['history']:
            print(i)
        print("------------End of the Transaction ------------")
    else:
        print("No transaction")


    

        
            

        
        
