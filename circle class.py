#Create a class named circle with property radius and methods getarea() and getperimreter()
class Circle:
    def __init__(self):
        self.radius=int(input("Enter the Radius"))
        self.perimeter=int(input("enter the Perimeter"))

    def getarea(self):
        area=3.14*self.radius**2
        print(area)
    def getperimeter(self):
        perimeter=2*3.14*self.radius
        print(perimeter)
c1=Circle()
c2=Circle()

c1.getarea()
c1.getperimeter()

c2.getarea()
c2.getperimeter()


