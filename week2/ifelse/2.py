number = 7

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


temperature = 22

if temperature > 30:
     print("It's hot outside!")
elif temperature > 20:
      print("It's warm outside")
elif temperature > 10:
     print("It's cool outside")
else:
     print("It's cold outside!")


a = 2
b = 330
print("A") if a > b else print("B")


day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("No match")


