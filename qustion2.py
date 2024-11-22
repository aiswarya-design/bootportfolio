# #write aprogram to check whether the enterd
#  x=int(input("Enter the number"))
# if(10<=x<=99):
#     print("number is 2 digit number")
# elif(100<=x<=999
#     print("number is 3 digit number")
# elif(1000<=x<=9999):
#       print("number is 4 digit number")
# else:
#     print("the num is not 2digits,3digits,4digits")

 # #write a simple calculator program to perform basic arithmetic operations(+,-,/,*)
# num1=int(input("enter the 1st num:"))
# num2=int(input("enter the 2nd num:"))
# op=input("enter the operator (+,-,/,*):")
# if(op=='+'):
#     print("sum:",num1+num2)
# elif(op=='-'):
#    print("difference:",num1-num2)
# elif(op=='*'):
#     print("product:",num1*num2)
# elif(op=='/'):
#     print("division:",num1/num2)
# else:
#      print("invalid operator")
# #write a program to print a triangle is equilateral,isosceles or scalene
# x=int(input("enter the side"))
# y=int(input("enter the side"))
# z=int(input("enter the side"))
# if(x==y==z):
#      print("equilateral")
# elif(x==y or x==z or y==z):
#      print("isosceles")
# else:
#      print("scalene")

# #write a program to print no of days in a month.
month_name=input("enter the month")
l1=['jan','march','may','july','aug','oct','dec']
l2=['apr','june','sep','nov']
l3=['feb']
if(month_name in l1):
     print("month",month_name,"has 31 days")
elif(month_name in l2):
     print("month",month_name,"has 30 days")
elif(month_name in l3):
     print("month",month_name,"has 29 days")
else:
     print("invalid input")
