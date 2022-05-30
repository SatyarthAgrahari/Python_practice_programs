# Write a recursive function to calculate the sum of number from 0
# to 10

#create function
def summation(n):
    if n==0:
        return 0
    else:
        #function call itself its Recursion
        return (n+summation(n-1))
#function call and result stored in variable
x=summation(10)
#print the output
print(x)
