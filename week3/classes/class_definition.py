class Phone:
    brand = "Unknown"
    
    def change_brand(self, b):
        self.brand = b

iPhone = Phone()
Samsung = Phone()
iPhone.brand = "Apple"

print(iPhone.brand)
print(Samsung.brand)

Samsung.change_brand("Samsung")
print(Samsung.brand)