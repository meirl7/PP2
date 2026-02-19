def generator1(n):
    for i in range(n):
        yield i * i
for i in generator1(12):
    print(i)


def generator2(n):
    for i in range(0, n, 2):
        yield i

cnt = int(input("Plase input some number: "))
for i in generator2(cnt):
    print(i, end=', ')