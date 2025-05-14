class Multiplier:
    def __init__(self, factor):
        self.factor = factor # setting the factor

    def __call__(self, number):
        # This method will be called when the object is called like a function
        return number * self.factor
    
multiplier = Multiplier(5)

# Testing with callable() to check if the object is callable
print(callable(multiplier)) # output: True

# Calling the object like a function to multiply an input by the factor
result = multiplier(10) # This calls __call__(10) method
print(result) # output: 50