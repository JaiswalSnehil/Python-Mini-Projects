def convert_temperature(temp, unit):
    unit = unit.upper()

    if unit == "C":
        f = (temp * 9/5) + 32
        k = temp + 273.15
        print(f"{temp}°C = {f:.2f}°F = {k:.2f}K")

    elif unit == "F":
        c = (temp - 32) * 5/9
        k = c + 273.15
        print(f"{temp}°F = {c:.2f}°C = {k:.2f}K")

    elif unit == "K":
        c = temp - 273.15
        f = (c * 9/5) + 32
        print(f"{temp}K = {c:.2f}°C = {f:.2f}°F")

    else:
        print("Invalid unit! Please use C, F, or K.")


# ---- User Input ----
try:
    temp = float(input("Enter temperature value: "))
    unit = input("Enter unit (C/F/K): ")

    convert_temperature(temp, unit)

except ValueError:
    print("Please enter a valid numeric temperature.")