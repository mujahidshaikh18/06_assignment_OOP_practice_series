class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        return f"{self.engine_type} engine started."
    
class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start_car(self):
        return f"{self.brand} car is starting. {self.engine.start()}"

# creating an engine object
engine = Engine("V8")
# creating a car object with the engine object
car = Car("Ford", engine)
# calling the start_car method of the car object
print(car.start_car())
# Output: Ford car is starting. V8 engine started.
# In this example, the Car class has a composition relationship with the Engine class.