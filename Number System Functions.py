def decimal_to_binary(num):
    return bin(num)[2:]
def decimal_to_octal(num):
    return oct(num)[2:]
def decimal_to_hexadecimal(num):
    return hex(num)[2:].upper()
def binary_to_decimal(binary):
    return int(binary, 2)
def octal_to_decimal(octal):
    return int(octal, 8)
def hexadecimal_to_decimal(hex_num):
    return int(hex_num, 16)
print("Choose Conversion Type:")
print("1. Decimal to Binary/Octal/Hexadecimal")
print("2. Binary to Decimal")
print("3. Octal to Decimal")
print("4. Hexadecimal to Decimal")
choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    num = int(input("Enter a decimal number: "))
    print("Binary:", decimal_to_binary(num))
    print("Octal:", decimal_to_octal(num))
    print("Hexadecimal:", decimal_to_hexadecimal(num))
elif choice == 2:
    binary = input("Enter a binary number: ")
    print("Decimal:", binary_to_decimal(binary))
elif choice == 3:
    octal = input("Enter an octal number: ")
    print("Decimal:", octal_to_decimal(octal))
elif choice == 4:
    hex_num = input("Enter a hexadecimal number: ")
    print("Decimal:", hexadecimal_to_decimal(hex_num))
else:
    print("Invalid choice!")