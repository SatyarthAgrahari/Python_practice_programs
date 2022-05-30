# Write a program to check that a string contain only a certain
# set of characters(in this case a-z,A-Z,0-9).

#import the re module
import re
  
#define pattern which to be matched
pattern = "^[a-zA-Z0-9]"
#mystring would be searched to match the pattern at the beginning of string.
mystring = "3are6Earn"

#match() pattern matches at the beginningof the string
x=re.match(pattern,mystring)

#print the position 
print(x)