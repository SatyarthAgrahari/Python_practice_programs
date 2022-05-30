# Write a program to preform Insert, Search, Update, Delete
# operation with database connectivity by using given screen in
# tkinter.
from logging import exception

#import the module tkinter
from tkinter import *

#import the API module pymysql
import pymysql 
#import the message box for showing popup
import tkinter.messagebox as m

#creating main window
r=Tk()
#define the main window size
r.geometry("600x600")
#define the title
r.title("Student Detail")
#change the background colour
r.config(bg="grey")

#acquiring connection with database, connection function
def CreateConn():
    return pymysql.connect(host="localhost",database="student",user="root",password="root",port=3306)

#function for insetion data into database
def InsertData():
    #store arguments with get() method 
    rn=ern.get()
    n=en.get()
    l=el.get()
    e=el.get()
    c=ec.get()
    #check condition no entry box will be empty
    if(n=="" or l=="" or e=="" or e=="" or c==""):
        m.showinfo("Insert Status","All Fields are Mandatory")
    else:
        try:
            #Established connection with databse
            conn=CreateConn()
            cursor=conn.cursor()
            args=(rn,n,l,e,c)
            #sql Statement
            query="Insert into student(Roll_No,First_Name,Last_Name,EMAIL,CONTACT)Values(%s,%s,%s,%s,%s)"
            cursor.execute(query,args)
            conn.commit()
            m.showinfo("Instert Status","Data Inserted")
            conn.close()
        #Handling Exceptons
        except Exception as x :
            #print the exception
            print("Insert Exception ",x)

#update data into database
def UpdateData():
    #input from the user
    rn=ern.get()
    n=en.get()
    l=el.get()
    e=el.get()
    c=ec.get()
    #check the condition
    if(n=="" or l=="" or e=="" or e=="" or c==""):
        m.showinfo("Insert Status","All Fields are Mandatory for Update")
    else:
        try:
            #connect with database
            conn=CreateConn()
            cursor=conn.cursor()
            args=(rn,n,l,e.c)
            #sql statement
            query="Update student set Roll_No=%s,First_Name=%s,Last_Name=%s,Email=%s,Contact=%s"
            cursor.execute(query,args)
            conn.commit()
            m.showinfo("Update Status","Data Updated")
            conn.close()
        
        #Exception Handling
        except exception as y:
            #print the exception
            print("Update Exception :",y)

#deleting data in the database
def DeleteData():
    #aruments
    rn=ern.get()
    #check conditions 
    if rn=="":
        m.showinfo("Delete Status","Enter Roll No")
    else:
        try:
            #connect with database
            conn=CreateConn()
            cursor=conn.cursor()
            args=(rn)
            #sql statement
            query="Delete from student where Roll_No=%s"
            cursor.execute(query,args)
            conn.commit()
            m.showinfo("Deleted Status","Data Deleted")
            conn.close()
        #exception Handling
        except Exception as z:
            #print the exception
            print("Delete Exception :",z)
#searching data in databse
def Search_D():
    #argument
    rn=ern.get()
    #check conditions
    if rn=="":
        m.showinfo("Search Data","Enter Roll No")
    else:
        try:
            #connect with database
            conn=CreateConn()
            cursor=conn.cursor()
            args=(rn)
            #sql statement
            query="Select * From student where Roll_No=%s"
            cursor.execute(query,args)
            result= cursor.fetchall()
            for i in result:
                print(i)
                result.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],[4]))
        #Exception Handling
        except Exception as u:
            #print the exception
            print("Search Exception :",u)

#creating Labels on main window
rn=Label(r,text="Roll NO :")
rn.place(x=30,y=40)
n=Label(r,text="First Name :")
n.place(x=30,y=90)
l=Label(r,text="Last Name :")
l.place(x=30,y=140)
e=Label(r,text="Email :")
e.place(x=30,y=190)
c=Label(r,text="Contact :")
c.place(x=30,y=240)
#Adding Entry Box in main window
ern=Entry()
ern.place(x=110,y=40)
en=Entry()
en.place(x=110,y=90)
el=Entry()
el.place(x=110,y=140)
ee=Entry()
ee.place(x=110,y=190)
ec=Entry()
ec.place(x=110,y=240)
#adding Buttons on main window
Button1=Button(r,text="INSERT",bg="White",command=InsertData)
Button1.place(x=40,y=300)
Button2=Button(r,text="SEARCH",bg="White",command=Search_D)
Button2.place(x=100,y=300)
Button3=Button(r,text="UPDATE",bg="White",command=UpdateData)
Button3.place(x=170,y=300)
Button4=Button(r,text="DELETE",bg="White",command=DeleteData)
Button4.place(x=240,y=300)
#mainloop() method called for run the applicaton.
mainloop()
