class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price # Private attribute

    # Getter method
    @property
    def price(self):
        return self._price

    # Setter method
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    # Deleter method
    @price.deleter
    def price(self):
        print(f"Deleting the price of {self.name}")
        del self._price

product =Product("Laptop", 50000)

# Accessing the price using @property
print(product.price) #output: 50000

# Setting the price using @price.setter
product.price = 55000
print(product.price) #output: 55000

# trying to set a negative price
product.price = -5000 #output: ValueError: Price cannot be negative

# Deleting the price using @price.deleter
del product.price #output: Deleting the price of laptop
