class A:
    def show(self):
        print("Method from class A")

class B(A):
    def show(self):
        print("Method from class B")
              
class C(A):
    def show(self):
        print("Method from class C")

class D(B, C):
    pass

# Creating an object of class D
d = D()

# Calling the show method to observed the Method Resolution Order (MRO)
d.show()

# Printing the MRO to observed the order
print(D.mro())

# Output [<class '__main__.D'>, <class '__main__.B'>, class '__main__.C'>, <class '__main__.A'>, <class 'object'>]