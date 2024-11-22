# print all odd numbers in the range(1,100) and print the count of those numbers
# i=1
# count=0
# while(i<=100):
#     if(i%2!=0):
#         print(i,end="")
#         count=count+1
#     print("count",count)
#     i=i+1
# print()
# print("count of odd numbers",count)
#count of numbers that are divisible by 8 in the range(200,300)
# i=200
# count=0
# while(i<=300):
#     if(i%7==0):
#         print(i,end=" ")
#         count=count+1
#         print("count",count)
#     i=i+1
# print()
#sum of series 1,2,3,4,5
i=1
sum=0
while(i<=5):
    sum=sum+i
    print("i",i,"sum",sum)
    i=i+1
print()
#print the sum and product of the series 5,15,25,35,45,55,65
i=5
sum=0
product=1
while(i<=65):
    sum=sum+i
    product=product*i
    i=i+1
    print("sum",sum,"product",product)
print()
#find the count of divisable by 4 and 6 in the range(1,100)
i=1
count=0
while(i<=100):
    if(i%4==0 and i%6==0):
        count=count+1
    i=i+1
print("count of numbers",count)
print()