# Creating a Class

class Student:

    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


    # Method
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Creating Objects

student1 = Student("Zahrah", 26, "Python")

student2 = Student("Aisha", 24, "AWS")


# Accessing Object Methods

student1.display_info()

print()

student2.display_info()
