import math

class Vector2:
    x = 0
    y = 0

    def __init__(self):
        self.x = 0
        self.y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def __add__(self, other: Vector2) -> Vector2:
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Vector2) -> Vector2:
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other) -> Vector2:
        return Vector2(self.x * other, self.y * other)

    def __eq__(self, other: Vector2) -> bool:
        return self.x == other.x and self.y == other.y
    

a = Vector2(2.3, 4.5)
b = Vector2(4.1, 5.3)

c = Vector2(2, 9) + a
print(c.x, c.y)

d = a - b
print(d.x, d.y)
d *= 2
print(d.x, d.y)

e = a
print(e == a)