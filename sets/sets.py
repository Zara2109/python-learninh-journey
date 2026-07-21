# Creating Sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)


# Adding an Element

set1.add(10)
print("After add():", set1)


# Removing an Element

set1.remove(2)
print("After remove():", set1)


# Union

print("Union:", set1.union(set2))


# Intersection

print("Intersection:", set1.intersection(set2))


# Difference

print("Difference (set1 - set2):", set1.difference(set2))


# Symmetric Difference

print("Symmetric Difference:", set1.symmetric_difference(set2))


# Membership Test

print("Is 5 in set1?", 5 in set1)

numbers = {1, 1, 2, 2, 3, 3, 4}

print("Duplicates Removed:", numbers)

#This demonstrates that sets automatically remove duplicates.
