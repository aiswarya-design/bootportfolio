# list=[1,1,2,3,4,5,6,6]
# s=[]
# for i in list:
#     if(i not in s):
#         s.append(i)
# print(s)


# l=[1,2,3,4,5,6,7,8]

# # for i in range(1,4):
# #     for j in range(1,i+2):
# #         print(j,end=" ")
# #     print()
#
# x=input("enter the string")
# rev=x[::-1]
# if(x==rev):
#     print("string is palindrome")
# else:
#     print("string is not palindrome")
# #14
# num=int(input("enter the number:"))
# s=str(num)
# sum=0
# temp=1
# for i in s:
#     temp=int(i)**len(s)
#     sum=sum+temp
# if(sum==num):
#     print(num,"is an armstrong number")
# else:
#     print(num,'is not an armstrong number')
# print()

# x=123
# # for i in x:
# #     print(i)
# d={0:'a',1:'b',2:'c'}
# for i in d:
#     print(i)
# x=['ab','cd']
# for i in x:
#     i.upper()
#     print(x)

# i=1
# while True:
#     if i%2==0:
#         break
#     print(i)
#     i+=2

# z=set('abc')
# z.add('san')
# z.update(set(['p','q']))
# print(z)

# x='abcd'
# for i in range(len(x)):
#     print(i)

# a=[1,2]
# print(a*3)

# a="4,5"
# nums=a.split(',')
# x,y=nums
# int_prod=int(x)*int(y)
# print(int_prod)

# sq=lambda x:x**2
# a=[]
# for i in range(5):
#     a.append(sq(i))
# print(a)

# def tester(*argv):
#     for arg in argv:
#         print(arg,end=" ")
#         tester('sunday','monday')

s1={1,2,3,4,5}
s2={2,4,6}
print(s1^s2)