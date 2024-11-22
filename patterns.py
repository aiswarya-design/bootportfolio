# #* * * * *
# #* * * * *
# #* * * * *
# #* * * * *
# #* * * * *
# for i in range(1,5):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()
#
# for i in range(1,4):
#     for j in range(1,4):
#         print("1",end=" ")
#     print()
#
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()
#
# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()
#
# # *
# # * *
# # * * *
# # * * * *
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# print()
#
# #1
# #2 2
# #3 3 3
# #4 4 4 4
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#
# #1
# #1 2
# #1 2 3
# #1 2 3 4
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# #1
# #1 1
# #1 1 1
# #1 1 1 1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("1",end=" ")
#     print()
#
# #1
# #2 3
# #4 5 6
# #7 8 9 10
k=1
for i in range(1,5):
    for j in range(1,5):
        print(k,end=" ")
        k=k+1
    print()
# #1
# #2 1
# #3 2 1
# #4 3 2 1
# for i in range(1,5):
#     for j in range(i,0,-1):#revers direction of (1,i+1),j iteration(columns) based on the value of i,(row)
#         print(j,end=" ")
#     print()
# #*
# #* * *
# #* * * * *
# #* * * * * * *
#for i in range(2,9,2):#1,3,5,7,9
#      for j in range(1,i+1):#revers direction of (1,i+1),j iteration(columns) based on the value of i,(row)
#          print("*",end=" ")
#      print()

# #1
# #1 2
# #1 2 1
# #1 2 1 2
# for i in range(1,5):
#     for j in range(1,i+1): #j iteration(columns) based on the value of i,(row)
#         if(j%2==0):
#             print(2,end=" ")
#         else:
#             print(1,end=" ")
#     print()
# #A
# #BB
# #CCC
# #DDDD
# n=65
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(n),end="")
#     n=n+1
#     print()
#
# for i in range(1,5):
#     n=65
#     for j in range(1,i+1):
#         print(chr(n),end=" ")
#         n=n+1
#     print()
# #A
# #B C
# #D E F
# #G H  I J
# n=65
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(n),end=" ")
#         n=n+1
#     print()
#
# * *
# * * * *
# * * * * * *
# * * * * * * * *
#
# for i in range(2,9,2):#1,3,5
#      for j in range(1,i+1):#revers direction of (1,i+1),j iteration(columns) based on the value of i,(row)
#          print("*",end=" ")
#      print()
#
#* * * * *
#* * * *
#* * *
#* *
#*
#* *
#* * *
#* * * *
#* * * * *
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#
# #      *
# #   *  *
# # *  * *
# #* * * *
# k=3*2
# # for i in range(1,5):
# #
# #     for p in range(1,k+1):#for printing space
# #         print(end=" ")
# #
# #     k=k-2#after each itteration decrements k value by 2
# #     for j in range(1,i+1):
# #             print("*",end=" ")
# #     print()
# # #piramid
# # k=3*2
# # for i in range(1,5):
# #
# #     for p in range(1,k+1):#for printing space
# #         print(end=" ")
# #
# #     k=k-2#after each itteration decrements k value by 2
# #     for j in range(1,i+1):
# #             print("*",end="  ")
# #     print()
# k=3*2
# for i in range(1,5):
#
#     for p in range(1,k+1):#for printing space
#          print(end=" ")
#
#     k=k-2#after each itteration decrements k value by 2
#     for j in range(1,i+1):
#            print("*",end="  ")
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     k=k+2
#     for j in range(1,i+1):
#         print("*",end="  ")
#     print()

# k=2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     k=k+2
#
# print()
# for j in range(1,i+1): #j iteration(columns) based on the value of i,(row)
#          if(j%2==0):
#              print(2,end=" ")
#          else:
#              print(1,end=" ")
# print()