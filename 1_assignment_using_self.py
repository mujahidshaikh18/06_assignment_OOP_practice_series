class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")

student1 = student("Mujahid Shaikh", 90)
student1.display() # Student Name: Mujahid Shaikh Student Marks: 90

 

