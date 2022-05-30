from logging import exception


#  Write a program to input two number from the user and handle
# your exception using else.

#use try keyword
try:
    #input the string from user
    a=str(input("Enter your Name :"))
    #print the string
    print(a)
#except keyword if exception occurs
except Exception as e:
    #print the exception
    print("Exception caught :",e)
#if no exceptions are found the print the else part
else:
    
    print("Nothing went wrong")