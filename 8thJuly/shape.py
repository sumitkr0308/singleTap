1.#Create a class Shape with a method area() (as a placeholder).
#Create a Square class that inherits from Shape and calculates the area based on user input side.
#Print the area.

class Shape:
    def area(self):
        pass #placeholder method
class Square(Shape):
  
    def __init__(self,side):
            self.side=side
    def area(self):
         return self.side*self.side

side=float(input("Enter the side of a Square: "))
s1=Square(side)
print(f"Area of a Square : {s1.area()}")

