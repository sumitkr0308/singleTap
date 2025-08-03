# create a class laptop with private variables _brand_price
# # use getter and setter to modify and access them

class Laptop:
    def __init__(self):
        self._brand = ""
        self._price = 0

    # Setter methods
    def set_brand(self, brand):
        self._brand = brand

    def set_price(self, price):
        self._price = price

    # Getter methods
    def get_brand(self):
        return self._brand

    def get_price(self):
        return self._price



laptop1 = Laptop()
laptop1.set_brand("Lenovo")
laptop1.set_price(45000)
print("Brand:", laptop1.get_brand())
print("Price:", laptop1.get_price())
