# Design a class Employee with name, emp_id, and salary.
# Add a method to calculate bonus (10% of salary).
# Create object and print bonus

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10


emp1 = Employee("Sumit Kumar", 101, 50000)

print(f"Employee Name: {emp1.name}")
print(f"Employee ID: {emp1.emp_id}")
print(f"Salary: ₹{emp1.salary}")
print(f"Bonus (10%): ₹{emp1.calculate_bonus()}")
