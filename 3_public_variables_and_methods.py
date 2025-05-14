class Car():
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...!")

my_car = Car("BMW")
print(my_car.brand) # Output: BMW
my_car.start() # Output: BMW is starting...!

