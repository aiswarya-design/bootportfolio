#Define a function to find the occurance(count)of each character
s="hello world"
for i in s:
        print(i,' ',s.count(i))

#
# # l=[1,1,1,2,2,3,4,6,7,7,7]
# # #find the occurance of each other
# l=[1,1,1,2,2,3,4,6,7,7]
# s=set(l)
# for i in l:
#     print(i,' ',l.count(i))
# # #find the maximum length word from this string
s="python is a programming language"
l= s.split()
max = 0
w = ""
for i in l:
    if len(i) > max:
        max = len(i)
        w = i
print(w)