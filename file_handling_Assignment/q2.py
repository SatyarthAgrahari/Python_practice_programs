# Write a program To Append Text To a File and Display the
# text

#string which append into the file
s=" This is Python Program"
#instruct the demo1.txt for append mode
file=open("demo1.txt","a")
#write the string in the file
file.write(s)
print("File Updated")
#close the file
file.close()
