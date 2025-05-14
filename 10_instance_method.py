class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof Woof!"
    
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")
print(dog1.bark())
print(dog2.bark())
# Output: Buddy says Woof Woof!
#         Max says Woof Woof!