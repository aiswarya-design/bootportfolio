#match()function

# import re
# s="pet:cat I love cats"
# #match() function checks only at the begining of the string
# m=re.match(r'pet:\w\w\w',s)# it returns match object
#
#
# if(m):
#     print("match found")
#     print(m.group())
# else:
#     print("not match found")

# import re
# s="I love cats pet:cat I lovre cow pet:cow"
# m=re.search(r'pet:\w\w\w',s)
#
# if(m):
#     print("match found")
#     print(m.group())
# else:
#     print("not matcch found")
#
# import re
# s="I love cats pet:cat I love cows pet:cow"
# m=re.findall(r'pet:\w\w\w',s)
# print(m)

# # Find all words starting with s,p or r and ends at 'at'
# import re
# s = "sat mat pat cat rat bat"
# m=re.findall('[spr]+at',s)
# print(m)
#
# # Find all words starting with except s,p or r and ends at 'at'
import re
# s = "sat mat pat cat rat bat"
# m=re.findall('[^ spr]+at',s)
# print(m)

# # # Find all 2 digit,3 digit and 4 digit numbers from the string
# s = "123 456 90 3455667 567 8960 87755343"
import re
# l=re.findall(r'\b[0-9]{2,4}\b',s)
# print(l)

#Find all 3letter 4 letter 5 letter words from the string
#
# s = "python is a high level programming language"
# import re
# l=re.findall(r'\b[a-z]{3,5}\b',s)
# print(l)


# #
# # # write a program to extract year,month,date from a url
# url = "https://www.washingtonpost.com/news/fottball-insider/wp/2016/09/02"
# import re
# m=re.findall(r'\d{4}/\d{2}/\d{2}',url)
# print(m)

# # # Find all words containing letter z
# ending with z-->[a-z]+z
# starting with z-->z[a-z]+
# # middile-->[a-z]+z[a+z]+
# s = "abcdz abzcd zabcd fghjkl"
# import re
# m=re.findall(r'\b[a-z]*z[a-z]*\b',s) # this pattern is any word containing z
# print(m)
# #To check whether a string contains only uppercase lowercase digits and underscore.
# s="abcdefghi1234567789"
# import re
# m=re.findall(r'^\w+$',s)
# print(m)
# ^-->starting of astring
# $-->end of a string
# only digits-->^\d+$
# only letters-->^[a-zA-Z]+$

# Example of sub function
# import re
# s="john@abc.com and mike@pqr.com"
# m=re.sub(r'@[a-z]+','@gmail',s)
# print(m)
# s="""Keep the blue flag
# flying high
# chelsea"""
# m=re.sub(r'\n',"",s)
# print(m)
# import re
# s="python, is a programming language."
# m=re.sub(r' ',':',s)
# print(m)

# Example of split function
# import re
# s="python is a programming language"
# m=re.split(r'\s',s)
# print(m)
# # or
# l=re.split(r'i',s)
# print(l)

# Sample programs
# Q1.Check whether an entered mobile number is valid or not (using dynamic input)
import re
number=input("enter the number")
m=re.search(r'\b^[6789]\d{9}$\b',number)
if m:
    print("number is valid")
else:
    print("number is not valid")
# Q2.write a program to find all words starting with a specfic letter (using dynamic input)
# import re
# letter=input("enter the letter")
# m=re.findall(r'[a-z]',letter)
#
# #
# #
#
#
# Q3.replace given date dd/mm/yy with dd-mm-yy
#
# for example 12/03/23 with 08-07-24


# Q4.find all valid email addresses


# s="""john@gmail.com,
#
# john__@gmail.com,
#
# john@.com,
#
# john_123@gmail.com,
#
# john_@gmail.com""""
