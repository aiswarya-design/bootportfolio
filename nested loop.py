#
#
#
# for i in range(1,4):   #nested loop
#     for j in range(1,4):
#         print(i,end=' ')
#     print()
# print()
# for i in range(1,4):
#     for j in range(1,5):
#         print(i,end=' ')
#     print()
# print()
#
#
#
#
# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=' ')
#     print()
# print()
# for i in range(1,4): #3 lines    i  rows
#     for j in range(1,5):#4 column j
#         print('*',end=' ')
#     print()
# print()
# #
# # l=['kelly','jenny','emi']
# #
# # #Output:
# # #kelly kelly kelly
# # #jenny jenny jenny
# # #emi    emi   emi
# #
#
# l=['kelly','jenny','emi']
# for i in l:
#     for j in range(1,4):
#         print(i,end=' ')
#     print()
#
#
# # #2
# serial_no=[1,2,3]
# qns=['what','why','when']
# for i in serial_no:
#     print(i)
#     for j in qns:
#
#         print(j,end=' ')
#         print()
#     print()
# # #Output:
# # 1.
# # what
# # why
# # when
# # 2.
# # what
# # why
# # when
# # 3.
# # what
# # why
# # when
# #
# d={1:['lion','tiger','horse'],2:['cat','dog','cow']}
#
#
# for i in d.values():
#     for j in i:
#         print(j)
# print()
# #working
# # i=['lion','tiger','horse']  j--->lion    lion   #print
# #                              ---->tiger  tiger
# #                              ---->horse  horse
# # i=['cat','dog','cow']       j---->cat    cat
# #                             ------>dig   dog
# #                             ------>cow   cow
# #
#
#
#
#
# # #Output
# # lion
# # tiger
# # horse
# # cat
# # dog
# # cow
#
#
# # #Print Multiplication table for (1....10)
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=' ')
#     print()
# #
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6.............20
# ......
# ......
# 10203040..........100


#fibinocci series
#logic
# 0 1 1 2 3 5 8 13 21
# a=0
# b=1
# print a   0---> print
# for i in range(8):   #remaining numbers
#     print(b)    1---->print()
#     a,b=b,a+b  ----->swapping

# a=0
# b=1
# print(a)
# for i in range(8):
#     print(b)
# a, b = b, a + b