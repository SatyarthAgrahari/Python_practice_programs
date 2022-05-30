# Write a program to Store Given List [“ Apple “, “ Mango ” , ”
# Orange ” ] Into File.

#create the list.
l1=["Apple","Mango","Orange"]
#instruction for writing data into file
file=open("demo2.txt","w")
#write the list in the file
file.writelines(l1)
print("File Created")
#close the file.
file.close()