class Account:
    def __init__(self):
        self.accountno=int(input("Enter the Accountno:"))
        self.accountname=input("Enter the Account name")
        self.balance=int(input("Enter the Accountbalance"))

    def withdraw(self):
        amount=int(input("Enter the amount to withdraw"))
        self.balance=self.balance-amount
        print("Availale balance")
        self.showbalance()
    def deposit(self):
        amount=int(input("Enter the amount"))
        self.balance=self.balance+amount
    def showbalance(self):
        print("The balance is",self.balance)

a1=Account()
a2=Account()

a1.withdraw()
a1.deposit()
# a1.showbalance()

a2.withdraw()
a2.deposit()
# a2.showbalance()

