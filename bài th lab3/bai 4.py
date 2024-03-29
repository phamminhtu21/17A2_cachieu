# a:
print("Hình 1: ")
for i in range(5):
    print(" " * (5 - i), end = "")
    print("* " * (i + 1))
for i in range(4, -1, -1):
    print(" " * (4 - i), end = "")
    print(" *" * (i + 1))
print("\n")


# b:
print("Hình 2: ")
for i in range(7):
    print(" " * (7 - i), end = "")
    print("*" * (2 * i + 1))
for i in range(3):
    print("  " * 3, end = "")
    print("*" * 3)