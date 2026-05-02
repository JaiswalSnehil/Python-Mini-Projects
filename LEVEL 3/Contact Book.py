import json
import os
import re

FILE_NAME = "contacts.json"


# -------------------------
# Validation Helpers
# -------------------------
def is_valid_phone(phone):
    # simple: digits only, length 7–15
    return phone.isdigit() and 7 <= len(phone) <= 15


def is_valid_email(email):
    # simple regex check
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


# -------------------------
# Load / Save
# -------------------------
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)
    print("Contacts saved 💾")


# -------------------------
# CRUD Operations
# -------------------------
def add_contact(contacts):
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty ❌")
        return

    if name in contacts:
        print("Contact already exists ❌")
        return

    phone = input("Enter phone: ").strip()
    if not is_valid_phone(phone):
        print("Invalid phone number ❌")
        return

    email = input("Enter email: ").strip()
    if not is_valid_email(email):
        print("Invalid email ❌")
        return

    contacts[name] = {"phone": phone, "email": email}
    print("Contact added ✅")


def update_contact(contacts):
    name = input("Enter name to update: ").strip()

    if name not in contacts:
        print("Contact not found ❌")
        return

    print("Leave field empty to keep current value.")

    phone = input(f"New phone ({contacts[name]['phone']}): ").strip()
    email = input(f"New email ({contacts[name]['email']}): ").strip()

    if phone:
        if is_valid_phone(phone):
            contacts[name]["phone"] = phone
        else:
            print("Invalid phone ❌")

    if email:
        if is_valid_email(email):
            contacts[name]["email"] = email
        else:
            print("Invalid email ❌")

    print("Contact updated ✏️")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted 🗑️")
    else:
        print("Contact not found ❌")


def search_contact(contacts):
    query = input("Enter name to search: ").strip().lower()

    results = {
        name: info
        for name, info in contacts.items()
        if query in name.lower()
    }

    if results:
        print("\n--- Search Results ---")
        for name, info in results.items():
            print(f"{name} | {info['phone']} | {info['email']}")
    else:
        print("No matches found ❌")


def view_contacts(contacts):
    if not contacts:
        print("No contacts available 📭")
        return

    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"{name} | {info['phone']} | {info['email']}")


# -------------------------
# Main Menu
# -------------------------
def main():
    contacts = load_contacts()

    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. View All Contacts")
        print("6. Save Contacts")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            update_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            view_contacts(contacts)
        elif choice == "6":
            save_contacts(contacts)
        elif choice == "7":
            save_contacts(contacts)
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice ❌")


# Run app
main()