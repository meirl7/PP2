class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def set_radius(self, r):
        self.radius = r

class Rectange(Shape):
    def set_length_and_width(self, length, width):
        self.length = length
        self.width = width
    def get_area(self):
        return self.lenght * self.width

c = Circle("Red")
c.set_radius(5)
print(c.color, c.radius)

q = Rectange("Green")
q.set_length_and_width(34, 12)
print(q.get_area())
