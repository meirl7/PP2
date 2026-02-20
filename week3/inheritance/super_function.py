class Human:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"My name is {self.name}")

class Student(Human):
    def __init__(self, name, grade):
        # super() is to get access methods and properties of a perent class
        super().__init__(name) # calling constructor of parent class
        self.grade = grade

    def print_name(self):
        super().print_name() # also calling parent class method
        print(f"I'm in grade {self.grade}")

s = Student("Meirlan", 11)
s.print_name()