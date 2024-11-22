# class definition-->Dynamically
class Person:
    def __init__(self):
        print("Creating a object")
        self.name=input("Enter the name")
        self.age=int(input("Enter the age"))
    def show_details(self):
            print(self.name,self.age)
p1=Person()
p2=Person()

print(p1) # only print the reference/address of p1
print(p2) # only print the reference/address of p2
print(p1.name,p1.age)
print(p2.name,p2.age)# objectname.propertyname


p1.show_details()#objectnanme.methodname

p2.show_details()#objectname.methodname