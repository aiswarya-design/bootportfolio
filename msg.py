#factorial
# import math
# while(1):
#     try:
#         x=int(input("enter the number"))
#         m=math.factorial(x)
#     except:
#         print("invalid Input")
#     else:
#         print(m)
#         break

#recursive function method
# import math
# def f():
#     try:
#         x=int(input("enter the number"))
#         m=math.factorial(x)
#     except:
#         print("invalid Input")
#         f()
#     else:
#         print(m)
# f()

# import math
# try:
#     x=int(input("enter the number"))
#     m=math.factorial(x)
# except Exception as s:
#     print(s)
# else:
#     print(m)


#finaly keyword

# try:
#     #normal program code
# except:
#     #handling code if exception occurs
# else:
#     #code to execute if no execption
# finally:
    #some code....(always executed)

#eg:
# try:
#     n=int(input("Enter the number"))
#     m=int(input("Enter the number"))
#     d=m/n
# except:
#     print("Zero Division Error")
# else:
#     print(d)
# finally:
#     print("try block is executed")


