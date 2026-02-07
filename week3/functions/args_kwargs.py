def build_order(customer, *items, **details):
    print(f"Customer: {customer}")
    for item in items:
        print(f"Item: {item}")
    for key, value in details.items():
        print(f"{key}: {value}")

build_order("John", "Laptop", "Mouse", shipping="Express", wrap=True)