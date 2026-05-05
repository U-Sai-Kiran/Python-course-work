from logic import *

acc_num = int(input("Enter the account number: "))
pin = int(input("enter the pin: "))

if login(acc_num,pin):
    print("Welcome to the ATM")

    while True:
        print("[C]heck Balance")
        print("[D]eposit")
        print("[W]ithdraw")
        print("[V]iew")
        print("[E]xit")

        ch = input("Enter the choice: ").upper()
        if ch=='C':
            check_balance()
        elif ch=='D':
            deposit()
        elif ch=='W':
            withdraw()
        elif ch=='V':
            viewtransaction()
        elif ch=='E':
            print("Thankyou")
            break
        else:
            print("Enter the valid input")
