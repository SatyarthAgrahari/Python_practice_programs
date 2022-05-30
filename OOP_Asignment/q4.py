# Create child class Bus that will be inherit all of the methods of the
# Vehicle class.

#create class1
class vehical:  #parent class
    #create method with no argument
    def car(self):
        print("This is the common feature of cars")
    #create method with one argument
    def SUV(self,a):
        print("This is the large in size cars")
    #create method with two argument
    def Small(selfa,a,b):
        print("This is the small cars")
#create class2 with inherit the class1
class Bus(vehical): #child class

    def passenger(self):
        print("More seats")
#create the objects of child class
b=Bus()
b.car()
b.SUV(10)
#calling the methods
b.Small(10,20)
b.passenger()
