def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid operand type")
        return None

# Example usage demonstrating the uncommon error
result1 = function_with_uncommon_error(10, 2) # Expected output: 5.0
result2 = function_with_uncommon_error(10, 0) # Expected output: Error message, None
result3 = function_with_uncommon_error(10, "abc") # Expected output: Error message, None
result4 = function_with_uncommon_error([1,2,3], 2) #Expected output: Error message, None