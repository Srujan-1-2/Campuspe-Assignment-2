num = int(input("Enter a number: "))
if num < 0:
    print("Factorial not possible for negative numbers")
elif num == 0:
    print("0! = 1")
else:
    fact = 1
    print(str(num) + "! =", end=" ")
    for i in range(num, 0, -1):
        print(i, end="") 
        if i > 1:
            print(" × ", end="")
        fact = fact * i
    print(" =", fact)