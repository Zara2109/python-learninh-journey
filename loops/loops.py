# For Loop

print("For Loop:")

for i in range(1, 6):
    print(i)


# While Loop

print("\nWhile Loop:")

count = 1

while count <= 5:
    print(count)
    count += 1


# Break Statement

print("\nBreak Example:")

for num in range(1, 11):
    if num == 6:
        break
    print(num)


# Continue Statement

print("\nContinue Example:")

for num in range(1, 11):
    if num == 6:
        continue
    print(num)
    