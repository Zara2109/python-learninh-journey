# Creating a Dictionary

student = {
    "name": "Zahrah",
    "age": 26,
    "course": "Python"
}

print("Dictionary:", student)


# Accessing Values

print("Name:", student["name"])
print("Course:", student.get("course"))


# Adding a New Key-Value Pair

student["city"] = "Hyderabad"
print("After Adding City:", student)


# Updating a Value

student["age"] = 27
print("After Updating Age:", student)


# Removing an Item

student.pop("city")
print("After pop():", student)


# Dictionary Keys, Values, Items

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# Looping Through a Dictionary

for key, value in student.items():
    print(key, ":", value)


# Checking if a Key Exists

print("name" in student)

employees = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}

for emp_id, emp_name in employees.items():
    print(f"{emp_id}: {emp_name}")
    