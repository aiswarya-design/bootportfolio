#print the string upto specific character (including that character)
# s="python is a programming language"
# ch=input("Enter the character:")
# for i in range(-1,len(s)):
#     if(s[i]==ch):
#         break
#     print(s[i+1],end=" ")
# print()

# #method2
# for i in s:
#     print(i,end=' ')
#     if(i==ch):
#         break
# #print those numbers that are not divisible by 7 and 5 in the range (1500,2700) using continue statement
# for i in range(1500,2701):
#     if (i%7==0 and i%5==0):
#         continue
#     print(i,end=" ")
# print()


#check whether the number is prime or not
#1
# count=0
# num=int(input("enter the number:"))
#
# for i in range(2,num): #except 1 and that number   { (num-1)=num (that number included in factors)}
#     if(num%i==0):
#         count=count+1   #there is any extra factors  count increament by 1
#         break
# if(count==0):
#     print("prime number") #no extra factors its prime----
# else:
#     else:
#     print("not prime number")
# print()
#
# # 2
# num = int(input("enter the number:"))
#
# for i in range(2,num):
#     if (num % i == 0):
#         print("Not prime")
#         break
# else:
#     print(" prime number")
# print()
#
# # working
# num = 4
# i -->(2, 3)
# i = 2
# 4 % 2 == 0
# true
# not prime
#
# num = 5
# i - --2, 3, 4
# i = 2
# 5 % 2 == 0
# false
# i = 3
# 5 % 2 == 0
# false
# i = 4
# 5 % 2 == 0
# false
# else