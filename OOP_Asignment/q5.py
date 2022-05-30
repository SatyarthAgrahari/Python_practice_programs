#  Create a Vehicle class and create method of the class and same
# are integrate with another class.


class vehical:  #parent class
    def fun1(self):
        print("Common Feature")
class BMW(vehical):  #sub class
    def fun1(self):
        print("BMW feature")
        super().fun1()
class Tesla(BMW):  #child class
    def fun1(self):
        print("Tesla feature")
        super().fun1()
#create the object of child class
t=Tesla()
t.fun1()
