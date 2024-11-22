#  #Factors of a number
# # # num=int(input("enter the number:"))
# # # for i in range(1,num+1):
# # #     if(num%i==0):
# # #         print(i,end=" ")
# # # print()
# #
# #
# # # #Sum of digits in a number
# # n=input("enter the number:")  #string input
# # #s=str(n)
# # sum=0
# # for i in n:
# #     sum=sum+int(i)
# # print("sum of digits:",sum)
# # print()
# #
# # #or
# # # for i in (range(0,len(n)):
# # #     sum=sum+int(n[i])
# # # print(sum)
# #
# #
# #
# #
# # #Check whether the number is Armstrong or not
# #
# # # # method1
# n=input("enter the number")
# sum=0
# l=len(n)
# for i in n:
#     sum=sum+int(i)**l
# print(sum)
# if(int(n)==sum):
#     print("armstrong")
# else:
#     print("not armstrong")
#
# # # # #method2
num=int(input("enter the number:"))
s=str(num)
sum=0
temp=1
for i in s:
    temp=int(i)**len(s)
    sum=sum+temp
if(sum==num):
    print(num,"is an armstrong number")
else:
    print(num,'is not an armstrong number')
print()
# #
# #
# # # #Reverse of a number
# num=input("enter the number:")
# rev=''
# for i in range(len(num)-1,-1,-1):
#     rev=rev+num[i]
# print("reverse of the number is",rev)
# print()
#
# #
# # #Factorial of a number using for loop
# n=int(input ("Enter a number: "))
# fact=1
# for i in range(1,n+1):
#         fact=fact*i
# print("Factorial of the given number is: ", fact)
# print()
# #Find the average age  using loop
# d={101:['Arun',23,'ekm'],102:['Anu',24,'tvm'],103:['Amal',27,'tvm']}
# sum=0
# for i in d.values():
#    # print(i[1])
#     sum=sum+i[1]
#     avg=sum/3
# print("average:",avg)
# print()
# #
# #
# # #l=[1,1,2,3,5,7,7,7,9,3] remove duplicates from the list.(without using built in function).
# #without using fun
# l=[1,1,2,3,5,7,7,7,9,3]
# s=[]
# for i in l:
#     if(i not in s):
#         s.append(i)
# print(s)

# #logic
#  i=1   s=[]         true     s=[1]
#  i=1   s=[1]        false
#  i=2   s=[1]        true     s=[1,2]
#  i=3   s=[1,2]      true     s=[1,2,3]
#  i=5   s=[1,2,3]    true     s=[1,2,3,5]
#  i=7   s=[1,2,3,5]  true     s=[1,2,3,5,7]
#  -
#  -
#  -
#  i=3.................false

#using fun
# s=set(l)
#print(list(s))