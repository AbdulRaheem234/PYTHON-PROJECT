import random

print("Welcome to Snake 🐍, Water 💧, and Gun 🔫 Game!")
print("Rules: Snake drinks water, Water damages gun, Gun kills snake.")
print("Choices: S for Snake, W for Water, G for Gun")

# Choices mapping
choices = {'S': 'Snake', 'W': 'Water', 'G': 'Gun'}

# Score
user_score = 0
computer_score = 0

# Game loop
for round_num in range(1, 6):  # 5 rounds
    print(f"\nRound {round_num}")
    user_choice = input("Enter your choice (S/W/G): ").upper()

    if user_choice not in choices:
        print("❌ Invalid choice, try again.")
        continue

    computer_choice = random.choice(list(choices.keys()))

    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    # Winning rules
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 'S' and computer_choice == 'W') or \
         (user_choice == 'W' and computer_choice == 'G') or \
         (user_choice == 'G' and computer_choice == 'S'):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("💻 Computer wins this round!")
        computer_score += 1

# Final result
print("\n--- Game Over ---")
print(f"Your Score: {user_score}")
print(f"Computer Score: {computer_score}")

if user_score > computer_score:
    print("🎉 Congratulations! You won the game!")
elif user_score < computer_score:
    print("😔 Computer won the game. Better luck next time!")
else:
    print("🤝 It's a tie!")
