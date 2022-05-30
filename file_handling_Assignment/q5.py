#  Write a program to Read List From the File . 

#instruction for read the file
f=open("demo2.txt","r")

#store the data in the variable
filecontent=f.readlines()
#print the content
print(filecontent)