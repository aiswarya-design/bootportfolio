# #squre of a number
# #using lambda function
# sq=lambda x:x**2
# print(sq(4))
#
# #userdefined
# def sq(x):
#     return x**2
# print(sq(4))

#MAP FUNCTION EXAMPLE
#using user defined
# l=[1,2,3,4]
# def square(x):
#     return x*x
# print(list(map(square,l)))
# print(tuple(map(square,l)))
#
# #using lambda
# l=[1,2,3,4]
# print(list(map(lambda x:x*x,l)))
# print(tuple(map(lambda x:x*x,l)))

#more than seaquance(Requirement:no of elements should be same)
# n1=[1,2,3,4]
# n2=[2,3,4,5]
# print(list(map(lambda a,b:a+b,n1,n2)))
#
# d=[{'name':'Arun','age':20,'place':'ekm'},{'name':'Anu','age':23,'place':'thr'},{'name':'manu','age':24,'place':'thr'}]
# print(list(map(lambda x:x['name'],d)))
# #using filter function
# n=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,n)))

# n=[56,23,89,12,90,5,101,17] #filter the number whose value greater than 50 and less than 100
# print(list(filter(lambda x:50<x<100,n)))
#
# n=[23,67,12,45,90,34] #filter those elements which are divisible by 3 and even
# print(list(filter(lambda x:x%3==0 and x%2==0,n)))
#
#  #functool module Reduce function
# n=[1,2,3,4]
# import functools
# print(functools.reduce(lambda x,y:x+y,n))
# given list l=[81,64,25,16,100
# write a program to create new sequence with square root of each element in the given sequence
# # expected output:[9,8,5,4,10]
# l=[81,64,25,16,100]
# import math
# print(list(map(lambda x:math.sqrt(x),l)))
#Given a list
# l=[23,45,100,102,678,56,34,90]
#
# # create a new sequence with elements whose value is less than 100
# print(list(filter(lambda x:x<100,l)))

#
# #Given a list
# s=["red","green",'yellow','blue','violet']
# # # craete a new sequence with strings whose length is less than 5
# print(list(filter(lambda x:len(x)<5,s)))
#
#
# #Given a list
# l=[-3,6,-12,-5,-34,56,-25,77,11]


 #Sum of positive odd numbers
 #sum of positive even numbers
 #sum of negative even numbers
 #sum of negative odd numbers

 #Count of Positive numbers and negative numbers
# l=[-3,6,-12,-5,-34,56,-25,77,11]
# import functools
# positive_odd=list(filter(lambda x:x>0 and x%2!=0,l))
# print("Positive odd",positive_odd)
# print("Sum of positive odd Numbers",functools.reduce(lambda x,y:x+y,positive_odd))
# positive_even=list(filter(lambda x:x>0 and x%2==0,l))
# print("Positive even",positive_even)
# print("Sum of positive even numbers",functools.reduce(lambda x,y:x+y,positive_even))
# negative_odd=list(filter(lambda x:x<0 and x%2!=0,l))
# print("Negative odd",negative_odd)
# print("Sum of negative odd numbers",functools.reduce(lambda x,y:x+y,negative_odd))
# negative_even=list(filter(lambda x:x<0 and x%2==0,l))
# print("Negative even",negative_even)
# print("Sum of negative even numbers",functools.reduce(lambda x,y:x+y,negative_even))


