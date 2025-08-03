# student result management

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  # Dictionary: {"Math": 90, "Science": 80, ...}

    def total_marks(self):
        return sum(self.marks.values())

    def average(self):
        return self.total_marks() / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A+'
        elif avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 50:
            return 'D'
        else:
            return 'F'

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print(f"  Total: {self.total_marks()}, Average: {self.average():.2f}, Grade: {self.grade()}")


# Main logic
students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    subjects = int(input("Enter number of subjects: "))
    marks = {}
    for _ in range(subjects):
        subject = input("Enter subject name: ")
        score = int(input(f"Enter marks for {subject}: "))
        marks[subject] = score
    students[roll] = Student(roll, name, marks)

def view_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        students[roll].display()
    else:
        print("Student not found!")

def view_all_students():
    if not students:
        print("No student records found.")
    else:
        for s in students.values():
            s.display()
            print("-" * 30)

while True:
    print("\n--- Student Result Management ---")
    print("1. Add Student")
    print("2. View Student Result")
    print("3. View All Students")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        view_all_students()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")

