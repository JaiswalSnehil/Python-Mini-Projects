from datetime import datetime

birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")

today = datetime.today()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

# Adjust negative days
if days < 0:
    months -= 1
    days += 30  # approx

# Adjust negative months
if months < 0:
    years -= 1
    months += 12

print(f"Your age is: {years} years, {months} months, {days} days")