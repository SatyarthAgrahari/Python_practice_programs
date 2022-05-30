# Write a program to input two numbers from the user and
# check it’s an integer or not using Try and Except.

#use the try keyword
try:

    #Input two numbers from the user.
    a=int(input("Enter the value of A :"))
    b=int(input("Enter the value of B :"))
    #print the number
    print(a,b)

#if the exception occurs the catch the except keyword
except:
    
    #print the exception
    print("Enter the integer value.")