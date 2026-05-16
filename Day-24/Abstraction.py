#Abstraction

from abc import ABC, abstractmethod
class payment(ABC):
    def input(self):
        print("Enter the amount")

    @abstractmethod
    def checkBalance(self):
        pass
    @abstractmethod
    def verifypin(self):
        pass

class UPI(payment):
    def checkBalance(self):
        print("check balance for upi")
    def verifypin(self):
        print("verified your pin with upi")

class Cards(payment):
    def checkBalance(self):
        print("check balance for card")
    def verifypin(self):
        print("verified your pin with card")

class NetBanking(payment):
    def checkBalance(self):
        print("check balance for netbanking")
    def verifypin(self):
        print("verified your pin for NetBanking")

class Wallet(payment):
    def checkBalance(self):
        print("check balance for wallet")
    def verifypin(self):
        print("verified your pin for wallet")


john = UPI()
print("john --- UPI")
john.input()
john.checkBalance()
john.verifypin()

cena = Cards()
print("cena --- Card")
cena.input()
cena.checkBalance()
cena.verifypin()

















        
