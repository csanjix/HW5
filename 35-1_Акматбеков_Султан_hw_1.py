class Person:
    def __init__(self, fullname, age, is_married):
      self.fullname = fullname
      self.age = age
      self.is_married = is_married

    def introduce_myself(self):
        print(f'My name is {self.fullname}.')
        print(f'I am {self.age}.')
        if self.is_married:
            print('I am married')
        else:
            print('I am not married')

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        self.marks = marks

    def calculate_average_mark(self):
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)

class Teacher(Person):
    def __init__(self, fullname, age, is_married, base_salary):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus_percentage = max(0, (self.experience - 3) * 0.05)
        return self.base_salary * (1 + bonus_percentage)

def created_students():
    student = []
    student1 = ['Sultan', 15, False, {'Math': 5, 'English': 5, 'Russian': 4}]
    student2 = ['Artur', 16, False, {'Math': 4, 'English': 5, 'Russian': 4}]
    student3 = ['Nikolai', 15, False, {'Math': 3, 'English': 3, 'Russian': 3}]

teacher = Teacher('Bolot', 57, True, 4, 30000)
teacher.introduce_myself()
print(f"My salary is ${teacher.calculate_salary():.2f}")

students = created_students()

for student in students:
    student.introduce_myself()
    print(f"Average Mark: {student.calculate_average_mark():.2f}")
    print("Marks:")
    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")
    print()