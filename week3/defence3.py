class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("My name is", self.name)
        print(f"I'm {self.age} years old")

class Student(Person):
    def __init__(self, grade, name, age):
        self.grade = grade
        self.name = name
        self.age = age
    def introduce(self):
        super().introduce()
        print("Grade:", self.grade)

class Doctor(Person):
    def __init__(self, spec, hosp_name, name, age):
        self.spec = spec
        self.hosp_name = hosp_name
        self.name = name
        self.age = age
    def introduce(self):
        super().introduce()
        print("Spec:", self.spec)
        print("Hospital name", self.hosp_name)

person = Person("Meirlan", 18)
person.introduce()

print()

student = Student("1st year", "John", 19)
student.introduce()

print()

doctor = Doctor("Doctor of something", "Hospital number of 1", "Alex", 28)
doctor.introduce()