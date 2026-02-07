prices = [100, 250, 400]
sale_price = list(map(lambda p: p * 0.9, prices))

names = ["alice", "bob", "charlie"]
upper = list(map(lambda n: n.upper(), names))

print(sale_price)
print(upper)