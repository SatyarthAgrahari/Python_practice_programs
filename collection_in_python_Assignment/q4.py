# Write a program to add element in list using for loop.

#create the empty list
l1=[]
a=int(input("How many elements in List: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    #append the element in list.
    l1.append(ele)
for j in range(0,a):
    print(l1[j])
