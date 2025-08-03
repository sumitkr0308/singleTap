#class student:take name and marks of 3 subjects calculate and print average

class Student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3

    def calculateAverage(self):
        return (self.mark1+self.mark2+self.mark3)/3

    def printAverage(self):
        print(f"Average Marks of {self.name.capitalize()} in 3 subjects = {self.calculateAverage()}")

s1=Student("Sumit", 95,85,78)
s1.printAverage()            
   
        