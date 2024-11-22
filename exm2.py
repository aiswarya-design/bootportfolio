#1.Given a list
# colors=['red','green','blue']
#    a).print the reverse list
#    b).print last element
#    c).Add a new element 'white' to the list
# #    d).update the color green into yellow
# #    e).print each element in the given list
# colors=['red','green','blue']
# for i in range (len(colors)-1,-1,-1):
#     print(colors[::-1])
#     print(colors[-1])
# colors.append('white')
# print(colors)
# colors[1]='yellow'
# print(colors)
# print(colors[0])
# print(colors[1])
# print(colors[2])
# 2.Given a list food=['burger','pizza','icecream','noodles','sandwitch']
#    print the food items at even index position
# food = ['burger', 'pizza', 'icecream', 'noodles', 'sandwitch']
# print(food[0:5:2])
# 3.Given a list
#     l=[367,123,566,232,900,456,891]
#     sum of all digits of all odd numbers in the given list
l=[367,123,566,232,900,456,891]
for i in l:
    if(i%2!=0):
        print(i)
        s=str(i)
        sum=0
        for j in s:
            sum=sum+int(j)
            print(sum)
# 4.l=[13,24,7,90,14,27,11]
#  print the prime numbers in the given list
#
# 5.l=[1,1,1,2,3,4,5,5,6,7,7]
#
# Given a list.check whether a particular number is present in the list or not.and if present also find the occurence of given number in the list
#
# 6.given a dictionary
#     population={'India':1000,'China':3000,'Paksitan':500}
# find the average population
#
# 7.given a nnumber n.Find the reverse of a number without using built in method
#
# 8.print the pattern
# 1
# 4 9
# 16 25 36
# 49 64  81  100
# 9.Print the Pattern
# *
# ***
# *****
# *******
# 10.print the fibinocci series
# 0,1,1,2,3,5,8,13,21