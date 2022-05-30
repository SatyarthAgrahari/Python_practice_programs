# Write a program that matches a word at the beginning of a
# string.

#import the re module
import re

#defining the pattern 
ptrn="^python"

#define the string 
mystring="python is high level language"
#match method
x=re.match(ptrn,mystring)
#print the matched position 
print(x)