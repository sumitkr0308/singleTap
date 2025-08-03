#Create class Person with name and age.
#Create class Skills with a list of skills.
#Class Employee should inherit from both and display all information (name, age, skills).

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Skills:
    def __init__(self,skill):
        self.skill=skill

class Employee(Person,Skills):
        def __init__(self, name, age,skill):
             Person.__init__(self,name, age)
             Skills.__init__(self,skill)
        def display(self):
             print("Name: ",self.name)
             print("Age: ",self.age)
             print("Skills: ",self.skill)


e1=Employee("Sumit",25,["Pyhton","C++","JavaScript"])
e1.display()
             


    