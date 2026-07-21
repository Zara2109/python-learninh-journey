# Lambda Function

square = lambda x: x ** 2

print("Square of 5:", square(5))


# Lambda with Multiple Arguments

add = lambda a, b: a + b

print("Sum:", add(10, 20))


# Filter Function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)


# Map Function

squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Squared Numbers:", squared_numbers)


# Sorting with Lambda

students = [
    ("Sara", 85),
    ("Ali", 92),
    ("John", 78)
]

students.sort(key=lambda student: student[1])

print("Sorted by Marks:")
print(students)
