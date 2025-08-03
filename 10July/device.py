# Class Device → method power_on()
# Class Computer → method boot()
# Class Laptop → method open_lid()
# Use Laptop object to call all 3 methods.


# Base class
class Device:
    def power_on(self):
        print("Device is powered on.")

# Derived from Device
class Computer(Device):
    def boot(self):
        print("Computer is booting...")

# Derived from Computer
class Laptop(Computer):
    def open_lid(self):
        print("Laptop lid is opened.")

# Create Laptop object and call all 3 methods
l = Laptop()
l.power_on()
l.boot()
l.open_lid()
