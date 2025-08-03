#2.create a vehicle class with a method start()
#create a class that inherit from vehicle and adds a method drive ().create an object
#and call both methods

class Vehicle:
    def start(self):
        print("Vehicle Started")
class Car(Vehicle):
    def drive(self):
        print("Car is being driven.")  

car1=Car()
car1.start()
car1.drive()