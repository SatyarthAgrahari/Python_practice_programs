# Write a program to delete a single data from the database table
# using python.

#import the API module pymysql.
import pymysql

#Acquiring the connection with database<connection Function.
def CreateConn():
    return pymysql.connect(host="localhost",database="practise",user="root",password="root",port=3306)

#showing all data
def ShowAllData():
    conn=CreateConn()
    Cursor=conn.cursor()
    #Sql statement.
    query="Select * From student"
    Cursor.execute(query)
    result=Cursor.fetchall()
    for i in result:
        print(i)
    conn.close()
#foer deleting the data
def DeleteData(Sid):
    conn=CreateConn()
    cursor=conn.cursor()
    args=(Sid)
    #Sql Statement
    query="Delete from student where Sid=%s"
    cursor.execute(query,args)
    conn.commit()
    print("Data Deleted")
    conn.close()
#call the function for showing the data
ShowAllData()
Sid=int(input("Enter the Id you want to Delete :"))
#call function for deleting the data 
DeleteData(Sid)
#again call the function for showing the data.
ShowAllData()
