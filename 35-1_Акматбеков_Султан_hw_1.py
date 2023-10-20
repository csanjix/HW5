class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'full name: {self.fullname}')
        print(f'age: {self.age}')
        print(f"is married: {'married' if self.is_married else 'single'}")

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        self.marks = marks

    def average_mark(self):
        total_marks = sum(self.marks.values())
        average_marks = total_marks / len(self.marks)
        return average_marks

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, base_salary):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        self.experience = experience
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus = max(0, self.experience - 3) * 0.05
        salary = self.base_salary + (self.base_salary * bonus)
        return salary


def create_students():
    students = []
    student1 = Student("John Doe", 16, False, {"Math": 65, "Science": 56, "History": 65})
    student2 = Student("Jane Smith", 15, False, {"Math": 54, "Science": 48, "History": 49})
    student3 = Student("Mike Johnson", 17, False, {"Math": 92, "Science": 65, "History": 64})
    students.extend([student1, student2, student3])
    return students


teacher = Teacher("Mr. Smith", 35, True, 8, 5000)
teacher.introduce_myself()
print(f"salary: {teacher.calculate_salary()}")
students = create_students()
for student in students:
    student.introduce_myself()
    print(f"marks: {student.marks}")
    print(f"average mark: {student.average_mark()}")
    print()