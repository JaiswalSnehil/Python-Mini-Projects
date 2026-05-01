import hashlib
import os

FILE_NAME = "users.txt"


# -------------------------
# Hash Password
# -------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# -------------------------
# Load Users from File
# -------------------------
def load_users():
    users = {}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                username, hashed = line.strip().split(",")
                users[username] = hashed

    return users


# -------------------------
# Save User to File
# -------------------------
def save_user(username, password):
    with open(FILE_NAME, "a") as file:
        file.write(f"{username},{hash_password(password)}\n")


# -------------------------
# Register
# -------------------------
def register(users):
    username = input("Enter username: ")

    if username in users:
        print("Username already exists ❌")
        return

    password = input("Enter password: ")

    if len(password) < 4:
        print("Password too short ❌")
        return

    save_user(username, password)
    users[username] = hash_password(password)

    print("Registration successful ✅")


# -------------------------
# Login
# -------------------------
def login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    if username in users and users[username] == hashed:
        print("Login successful 🎉")
    else:
        print("Invalid credentials ❌")


# -------------------------
# Main Menu
# -------------------------
def main():
    users = load_users()

    while True:
        print("\n--- LOGIN SYSTEM ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register(users)

        elif choice == "2":
            login(users)

        elif choice == "3":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice ❌")


# Run program
main()