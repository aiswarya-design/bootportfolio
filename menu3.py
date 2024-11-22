def createset():
    s=set()
    count=int(input("enter the count"))
    for i in range(count):
        e=int(input("enter the element"))
        s.add(e)
    return s
def searchelement():
    element=int(input("enter the element"))
    if(element in s):
        print("the element is present")
    else:
        print("the element is not present")
def displayset():
    print(s)
s=set()
while(1):
    print("Set operation")
    print("createset")
    print("searchelement")
    print("displayset")
    print("exit")
    ch=int(input("enter the choice"))
    if(ch==1):
        s=createset()
    elif(ch==2):
        searchelement()
    elif(ch==3):
        displayset()
    elif(ch==4):
        exit()