# class circle :circle method to calculate circumference and area
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def calculateCircumference(self):
        return 2*3.14*self.radius

    def calculateArea(self):
        return 3.14*(self.radius)**2

c1= Circle(4)
print(f"Circumference of a Circle: {c1.calculateCircumference()}")
print(f"Area of a Circle: {c1.calculateArea()}")


