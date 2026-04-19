def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added ✅")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available 📭")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task '{removed}' deleted 🗑️")
            else:
                print("Invalid task number ❌")
        except ValueError:
            print("Please enter a valid number ❌")


def main():
    tasks = []

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice ❌ Try again.")


# Run the app
main()