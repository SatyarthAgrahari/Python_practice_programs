#  Create a Vehicle class and perform method overloading in
# class.

#create class
class vehical:
    #create module with no argument
    def car(sefl):
        print("This is the common feature of car")
    #create module with one argument
    def car(self,a):
        print("This is the unique feature of BMW")
    #create module with two argument
    def car(self,a,b):
        print("This is the unique feature of Tesla")
#create the objects of the class
v=vehical()
#call the method
v.car(10,20)