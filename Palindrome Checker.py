text = input("Enter word/number: ")
rev = text[::-1]
print("Original:", text)
print("Reversed:", rev)
if text.lower() == rev.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")