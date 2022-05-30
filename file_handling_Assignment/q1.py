# Write a program to create a .Txt File And Read An Entire
# Text File.

#string which store in the .txt file
s="This is the file handling program."

#creating the demo1.txt file in write mode.
file=open("demo1.txt","w")
#write the string in demo1.txt file
file.write(s)
print("File Created")
#close the file
file.close()
#open the demo1.txt in read mode 
f=open("demo1.txt","r")
#store the file context in variable
filecontent=f.read()
#print the varible in console
print(filecontent)
