#write a program to maximum of 3 numbers
a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))

if(a>b and a>c):
    print("Number" ,a,"is biggest")
elif(b>a and b>c):
    print("Number",b, "is biggest")
else:
    print("Number" ,c, "is biggest")