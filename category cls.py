class Category: #base class
    def __init__(self):
        self.catname=input("Enter the Category")
    def showdetails(self):
        print("Categoryname",self.catname)

class product(Category): #child class
    def __init__(self):
        super().__init__()
        self.productname=input("Enter the product name")
        self.productprice=int(input("Enter the price"))
        self.description=input("Enter the description")
        self.quantity=int(input("Enter the quantity"))
    def showdetails(self):
        # super().showdetails() this is the fuctionally based call
        print("Categoryname",self.categoryname) #2nd way for call category names
        print("Productname",self.productname)
        print("Productprice",self.productprice)
        print("Productdescription",self.productdescription)
        print("Productquantity",self.productquantity)
p1=product()
p2=product()
p1.showdetails1()
p2.showdetails1()

