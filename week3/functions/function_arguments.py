def info(name, age, city="Unknown"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

info("Alice", 25) # thrid is default parameter
info("Bob", 30, "New York")