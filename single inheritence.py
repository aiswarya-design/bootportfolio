class Person:
    def _init_(self):
        self.name=input("Enter the name")
        self.age=int(input("Enter the age"))

    def showdetails(self):
        print(self.name,self.age)
class Employee(Person):
    def _init_(self):
        super()._init()  #super() used to call the parent method __init_
        self.empid=int(input("Enter the id"))
        self.salary=int(input("Enter the salary"))

    def showdetails1(self):
        #super().showdetails() #Super() is used to call the method showdetails()
        print(self.empid,self.salary)

e=Employee()
e.showdetails()
e.showdetails1()