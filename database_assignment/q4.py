# Write a program to fetch individual data from database table and
# print on console using python.

#import the API module pymysql
import pymysql

#Acquiring Connection with Database, connection function
def CreateConn():
    return pymysql.connect(host="localhost",database="practise",user="root",password="root",port=3306)

#create function for showing data by student ID.
def ShowDatabyId(Sid):
    conn=CreateConn()
    cursor=conn.cursor()
    args=(Sid)

    #Sql statement.
    query="Select * From student where Sid=%s"
    cursor.execute(query,args)
    result=cursor.fetchall()
    for i in result:
        print(i)
    conn.close()
#creating variable for user input.
Sid=int(input("Enter the student ID: "))

#Call the function.
ShowDatabyId(Sid)