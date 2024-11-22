class Rectangle:
    def __init__(self):
        self.length=input("enter the number")
        self.breadth=input("enter the number")
    def calculate_area(self):
        return self.length*self.breadth
class Circle:
    def __init__(self,a,b):
        self.radius=a
    def calculate_area(self):
        return 3.14*self.radius*self.radius
    def print_area(object):
        print(object.calculate_area())

r=Rectangle()
c=Circle()

