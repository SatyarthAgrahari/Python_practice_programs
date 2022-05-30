# Write a program to search the number (0-9) of length between 1
# to 3 in a string.


#import the re module
import re
#search the number of length 1 to 3
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")

for n in results:
    # group():- returns the part of the string where there was a match
    print(n.group(0))