data = ["Python", "JavaScript", "C++", "Java", "Go"]
# ####3
long_names = list(filter(lambda x: len(x) > 3, data))

# creating the list from 1 until 19
nums = range(20)
odds = list(filter(lambda x: x % 2 != 0, nums))

print(long_names)
print(odds)