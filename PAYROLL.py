#payroll application
from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self):
        self.name=input("Enter the name")
        self.age=int(input("Enter the age"))
        self.empid=int(input("Enter the id of Employee"))
    def showdetails(self):
        print("Employee Id",self.empid,"Employee Name",self.name)
    @abstractmethod
    def calculate_salary(self):
        pass
class Fixed_Employee(Employee):
    def __init__(self):
        super().__init__()
        self.salary=int(input("Enter the monthly salary"))
    def calculate_salary(self):
        print("Salary of",self.empid,"is",self.salary)


class Hourly_Employee(Employee):
    def __init__(self):
        super().__init__()
        self.hours=int(input("Enter the number of hours"))
        self.rate=int(input("Enter the rate/hour"))
    def calculate_salary(self):
        s=self.hours*self.rate
        print("Salary of",self.empid,"is",s)
l=[]
while(1):
    print("Payroll Application")
    print('1.Add Employee')
    print("2.Monthly salary")
    print("3.Exit")
    ch=int(input("Enter the choice"))

    if ch==1:
        type=input("enter the employee (fixed/hourly)")
        if type=="fixed":
            e=Fixed_Employee()
            l.append(e)
        elif type=="hourly":
            e=Hourly_Employee()
            l.append(e)
    elif ch==2:
        id=int(input("Enter the id of employee"))
        for i in l:
            if(i.empid==id):
                i.calculate_salary()
                break
        else:
            print("Employee Id does not exist")
    else:
        exit()

