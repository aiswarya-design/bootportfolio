#Menu driven for banking operations
class Account:
    def __init__(self):
        print("Enter the Account details")
        self.acctnumber=int(input("Enter the account number"))
        self.acctname=input("Enter the name")
        self.balance=int(input("enter the balance"))
    def withdraw(self):
        amount=int(input("Enter the amount"))
        self.balance=self.balance-amount
    def deposit(self):
        amount=int(input("Enter the amount"))
        self.balance=self.balance+amount
    def showbalance(self):
        print(self.acctnumber,"Current Available Balance is:",self.balance)
l=[]
while(1):
    print("Banking operations")
    print("1.Create an account")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.showbalance")
    print("5.Exit")

    ch=int(input("Enter your choice"))
    if ch==1:
        a=Account()
        l.append(a)
        for i in l:
            print(i.acctnumber,i.acctname,i.balance)
    elif ch==2:
        number=int(input("Enter the number"))
        for i in l:
            if(number==i.acctnumber):
                i.withdraw()
                break
        else:
            print("Account does not exist")

    elif ch==3:
        number=int(input("Enter the number"))
        for i in l:
            if(number==i.acctnumber):
                i.deposit()
                break
        else:
            print("Account does not exist")
    elif ch==4:
        number=int(input("Enter the number"))
        for i in l:
            if(number==i.acctnumber):
                i.showbalance()
                break
        else:
            print("Account does not exist")
    elif ch==5:
            exit()
