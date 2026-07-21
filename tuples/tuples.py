# Creating a Tuple

colors = ("Red", "Blue", "Green", "Yellow")

print("Tuple:", colors)


# Accessing Elements

print("First Color:", colors[0])
print("Last Color:", colors[-1])


# Slicing

print("First Two Colors:", colors[:2])


# Length of Tuple

print("Length:", len(colors))


# Tuple Packing

person = ("Zahrah", 26, "Python Learner")

print("Packed Tuple:", person)


# Tuple Unpacking

name, age, role = person

print("Name:", name)
print("Age:", age)
print("Role:", role)


# Count Method

numbers = (1, 2, 3, 2, 4, 2)

print("Count of 2:", numbers.count(2))


# Index Method

print("Index of 3:", numbers.index(3))
