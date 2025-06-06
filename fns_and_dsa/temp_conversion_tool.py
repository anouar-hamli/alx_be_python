# ✅ Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# ✅ Convert Fahrenheit to Celsius using global variable
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# ✅ Convert Celsius to Fahrenheit using global variable
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # ✅ User input for temperature
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        # ✅ Handle non-numeric input
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # ✅ User input for unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # ✅ Perform conversion based on unit
    if unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    elif unit == 'F':
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# ✅ Ensure main is only called when script is run directly
if __name__ == "__main__":
    main()
