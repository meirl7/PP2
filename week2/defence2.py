names = {
    "Dimash": 23,
    "Aibyn": 43,
    "Meirlan": 18,
    "Sanzhar": 9
}

allowed = ["Meirlan", "Sanzhar"]

result = []

for i in names:
    age = names[i]
    if (age in range(18, 24)) and (i in allowed):
        result.append(i)

print(result)