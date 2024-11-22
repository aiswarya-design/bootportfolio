import re
data="""John is 40 and Mike is 34
        Sam is 33 and jose is 18"""

pattern1='[A-Z][a-z]+'
s=re.findall(pattern1,data)
pattern2='[0-9]{2}'
a=re.findall(pattern2,data)
print(a)
print(s)

# s="abd abcd abccd abcccd abed"
# a=re.findall('abc*d',s)
# print(a)
#abc*d -->abd abcd abccd abcccd
# s=re.findall('abc+d',s)
# print(s)
#abc+d --> ['abcd', 'abccd','abcccd']
# t=re.findall('abc?d',s)
# print(t)
#abc?d-->['abd','abcd']
# c=re.findall('abc{2}d',s)
# print(c)
#abc{2}d-->['abccd']
d=re.findall('abc{1,3}',s)
print(d)
#abc{1,3}d-->['abcd','abccd','abcccd']


