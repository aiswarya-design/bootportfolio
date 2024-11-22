def create():
    d=dict()
    count=int(input("enter the count"))
    for i in range(count):
        e=int(input("enter the element"))
        d.key()
    return d
def searchelement():
    element=int(input("search the element"))
    if(element in d):
        print("the element is present")
    else:
        print("the element is not present")
def display():
    print(d)
while(1):
    print("dictionary operation")
    print("create")
    print("searchelement")
    print("display")
    print("exit")
    ch=int(input("enter the choice"))
    if(ch==1):
        create()
    elif(ch==2):
        searchelement()
    elif(ch==3):
        display()
    elif(ch==4):
        exit()
