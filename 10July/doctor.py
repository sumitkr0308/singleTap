#Class Doctor has a method treat_patient().
#Class Teacher has method teach_students().
#Create a class Person that inherits from both and adds method introduce().
#Create object of Person and call all 3 methods.

class Doctor:
    def treat_patient(self):
             print("Doctor is Treating the Patient.")
class Teacher:
    def teach_students(self):
        print("Teacher is teaching the Students.")

class Person(Doctor,Teacher):
    def introduce(self):
        print("I am a Doctor and Teacher for Medical Students.")    
    
p1=Person()
p1.introduce()
p1.treat_patient()
p1.teach_students()    
        