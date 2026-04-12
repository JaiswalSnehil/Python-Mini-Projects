import random

choices = ["rock", "paper", "scissors"]

while True:
    player = input("\nEnter rock, paper, or scissors (or 'q' to quit): ").lower()

    if player == 'q':
        print("Thanks for playing! 👋")
        break

    if player not in choices:
        print("Invalid input ❌ Try again.")
        continue

    computer = random.choice(choices)

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a draw 🤝")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win 🎉")

    else:
        print("You lose 😢")