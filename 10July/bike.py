#Class Bike has method wheels(), class Color has method color_name().
#Create a class Model that inherits both and adds method show_model()

class Bike:
    def wheels(self):
        print("Bike has 2 wheels.")

class Color:
    def color_name(self):
        print("Color of Bike is Black.")

class Model(Bike,Color):
    def show_model(self):
        print("This is the Ducati Monster 821.")


b1=Model()
b1.wheels()
b1.color_name()
b1.show_model()        


