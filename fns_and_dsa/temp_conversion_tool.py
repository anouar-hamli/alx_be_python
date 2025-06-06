# Global conversion factors - exactly as specified
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit"""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


def main():
    print("Temperature Conversion Tool")
    print("--------------------------")

    # Get temperature input with validation
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Get unit input with validation
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    while unit not in ('C', 'F'):
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    # Perform conversion and display result
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    else:
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")


if __name__ == "__main__":
    main()