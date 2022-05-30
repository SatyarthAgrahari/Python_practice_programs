# Write a program to create Mysql Database and connect with
# the database.

#import the API module pymysql
import pymysql

#Acquiring Connection with Database, connection function
def CreateConn():
    return pymysql.connect(host="localhost",database="practise",user="root",password="root",port=3306)

#create Table function
def CreateTable():
    conn=CreateConn()
    cursor=conn.cursor()

    #Sql Statement.
    query="CREATE TABLE STUDENT(Sid INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(50),Email VARCHAR(50),City VARCHAR(50))"
    cursor.execute(query)
    conn.commit()
    print("Table Created.")
    conn.close()
    
#call the function.
CreateTable()