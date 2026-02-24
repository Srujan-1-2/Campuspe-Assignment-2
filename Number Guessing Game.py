import random
secret_number = random.randint(1, 100)
print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")
guess = None
attempts = 0
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too Low! Try again.")
    elif guess > secret_number:
        print("Too High! Try again.")
    else:
        print("\n Congratulations!")
        print(f"You guessed the number in {attempts} attempts.")