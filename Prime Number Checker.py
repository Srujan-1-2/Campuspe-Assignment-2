#Part 1: Check if a single number is prime. Handle negative numbers, 0, 1, & 2.
num = int(input("Enter a number: "))

# Check special cases first
if num < 0:
    print("Negative numbers are not prime.")

elif num == 0 or num == 1:
    print(num, "is NOT a prime number.")

elif num == 2:
    print("2 is a PRIME number.")

else:
    is_prime = True   # Assume number is prime

    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a PRIME number.")
    else:
        print(num, "is NOT a prime number.")
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:")

for number in range(start, end + 1):

    if number > 1:  # Prime numbers are greater than 1
        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break   # Stop checking if divisible

        if is_prime:
            print(number, end=", ")