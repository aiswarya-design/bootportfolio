# #print the series 1,4,9,16,25,36,49,64,81,100
# i=1
# k=3
# while(i<=100):
#      print(i,end=" ")
#      i=i+k
#      k=k+2
# print()
#sum and product of series 1,2,3,.....,10
# i=1
# sum=0
# product=1
# while(i<=10):
#     sum=sum+i
#     product=product*i
# print("the sum of the series",sum)
# print("the product of the series",product)
# i=i+1
# print()

#count of even numbers in the range(1,100)
# i=1
# count=0
# while(i<=100):
#     print(i,end=" ")
#     count=count+1
#     i=i+1
#     print("count",count)
##Check whether the number is Armstrong or not
n=input("enter the number")
sum=0
l=len(n)
for i in n:
    sum=sum+int(i)**l
    print(sum)
    if(int(n)==sum):
        print("armstrong")
    else:
        print("not armstrong")
# #d={101:['Arun',23,'ekm'],102:['Anu',24,'tvm'],103:['Amal',27,'tvm']}.Find the average age  using loop
# # # #l=[1,1,2,3,5,7,7,7,9,3] remove duplicates from the list.(without using built in function).
# s=[]
# for i in l:
#      if s not in l:
#          s.append()
#
# #Reverse of a number without using built in function
#
# #l=[12,-3.4,'hello','a',78,9.8,45].create 3 lists  for different types from given list
# #print the pattern
# # 1111
# # 2222
# # 3333
# # 4444
# # k=1
# # for i in range(1,5):
# #      for j in range(1,5):
# #          print(i,end=" ")
# #          k=k+1
# #          print()
# ##print the series
# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10
#      #
# # k=3
# # for i in range(1,5):
# #     for j in range(1,i+1):
# #         print(k,end=" ")
# #     k=k+2
# # print()
#
# #Fibinocci Series 0,1,1,2,3,5,8,13,21
# a=0
# b=1
# print(a)
# for i in range(8):
#     print(b)
#     a,b=b,a+b
#check whether a  number is prime or not
# i=1
# num=int(input("enter the number"))
# for i in range(2,num):
#     if(num%i==0):
#         print("not prime")
#         break
#     else:
#         print("number is prime")
# print()