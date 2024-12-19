def function_with_improved_error_handling(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Invalid input type: Operands must be numbers.")
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Division by zero")

# Example usage demonstrating the improved error handling
try:
    result1 = function_with_improved_error_handling(10, 2)  # Output: 5.0
    result2 = function_with_improved_error_handling(10, 0)  # Raises ZeroDivisionError
    result3 = function_with_improved_error_handling(10, "abc")  # Raises ValueError
    result4 = function_with_improved_error_handling([1,2,3], 2) # Raises ValueError
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
