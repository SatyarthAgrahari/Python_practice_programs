# Write a program to match a string that contains only upper
# & lowercase letters

#import re module
import re

#define pattern 
ptrn="^[a-zA-Z]"
#deine string 
mystring="Abc 223as hjhj"
#match() method
x=re.match(ptrn,mystring)
#print the position
print(x)