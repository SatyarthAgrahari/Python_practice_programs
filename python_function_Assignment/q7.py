#  Write a program to generate a random captcha list, using python inbuilt
# module.

#import the random module
import random

#create the list
l1=[22,334,1,10,2233]

for i in range(0,5):
    #choice() return random number from list
    x=random.choice(l1)
    #print the number
    print(x)