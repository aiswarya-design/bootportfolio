class Person:
    def __init__(self,n,a):
        print("Creating a object")
        self.name=n
        self.age=a
    def show_details(self):
            print(self.name,self.age)
p1=Person('Arun',23)


p2=Person('Amal',24)

print(p1) # only print the reference/address of p1
print(p2) # only print the reference/address of p2
print(p1.name,p1.age)
print(p2.name,p2.age)# objectname.propertyname


p1.show_details()#objectnanme.methodname

p2.show_details()#objectname.methodname