# Day 5: Loops (for, while, nested loops)


# For Loop
print("For Loop")
for x in range(5):
    print(x) # 0, 1, 2, 3, 4


# While Loop
print("While Loop")
x = 0
while x < 5:
    print(x) # 0, 1, 2, 3, 4
    x += 1


# Nested Loop
print("Nested Loop")
for x in range(5):
    for y in range(5):
        print(x, y) # 0 0, 0 1, 0 2, 0 3, 0 4, 1 0, 1 1, 1 2, 1 3, 1 4, 2 0, 2 1, 2 2, 2 3, 2 4, 3 0, 3 1, 3 2, 3 3, 3 4, 4 0, 4 1, 4 2, 4 3, 4 4



# print Peramid using Nested for loop
print("print Peramid")
for x in range(6):
    for y in range(x):
        print("*", end="")
    print()
