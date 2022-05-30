# Write a program to insert the data into database using
# python.


#import the API module pymysql
import pymysql

#Acquiring Connection with Database, connection function
def CreateConn():
    return pymysql.connect(host="localhost",database="practise",user="root",password="root",port=3306)

#Create Function For Inserting Data.
def InsertData(name,email,city):
    conn=CreateConn()
    cursor=conn.cursor()
    args=(name,email,city)

    #Sql statement.
    query="insert into student(name,email,city)Values(%s,%s,%s)"
    cursor.execute(query,args)
    conn.commit()
    print("Data Inserted.")
    conn.close()
    
#creating variable for user input.
name=input("Enter yur name :")
email=input("Enter your email :")
city=input("In which city do you Live :")

#Call the Function
InsertData(name,email,city)
