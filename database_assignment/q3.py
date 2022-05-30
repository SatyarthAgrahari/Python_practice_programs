# Write a program to fetch all the data from database table
# and print on console.


#import the API module pymysql
import pymysql

#Acquiring Connection with Database, connection function
def CreateConn():
    return pymysql.connect(host="localhost",database="practise",user="root",password="root",port=3306)

#Create function for showing Data store in Database
def ShowAllData():
    conn=CreateConn()
    Cursor=conn.cursor()

    #Sql Statement.
    query="Select * From student"
    Cursor.execute(query)
    result=Cursor.fetchall()
    for i in result:
        print(i)
    conn.close()
    
#Call the function
ShowAllData()