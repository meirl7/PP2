class Car:
    range = 0 # in km

    def __init__(self, model):
        self.model = model
    
    def drive(self, km):
        range += km

c1 = Car("Sedan")
c2 = Car("SUV")

c1.drive(100000)
c2.drive(10234)

print(c1.range)
print(c2.range)