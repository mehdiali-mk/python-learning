"""
AIM: Create Account class with 2 attributes - Balance and Account No.
Create methods for debit, credit & printing the balance.
Author: Mehdiali
Date: 03 / June / 2024 - 03:26 PM
"""

class Account:

    def __init__(self, balance, accountNo):
        self.balance = balance
        self.accountNo = accountNo
        self.printBalance()
    
    def printBalance(self):
        print("Current Balance [", self.accountNo, "] =", self.balance)

    def debit(self, ammountToDebit):
        if (self.balance < ammountToDebit):
            print("You do not have enough money!!!, Please credit some.")
        else:
            self.balance -= ammountToDebit
            print(ammountToDebit, "has been debited.")
            self.printBalance()
    
    def credit(self, ammountToCredit):
        self.balance += ammountToCredit
        print(ammountToCredit, "has been credited.")
        self.printBalance()

person1 = Account(100000, 123456)
person1.debit(50000)
person1.credit(25000)
