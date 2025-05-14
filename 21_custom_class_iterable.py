class Countdown:
    def __init__(self, start):
        self.start = start # Set the starting number
        self.current = start # Initialize the current number to the starting number

    def __iter__(self):
        # Return the iterator object itself
        return self

    def __next__(self):
        # if the current number is less than or equal to 0
        if self.current < 0:
            # Raise the StopIteration exception to signal the end of the iteration
            raise StopIteration
        # Decrement the current number by 1
        self.current -= 1
        return self.current + 1
    
countdown = Countdown(5)

# Using the countdown object in a for loop
for number in countdown:
    print(number) #output: 5 4 3 2 1 0