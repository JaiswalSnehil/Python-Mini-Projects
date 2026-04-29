import csv
import os

FILE_NAME = "expenses.csv"


# ------------------------
# Load Expenses From File
# ------------------------
def load_expenses():
    expenses = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append({
                    "date": row["date"],
                    "category": row["category"],
                    "amount": float(row["amount"])
                })

    return expenses


# ------------------------
# Save Expenses To File
# ------------------------
def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["date", "category", "amount"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for expense in expenses:
            writer.writerow(expense)

    print("Expenses saved successfully ✅")


# ------------------------
# Add Expense
# ------------------------
def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/etc): ")

    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("Invalid amount ❌")
        return

    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully 💸")


# ------------------------
# View All Expenses
# ------------------------
def view_expenses(expenses):

    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- All Expenses ---")
    print(f"{'Date':12} {'Category':15} {'Amount':10}")

    for e in expenses:
        print(f"{e['date']:12} {e['category']:15} ₹{e['amount']:.2f}")


# ------------------------
# Total Spend
# ------------------------
def total_spend(expenses):
    total = sum(e["amount"] for e in expenses)

    print(f"\nTotal Spending: ₹{total:.2f}")


# ------------------------
# Daily Spend
# ------------------------
def daily_spend(expenses):
    date = input("Enter date (YYYY-MM-DD): ")

    total = sum(e["amount"] for e in expenses if e["date"] == date)

    print(f"Spent on {date}: ₹{total:.2f}")


# ------------------------
# Main Menu
# ------------------------
def main():
    expenses = load_expenses()

    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spend")
        print("4. View Daily Spend")
        print("5. Save Expenses")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_spend(expenses)

        elif choice == "4":
            daily_spend(expenses)

        elif choice == "5":
            save_expenses(expenses)

        elif choice == "6":
            save_expenses(expenses)
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice ❌")


# Run app
main()