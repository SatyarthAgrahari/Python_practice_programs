#  Write a program to update a single data into a database table and
# print updated data on console using python.

#import the API module pymysql.
import pymysql

#Acquiring connection with databse ,connection Function
def CreateConn():
    return pymysql.connect(host="localhost",database="practise",user="root",password="root",port=3306)

#create function for showing data
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

#For Updating the Data.
def UpdateData(name,email,city,Sid):
    conn=CreateConn()
    cursor=conn.cursor()
    args=(name,email,city,Sid)

    #Sql Statement.
    query="Update student set Name=%s,email=%s,City=%s where Sid=%s "
    cursor.execute(query,args)
    conn.commit()
    print("Data Updated")
    conn.close()

#call the function for showing data
ShowAllData()

#creating Variable for user input.
Sid=int(input("Enter the student ID :"))
n=input("Enter the name :")
e=input("Enter Your Email :")
c=input("Enter your city :")

#call the function for update
UpdateData(n,e,c,Sid)
#showing the data.
ShowAllData()