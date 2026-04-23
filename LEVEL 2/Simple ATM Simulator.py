def atm():
    correct_pin = "1234"
    balance = 1000.0

    # PIN verification
    attempts = 3
    while attempts > 0:
        pin = input("Enter your PIN: ")
        if pin == correct_pin:
            print("Login successful ✅")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN ❌ Attempts left: {attempts}")
    else:
        print("Too many incorrect attempts. Card blocked 🚫")
        return

    # Main menu loop
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"Your balance is: ₹{balance:.2f}")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount > 0:
                    balance += amount
                    print(f"₹{amount:.2f} deposited successfully 💰")
                else:
                    print("Invalid amount ❌")
            except ValueError:
                print("Please enter a valid number ❌")

        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount <= 0:
                    print("Invalid amount ❌")
                elif amount > balance:
                    print("Insufficient balance ❌")
                else:
                    balance -= amount
                    print(f"₹{amount:.2f} withdrawn successfully 💸")
            except ValueError:
                print("Please enter a valid number ❌")

        elif choice == "4":
            print("Thank you for using ATM 👋")
            break

        else:
            print("Invalid choice ❌ Try again.")


# Run the ATM simulator
atm()