#Create class University → College → Student.
# Each class should display their info using a method.
# Call all 3 from Student object.


# Base class
class University:
    def show_university(self):
        print("University: ABC University")

# Derived from University
class College(University):
    def show_college(self):
        print("College: XYZ Engineering College")

# Derived from College
class Student(College):
    def show_student(self):
        print("Student: Sumit Kumar")

# Create Student object and call all 3 methods
s = Student()
s.show_university()
s.show_college()
s.show_student()
