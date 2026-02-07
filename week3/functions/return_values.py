def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

nums = [10, 20, 30, 40, 50]
s, a = get_stats(nums)
print(f"Sum: {s}, Avg: {a}")