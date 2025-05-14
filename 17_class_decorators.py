def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls

# Appling the class decoratorsto the person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, my name is {self.name}."
    
# creating an instance of the person class
person = Person("Zaid")

print(person.greet()) # output: Hello from Decorator!