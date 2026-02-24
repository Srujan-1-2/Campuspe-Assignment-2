year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year")
            print("Reason: Divisible by 400")
        else:
            print(year, "is NOT a Leap Year")
            print("Reason: Divisible by 100 but not 400")
    else:
        print(year, "is a Leap Year")
        print("Reason: Divisible by 4 but not 100")
else:
    print(year, "is NOT a Leap Year")
    print("Reason: Not divisible by 4")