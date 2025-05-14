class Logger:
    def __init__(self):
        print("Message before: Logger object is created.")  

    def __del__(self):
        print("Message after: Logger object is destroyed.")

log = Logger()  # This will call the __init__ method and print "Logger initialized."
del log  # The __del__ method will be called when the object is about to be destroyed.  