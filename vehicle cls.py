#Hierarchial inheritence
class Vehicle:
    def getdetails(self):
        self.brand = input("Enter the brandname")
        self.model = input("Enter the model name")
        self.year = int(input("Enter the year of manufacture"))

    def showdetails(self):
        print(self.brand, self.model, self.year)

class Car(Vehicle):
    def getdetails1(self):
        super().getdetails()
        self.mileage = input("Enter the mileage")

    def showdetails1(self):
        super().showdetails()
        print(self.mileage)
class Bike(Vehicle):
    def getdetails2(self):
        super().getdetails()
        self.cc = int(input("Enter the cc"))

    def showdetails2(self):
        super().showdetails()
        print(self.cc)
c = Car()
c.getdetails1()
c.showdetails1()

b = Bike()
b.getdetails2()
b.showdetails2()