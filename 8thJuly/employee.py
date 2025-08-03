#3.create an Employee class with a method get_salary().
#Create a Manager class that inherits from Employee and adds a method bonus().
#Print both salary and bonus using object.

class Employee:
    def __init__(self,salary):
        self.salary=salary
        
    def get_salary(self):
        return self.salary
        

class Manager(Employee):
    def __init__(self, salary,bonus_amt):
        super().__init__(salary) #inherit salary 
        self.bonus_amt=bonus_amt

    def bonus(self):
        return self.bonus_amt

m1=Manager(15000,5000)
print(f"Salary : {m1.get_salary()}")        
print(f"Bonus : {m1.bonus()}")

