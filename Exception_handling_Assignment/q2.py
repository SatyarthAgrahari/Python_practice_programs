# Write a program to input a string from the user evaluate
# using Try and Except.

#use the try keyword
try:
    #input a strring from user.
    a = str(input("Enter the value of X :"))
    #print the string
    print(a)
#use except keyword if exception occurs the sttore in e.
except Exception as e :
    #print the exception
    print("Exception value is not string caught :",e)
#form confirming our program run completely.
print("byy")