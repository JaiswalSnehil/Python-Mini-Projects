import random

while True:
    input("\nPress Enter to roll the dice 🎲...")

    dice = random.randint(1, 6)
    print(f"You rolled: {dice}")

    while True:
        choice = input("Roll again? (y/n): ").lower()

        if choice == 'y':
            break
        elif choice == 'n':
            print("Game Over 👋")
            exit()
        else:
            print("Invalid input ❌ Please enter 'y' or 'n'")