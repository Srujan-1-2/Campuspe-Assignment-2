number = int(input("Enter number: "))
range_end = int(input("Enter range (end): "))
print("Multiplication Table of", number)
for i in range(1, range_end+1):
    print(number, "x", i, "=", number * i)