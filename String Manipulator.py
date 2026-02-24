sentence = input("Enter a sentence: ")
print("\nOriginal:", sentence)
total_with_spaces = len(sentence)
print("Characters (with spaces):", total_with_spaces)
total_without_spaces = len(sentence.replace(" ", ""))
print("Characters (without spaces):", total_without_spaces)
words = sentence.split()
print("Words:", len(words))
print("UPPERCASE:", sentence.upper())
print("lowercase:", sentence.lower())
print("Title Case:", sentence.title())
if words:
    print("First word:", words[0])
else:
    print("First word: (no words entered)")
if words:
    print("Last word:", words[-1])
else:
    print("Last word: (no words entered)")
reversed_sentence = sentence[::-1]
print("Reversed sentence:", reversed_sentence)