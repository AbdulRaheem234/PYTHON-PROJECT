import random

# Generate random number between 1 and 100
target_number = random.randint(1, 100)

print("🎯 Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print("Try to guess it!")

guess_count = 0

while True:
    guess = int(input("Enter your guess: "))
    guess_count += 1

    if guess > target_number:
        print("Lower number please ❗")
    elif guess < target_number:
        print("Higher number please ❗")
    else:
        print(f"🎉 Correct! You guessed the number in {guess_count} tries.")
        break
