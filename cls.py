# class A():
#
# 	def __init__(self,count=100):
#
# 		self.count=count
#
#
#
# obj1=A()
#
# obj2=A(102)
#
# print(obj1.count)
#
# print(obj2.count)
# class A:
#     def __init__(self,name):
#         self.name=name
# a1=A("john")
# a2=A("john")

#
# a.change()
#
# print(a.num)
class A:

	def __init__(self,num):

		num=3

		self.num=num

	def change(self):

		self.num=7

a=A(5)

print(a.num)

a.change()

print(a.num)