# Creating a List

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:", fruits)


# Accessing Elements

print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])


# Slicing

print("First Two Fruits:", fruits[:2])


# Adding Elements

fruits.append("Grapes")
print("After Append:", fruits)

fruits.insert(1, "Pineapple")
print("After Insert:", fruits)


# Removing Elements

fruits.remove("Banana")
print("After Remove:", fruits)

removed_item = fruits.pop()
print("Removed Item:", removed_item)
print("After Pop:", fruits)


# Length of List

print("Length:", len(fruits))


# Sorting

numbers = [5, 2, 8, 1, 9]

numbers.sort()
print("Sorted List:", numbers)


# Reversing

numbers.reverse()
print("Reversed List:", numbers)
