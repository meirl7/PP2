users = [
    {"name": "Zoe", "score": 88},
    {"name": "Alex", "score": 95},
    {"name": "Mark", "score": 82}
]

by_name = sorted(users, key=lambda x: x["name"])
by_score = sorted(users, key=lambda x: x["score"], reverse=True)

print(by_name)
print(by_score)