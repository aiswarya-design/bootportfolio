class A:
    def f(self):
        print("hello")


a=A()
# a.f()
# a.g()
class B(A):
    # def f(self):----->this is method overiding same functions in parent class and child class
    #     print("python")
    super().f()
    def g(self):
        print("helo")

b=B()
b.f()
b.g()