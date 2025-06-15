def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
    except ZeroDivisionError:

        return "Error: Cannot divide by zero."
    except ValueError:

        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {result}"
