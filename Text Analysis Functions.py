def count_characters(text):
    return len(text)
def count_words(text):
    return len(text.split())
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count
def count_consonants(text):
    consonants = 0
    for ch in text:
        if ch.isalpha() and ch.lower() not in "aeiou":
            consonants += 1
    return consonants
sentence = input("Enter a sentence: ")
print("\n--- Text Analysis Results ---")
print("Total Characters:", count_characters(sentence))
print("Total Words:", count_words(sentence))
print("Total Vowels:", count_vowels(sentence))
print("Total Consonants:", count_consonants(sentence))