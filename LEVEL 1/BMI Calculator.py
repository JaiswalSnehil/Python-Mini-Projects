def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


# ---- User Input ----
try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (meters): "))

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")

except ValueError:
    print("Please enter valid numeric values.")