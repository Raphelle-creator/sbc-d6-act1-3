rows = int(input("Enter the number of rows for the pattern: "))

for i in range(rows, 1, -1):
    print("*" * i)

print("*" + " " * 4 + "*")

for x in range(2, rows + 1):
    print("*" * x)


