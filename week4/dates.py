from datetime import datetime, timedelta

# 1
current_date = datetime.now()

result_date = current_date - timedelta(days = 5)

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Date of 5 days ago:", result_date.strftime("%Y-%m-%d"))


# 2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:  ", yesterday.strftime("%d-%m-%Y"))
print("Today:", today.strftime("%d-%m-%Y"))
print("Tomorrow: ", tomorrow.strftime("%d-%m-%Y"))

# 3
dt_with_ms = datetime.now()
dt_without_ms = dt_with_ms.replace(microsecond = 0)

print("With microseconds:", dt_with_ms)
print("Without microseconds: ", dt_without_ms)

# 4
date1 = datetime(2026, 2, 20, 14, 15, 30)
date2 = datetime.now()

difference = date1 - date2

seconds_diff = difference.total_seconds()

print(f"Difference in seconds: {seconds_diff:.2f}")