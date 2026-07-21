# Function without parameters

def greet():
    print("Hello, welcome to Python!")


greet()


# Function with parameters

def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Zahrah")


# Function with return value

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print("Sum:", result)

# Nested Function

def outer_function():

    def inner_function():
        print("This is the inner function.")

    print("This is the outer function.")
    inner_function()


outer_function()

