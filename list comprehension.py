
# n=[1,2,3,4]
# normal method
# n=[1,2,3,4]
# new=[]
# for I in n:
# new.append(s)
# print(new)
#
# using map()
# print(list(map(lambda x:x**2,n))
#
# using list comprehension
# n=[1,2,3,4]
# new=[i**2 for i in n]  #-->[1,4,9,16]
# print(new)
# n=[1,1,1,1]
# new=[5 for i in n]
# print(new)    #-->[5,5,5,5]
# #
# l=[22,56,33,11,89,57,34]
# new=[i for i in l if i%2==0]
# print(new)


# a.creating a new list sequence with elements which contains letter 'n'
# fruits=['banana','apple','orange','cherry','pineapple']
# new=[i for i in fruits if 'n' in i]
# print(new)
# # b,creating a new list sequence with reverse of each elements
# fruits=['banana','apple','orenge','cherry','pinapple']
# new=[i[::-1] for i in fruits]
# print(new)

# c.creating a new list sequence with elements whose length less than 5
# fruits = ['banana', 'apple', 'orenge', 'cherry', 'pinaple']
# new= [i for i in fruits if len(i)<5]
# print(new)

# l=[56,12.6,45,90,-6,34.8,-5,-12,'hello','python']

# creating a new list sequence with only floating point values
# l=[56,12.6,45,90,-6,34.8,-5,-12,'hello','python']
# new=[i for i in l if type(i)==float]
# print(new)
# l = [56, 12.6, 45, 90, -6, 34.8, -5, -12, 'hello', 'python']
# new= [x for x in l if isdigit(x, float)]
# print(float_values)

# creating list with only positive values
# creating a list with only string types
# creating a list with elements whose value is divisible by 3 in the range(1,100)

#without using recursion
def count_down(n):
    for i in range(n,0):
        print(i)

count_down(3)
