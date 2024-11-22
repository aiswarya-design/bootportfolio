class Book:
    def __init__(self):
        print("Enter the Book details")
        self.bookid=int(input("Enter the Bookid"))
        self.title=input("Enter the Title")
        self.author=input("Enter the Author")
        self.price=int(input("Enter the price"))
        self.pages=int(input("Enter the Pages"))
    def gettitle(self):
        print("Title",self.title)

    def getauthor(self):
        print("Author", self.author)

    def getprice(self):
        print("Price", self.price)

    def getpages(self):
        print("No of Pages", self.pages)

    def setauthor(self):
        self.author = input("Enter the new author")
        print("The new updated author value of book")
        self.getauthor()

    def settitle(self):
        self.title = input("Enter the new title")
        print("The new updated title value of book")
        self.gettitle()

    def setprice(self):
        self.price = int(input("Enter the new price"))
        print("The new updated price value of book")
        self.getprice()

b1 = Book()
b2 = Book()
b1.gettitle()
b2.gettitle()

b1.settitle()
b2.setauthor()