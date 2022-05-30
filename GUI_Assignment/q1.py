# Write a program to preform Insert, Search, Update, Delete
# operation on student form using given screen(400x400) in tkinter


from cProfile import label
from cgitb import text

#import the module tkinter
from tkinter import *

#Create the main window using Tk() method
r=Tk()

#defind the main window size using geometry() module
r.geometry("400x400")
#write the Tile of main window using title() module
r.title("Student details")
#Define the Background colour
r.config(bg="grey")

#Adding Labels in main window
n=Label(r,text="First Name :")
n.place(x=30,y=40)
l=Label(r,text="Last Name :")
l.place(x=30,y=90)
e=Label(r,text="Email :")
e.place(x=30,y=140)
c=Label(r,text="Contact :")
c.place(x=30,y=190)

#Adding Entry box in main window
en=Entry()
en.place(x=110,y=40)
el=Entry()
el.place(x=110,y=90)
ee=Entry()
ee.place(x=110,y=140)
ec=Entry()
ec.place(x=110,y=190)

#Adding Buttons in main window
Button1=Button(r,text="INSERT",bg="White")
Button1.place(x=40,y=230)
Button2=Button(r,text="SEARCH",bg="White")
Button2.place(x=100,y=230)
Button3=Button(r,text="UPDATE",bg="White")
Button3.place(x=170,y=230)
Button4=Button(r,text="DELETE",bg="White")
Button4.place(x=240,y=230)

#mainloop() method called for run the application
mainloop()