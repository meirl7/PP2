
n = int(input())

f = False

for i in range(2, n):
    if n % i != 0:
        f = not f
print("Yes" if f else "No")