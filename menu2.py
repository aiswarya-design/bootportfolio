# Menu driven code
# List operation
def createlist():
    l=[]
    count=int(input("enter the count"))
    for i in range(count):
        e=int(input("enter the element"))
        l.append(e)
    return l

def searchelement(l):
    element=int(input("search the element"))
    if element in l:
        print("the element is present in the list")
    else:
        print("the element is not prenet in the list")
def displaylist(l):
    print(l)
l=[]
while(1):
    print("List operation")
    print("Createlist")
    print("Searchelement")
    print("Displaylist")
    print("exit")
    ch=int(input("enter your choice"))
    if ch==1:
       l= createlist()
    elif ch==2:
        searchelement(l)
    elif ch==3:
        displaylist(l)
    elif ch==4:
        exit()
