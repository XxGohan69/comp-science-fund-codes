import random

number_to_guess = random.randint(1, 100)
guess = None
attempts = 0

print("Guess the number (between 1 and 100):")

while guess != number_to_guess:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
