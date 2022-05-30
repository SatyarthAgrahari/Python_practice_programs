# Write a program to input two number from the user and
# check its an integer or not using Try and Except, if number
# are integer then the print sum of that number using finally
# block.

#use try keyword
try:
    #input two numbers from user.
    a=int(input("Enter the value of A :"))
    b=int(input("Enter the value of B :"))

#if exception occurs so use except keyword
except Exception as e:

    #print the exception
    print("Exception caught :",e)
    
#use finally keyword which run always
finally:
    #use the operators
    c=a+b
    # print the value of c
    print(c)
