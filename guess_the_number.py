"""
Author: Dhruv Patni
Repository: PyVerse
File: guess_the_number.py

Description:
-------------
A fun "Guess the Number" game built using Python.
The computer randomly selects a number between 1 and 100,
and the player must guess it in the fewest attempts possible.

Topics Covered:
- Loops
- Conditionals
- Random module
- User input/output
"""

import random

def guess_the_number():
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please guess a number between 1 and 100 only!")
                continue

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                break

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

    print("Thanks for playing! 👋")


if __name__ == "__main__":
    guess_the_number()
