class Library:
    def __init__(self):
        print("Enter the book details")
        self.bookid=int(input("Enter the book id"))
        self.title=input("Enter the Book title")
        self.author=input("Enter the author of the book")
        self.price=int(input("Enter the price"))
        self.pages=int(input("Enter the pages"))
    def showdetails(self):
        print("BookId:",self.bookid,"Title:",self.title,"Author:",self.author,"Price:",self.price,"Pages:",self.pages)
    def updatebook(self):
        attr=input("Enter the attribute(title/author/price/all) you want to update")
        if attr=="title":
            self.title=input("Enter the new title")
        elif attr=="author":
            self.author=input("Enter the new author")
        elif attr=="price":
            self.price=int(input("Enter the new price"))
        elif attr=='all':
            self.title = input("Enter the new title")

            self.author = input("Enter the new author")

            self.price = int(input("Enter the new price"))
        else:
            print("Invalid Choice")
    def deletebook(self):
        l.remove(self)
        print("Book details is deleted")
    print("Book details is deleted")


l=[]
while(1):

    print("Libaray Management")
    print('1.Add Book')
    print('2.Display Book List')
    print('3.Details of a Book')
    print('4.Update a book')
    print('5.Delete a book')
    print('6.exit')

    ch=int(input("Enter the choice"))

    if ch==1:
        b=Library()
        l.append(b)
    elif ch==2:
        for i in l:
            i.showdetails()
    elif ch==3:
        id=int(input("Enter the id of book"))
        for i in l:
            if(id==i.bookid):
                i.showdetails()
                break
        else:
            print("book does not Exist")

    elif ch==4:
        id = int(input("Enter the id of book"))
        for i in l:
            if (id == i.bookid):
                i.updatebook()
                break
        else:
            print("book does not Exist")
    elif ch==5:
        id = int(input("Enter the id of book"))
        for i in l:
            if (id == i.bookid):
                i.deletebook()
                break
            else:
                print("book does not Exist")
                exit()