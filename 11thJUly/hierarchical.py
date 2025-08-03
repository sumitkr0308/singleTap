# . Hierarchical Inheritance
# Create a base class Vehicle and two child classes Car and Bike.
# Each class should have its own method like drive() or ride().
# Call their respective methods from objects.

class Vehicle:
    def start(self):
        print("Vehicle is starting...")

# Child class 1
class Car(Vehicle):
    def drive(self):
        print("Driving the car...")

# Child class 2
class Bike(Vehicle):
    def ride(self):
        print("Riding the bike...")

# Creating objects
car_obj = Car()
bike_obj = Bike()
car_obj.start()     
car_obj.drive()     

bike_obj.start()    
bike_obj.ride()     
