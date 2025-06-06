# Global conversion factors - properly defined
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius"""
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Temperature must be a numeric value")
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit"""
    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperature must be a numeric value")
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def get_user_input():
    """Get and validate user input"""
    temp_input = input("Enter the temperature to convert: ")
    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if unit not in ('C', 'F'):
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    return temperature, unit


def main():
    print("Temperature Conversion Tool")
    print("--------------------------")

    try:
        temperature, unit = get_user_input()

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()