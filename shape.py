#abstract class and method

from abc import ABC,abstractmethod
class Shape(ABC): #Here shape is an abstract class.It declares two abstract methods area and perimeter
    def __init__(self,s):
        self.shapename=s


    def show(self):
        print(self.shapename)

    @abstractmethod #declares area() method as abstractmethod
    def area(self):
        print(self.area())
    @abstractmethod
    def perimeter(self):
        print(self.perimeter())#declares perimeter() method as abstractmethod
#Abstract class is ablue print/template for other classess that are inherited from this class.we cannot create
class Circle(Shape): #Circle class is a subclass of abstract class shape must provide the implementation of abstract methods.
    def __init__(self,shape):#Otherwise,it shows an error
        super().__init__(shape)
        self.radius=int(input("enter the radius"))
    def area(self):
        print(3.14*self.radius*self.radius)
    def perimeter(self):
        print(2*3.14*self.radius)
class Rectangle(Shape):
    def __init__(self,shape):
        super().__init__(shape)
        self.length=int(input("Enter the length"))
        self.width=int(input("Enter the breadth"))
    def calculate_area(self):
        print(self.length*self.width)
    def calculate_perimeter(self):
        print(2*(self.length+self.width))
c=Circle("circle")
c.show()
c.area()
c.perimeter()

r=Rectangle("rectangle")
r.show()
r.area()
r.perimeter()