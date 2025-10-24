import random


def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    guesses = 0

    print("Welcome to the Number Guessing Game!")
    print("I've selected a number between 1 and 100. Can you guess it?")

    while True:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            guesses += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(
                    f"Congratulations! You guessed the number in {guesses} attempts!")
                break
            elif guess < secret_number:
                print("Higher number please!")
            else:
                print("Lower number please!")

        except ValueError:
            print("Please enter a valid number between 1 and 100.")


# Start the game
number_guessing_game()
