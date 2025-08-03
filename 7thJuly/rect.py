#make a class rectangle that takes length and breadth.add a method to calculate area

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth   

rect1=Rectangle(15,4)
print(f"Area of Rectangle: {rect1.area()}")     