# Write a program to replace a word from the string.

#impot the re module
import re

#defining the string
str1="hello dear"
print("Before Replace :",str1)
rplc=str(input("Enter your name :"))

#sub(): this method use for match and replace pattern 
result=re.sub("dear",rplc,str1)
print(result)