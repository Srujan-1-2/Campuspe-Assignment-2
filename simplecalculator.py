num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"
modulus = num1 % num2 if num2 != 0 else "Undefined"
exponentiation = num1 ** num2
print("\nResults:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ^ {num2} = {exponentiation}")