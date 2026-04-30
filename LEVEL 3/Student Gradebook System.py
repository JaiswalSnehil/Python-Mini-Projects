import csv

FILE_NAME = "gradebook.csv"


# -------------------------
# Grade Logic
# -------------------------
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


# -------------------------
# Add Student
# -------------------------
def add_student(gradebook):
    name = input("Enter student name: ")

    try:
        n = int(input("Enter number of subjects: "))
    except ValueError:
        print("Invalid input ❌")
        return

    marks = []

    for i in range(n):
        try:
            m = float(input(f"Enter marks for subject {i+1}: "))
            marks.append(m)
        except ValueError:
            print("Invalid marks ❌")
            return

    total = sum(marks)
    avg = total / len(marks)
    grade = calculate_grade(avg)

    gradebook[name] = {
        "marks": marks,
        "total": total,
        "average": avg,
        "grade": grade
    }

    print("Student added successfully ✅")


# -------------------------
# View Students
# -------------------------
def view_students(gradebook):
    if not gradebook:
        print("No records found 📭")
        return

    print("\n--- STUDENT REPORT ---")
    for name, data in gradebook.items():
        print(f"\nName: {name}")
        print(f"Marks: {data['marks']}")
        print(f"Total: {data['total']}")
        print(f"Average: {data['average']:.2f}")
        print(f"Grade: {data['grade']}")


# -------------------------
# Save to CSV
# -------------------------
def save_to_file(gradebook):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Marks", "Total", "Average", "Grade"])

        for name, data in gradebook.items():
            writer.writerow([
                name,
                ",".join(map(str, data["marks"])),
                data["total"],
                f"{data['average']:.2f}",
                data["grade"]
            ])

    print("Report saved to file ✅")


# -------------------------
# Main Menu
# -------------------------
def main():
    gradebook = {}

    while True:
        print("\n--- GRADEBOOK MENU ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Save Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(gradebook)

        elif choice == "2":
            view_students(gradebook)

        elif choice == "3":
            save_to_file(gradebook)

        elif choice == "4":
            save_to_file(gradebook)
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice ❌")


# Run program
main()