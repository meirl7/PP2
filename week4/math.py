import math

# 1
deg = float(input("Input degree: "))
print("Output radian:", math.radians(deg))

# 2
h = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))
print(((b1 + b2) / 2) * h)

# 3
n_s = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = (n_s * pow(side_length, 2)) / (4 * math.tan(math.pi / n_s))

print(f"The area of the polygon is: {area}")

# 4
b_len = float(input("Length of base: "))
h_p = float(input("Height of parallelogram: "))
print("Expected Output:", b_len * h_p)