import random


def snake_water_gun():
    print("Welcome to Snake Water Gun Game!")
    print("Rules:\nSnake drinks Water\nWater drowns Gun\nGun kills Snake")
    choices = ['snake', 'water', 'gun']
    user_score = 0
    comp_score = 0
    rounds = 0
    while True:
        print("\nChoose one:")
        print("1. Snake\n2. Water\n3. Gun\n4. Quit")
        try:
            user_choice = int(input("Enter your choice (1-4): "))
            if user_choice == 4:
                print("\nFinal Scores:")
                print(f"You: {user_score} | Computer: {comp_score}")
                print("Thanks for playing!")
                break
            if user_choice not in [1, 2, 3]:
                print("Invalid input! Please enter 1, 2, 3, or 4.")
                continue
            user = choices[user_choice - 1]
            computer = random.choice(choices)
            print(f"\nYou chose: {user}")
            print(f"Computer chose: {computer}")
            # Determine the winner
            if user == computer:
                print("It's a tie!")
            elif (user == 'snake' and computer == 'water') or \
                 (user == 'water' and computer == 'gun') or \
                 (user == 'gun' and computer == 'snake'):
                print("You win this round!")
                user_score += 1
            else:
                print("Computer wins this round!")
                comp_score += 1
            rounds += 1
            print(
                f"\nScore after {rounds} rounds: You {user_score} - {comp_score} Computer")
        except ValueError:
            print("Please enter a valid number!")


# Start the game
snake_water_gun()
