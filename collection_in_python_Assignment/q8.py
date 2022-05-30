# Write a program to convert two given list into dictionary.
# List1 [1,2,3,4,5] , List2 [‘A’,’B’,’C’,’D’,’E’]

#Create the empty dictionary.
d1={}
#create the lsit
l1=[1,2,3,4,5]
l2=['A','B','C','D','E']
#reverse the list
l1.reverse()
l2.reverse()
for i in l1:
    for j in l2:
        #last element store in the x and y of the lis l1 and l2 respectively using pop() module
        x=l1.pop()
        y=l2.pop()
        #covert the given list into dictionary
        d1[x]=y

#print the Dictionary.
print("Dict is :",d1)

