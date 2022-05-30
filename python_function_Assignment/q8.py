#  Write a program to shuffle captcha list, using python inbuilt module.

#import the random module
import random 
#create the list
l1=["Apple","Mango","Graps","Kiwi","Banana"]
for i in range(0,5):
    #shuffle the list using shuffle() method
    random.shuffle(l1)
    #print the output
    print(l1)