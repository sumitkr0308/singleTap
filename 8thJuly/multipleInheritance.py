#Create a class Maths with a method add(a, b).
#Create a class Science with a method physics_topic().
#Create a class Student that inherits from both and adds a method show_info().
#Use all methods through an object.
class Maths:
    def add(self,a,b):
        return a+b
class Science:
    def physics_topic(self):
        return "Newton's Law of Motion."
class Student(Maths,Science):
    def show_info(self):
        return "I am a Student and I am studying Maths and Science both."   

s1=Student()
print("Addition: ",s1.add(5,6))
print("Physics Topic: ",s1.physics_topic())
print("Info: " ,s1.show_info())     

