# A
print("Section A :")
for x in range(10, 21):
    print(f" {x} ")
# B
print("Section B :")
for x in range(10, 21):
    if x % 2 == 0:
        print(f" {x} ")

# C
print("Section C :")
skip: int = int(input("Enter skip number :"))
y = skip
for x in range(10, 20):
    if y == skip:
        print(f" {x} ")
    y = y - 1
    if y == 0:
        y = skip
