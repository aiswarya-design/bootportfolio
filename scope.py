#Global scope
# x=10
# print(x)
#
# def f():
#     print(x)
# f()

# #Local scope
# def f():
#     x=20  #localvariable
#     print(x)
# f()
# print(x)

#Global keyword #to change local scope to global scope
# def f():
#     global x
#     x=20
#     print(x)
# f()
# print(x)

#global example
# x=20
# def f1():
#     print(x)
#
# def f2():
#     print(x)
# f1()
# f2()
# print(x)

# #local example
# # def f1():
# #     global x
# #     x=20
# #     print(x)
# # def f2():
# #     print(x)
# # f1()
# # f2()
#
# #Nonlocal Scope or Enclosed Scope
# def outer():
#     x=20
#
#     def inner():
#
#         x=30
#         print("inside the inner function",x) #-->30
#     print("inside the outer function before calling",x)  #-->20
#     inner()
#     print("inside the outer function after calling",x)  #--->20
# outer()

#built in scope
#from math import pi
import math

def f1():
    print(math.pi)
def f2():
    print(math.pi)
f1()
f2()
print(math.pi)





