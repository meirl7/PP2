import math

class Functions:
    def get_sin(self, angle):
        return math.sin(angle)
    def get_cos(self, angle):
        return math.cos(angle)
    def get_tan(self, angle):
        return math.tan(angle)
    def sqrt(self, value):
        return math.sqrt(value)

class Constants:
    def __init__(self):
        self.e = math.e
        self.pi = math.pi
        self.sq2 = math.sqrt(2)

class ProblemSolver(Functions, Constants):
    def get_len_between_two_pts(self, x1, y1, x2, y2):
        return super().sqrt(x1 * x2 + y1 * y2)
    
    def get_area_of_circle(self, radius):
        return super().pi * radius * radius


