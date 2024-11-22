# class A:
#     def show(self):
#         print("In first method")
#     def show(self,a):
#         print("In second metod")
#     def show(self,a,b):
#         print("In third method")
# a=A()
# #a.show()
# #a.show(10)
# a.show(10,20)

class A:
    def __init__(self,a):
        self.x=a

    # def __add__(self,other):
    #     return self.x++other.x
    #
    # def __sub__(self,other):
    #     return self.x - other.x
    #
    # def __mul__(self,other):
    #     return self.x*other.x
    #
    # def __truediv__(self,other):
    #     return self.x/other.x
    def __str__(self):
        return str(self.x)

obj1=A(10)
obj2=A(20)

# print(1+2)  #Integer addition
# print('1'+'2') #string concatination
# print([1]+[2]) #List marging

# print(obj1+obj2)
# print(obj1-obj2)
# print(obj1*obj2)
# print(obj1/obj2)
print(obj1)
#Inorder to implement our own implementation for + operator in user defined types like class
#we have to define the function __add__(ie,magical method)in our cls
#Suppose we want to implement - operator we use __sub__function
#for * we use __mul__ function and for / we use __div__ function
#operator overloading means  an operator behaves differently in different objects
#python provide a feature to implement custom behavior for our built in operators in our user defined types
#like class.this feature is called magical methods or dunder metods
#(eg: __add__,__sub__,__mul__,__div__)
