# Write a program to accept a list from the user and print the
# alternate element of list.

#Ceate Empty list
l1=[]

#take the user input
a=int(input("How many elements in List: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    #append the element in the list
    l1.append(ele)
for j in range(0,a):
    #print alternate element off the list
    print(l1[j])
