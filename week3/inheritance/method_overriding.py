class Class1:
    def print_class(self):
        print("Class1")

class Class2(Class1):
    def print_class(self):
        print("Overriding Class1")

a = Class2()
a.print_class()