# Create Vehicle class and create one method without any
# body.

#create class1
class Vehical: #parent class
    #create method
    def Electric_V(self):
        pass
#create class2 which inherit the class1
class BMW(Vehical): #child class
    #defining method
    def Electric_V(self):
        print("EV offter is 6.5% OFF")
#create class3 which inherit the class1
class Tesla(Vehical): #child class
    def Electric_V(self):
        print("EV offter is 2% OFF")
#creating the objects of child class
b=BMW()
t=Tesla()
#calling the method
b.Electric_V()
t.Electric_V()