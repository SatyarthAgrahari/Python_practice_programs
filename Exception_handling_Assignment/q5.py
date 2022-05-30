#  Write a program to print multiple except block.

#use try keyword
try:
    #without defining the variable print the variable
    print(x)
#if exception occurs so us except keyword
except Exception as e:
    #rint the exception
    print("Exception caught :",e)
#Multiple except block
except:
    #print the exception
    print("Variable is not define.")