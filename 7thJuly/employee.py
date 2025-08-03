# class employee add method to calculate salart after bonus 

class employee:
    def __init__(self,salary):
        self.salary=salary
    def addBonus(self,bonus):
        self.bonus=bonus

    def newSalary(self):
        return self.salary+self.bonus


e1=employee(15000)
e1.addBonus(500)
print(f"Salary after Bonus: {e1.newSalary()}")            

        