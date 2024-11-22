# #functions
#
# #function definision
# #sum of two numbers
# # def add():
# #     num1=int(input("enter the number"))
# #     num2=int(input("enter the numebr"))
# #     sum=num1+num2
# #     print(sum)
# # add() #it is the call funtion
#
# #define a function to display a msg
# # def display():
# #     msg="hello"
# #     print(msg)
# # display()
# #define a function to find the factorial of a number
# # def fact():
# #     n=int(input("enter a number"))
# #     fact=1
# #     for i in range(1,n+1):
# #         fact=fact*i
# #     print("the factorial of a number",fact)
# # print()
# # fact()
# #define a function to revers of a number
# def reverse():
#     num = input("enter the number:")
#     rev = ''
#     for i in range(len(num) - 1, -1, -1):
#         rev = rev + num[i]
#     print("reverse of the number is", rev)
#     print()
# reverse()
#
# #define a function to check whether the number is prime or not
# def prime():
#     num = int(input("enter the number:"))
#     for i in range(2,num):
#         if (num % i == 0):
#             print("Not prime")
#             break
#         else:
#             print(" prime number")
# print()
# prime()
#define a function  to check whether the number is armstrong
# def check_armstrong():
#     num=input("enetr the number:")
#     l=len(num)
#     sum=0
#     for i in range(0,l):
#         sum=sum+int(num[i])**l
#     if(sum==int(num)):
#         print("Armstrong")
#     else:
#         print("not Armstrong")
# check_armstrong()

#function with parameters
# #sum of numbers
# def add(n1,n2):
#     sum=n1+n2
#     print(sum)
# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# add(num1,num2)#it is the function arguments,it assign the n1,n2
#display the msg
# def message(msg):
#     print(msg)
# msg=input("enter the msg")
# message(msg)
#factorial
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# n=int(input("enter the number"))
# fact(n,fact)




