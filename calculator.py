def add(a, b):
    """
    Adds two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtracts two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiplies two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divides two numbers.
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
    
    Returns:
        Quotient of a and b
    
    Raises:
        ValueError: If divisor is zero
    """
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed!")
    return a / b


def modulo(a, b):
    """
    Finds the remainder of division.
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
    
    Returns:
        Remainder of a divided by b
    
    Raises:
        ValueError: If divisor is zero
    """
    if b == 0:
        raise ValueError("Error: Modulo by zero is not allowed!")
    return a % b


def calculate(num1, num2, operator):
    """
    Performs calculation based on operator.
    
    Args:
        num1: First number
        num2: Second number
        operator: Operation to perform (+, -, *, /, %)
    
    Returns:
        Result of the operation
    
    Raises:
        ValueError: If operator is invalid or division by zero
    """
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    elif operator == '%':
        return modulo(num1, num2)
    else:
        raise ValueError("Invalid operator! Use +, -, *, /, or %")


def calculator_interactive():
    """
    Interactive calculator program.
    Allows user to perform multiple calculations.
    """
    print("=" * 60)
    print("BASIC CALCULATOR PROGRAM")
    print("=" * 60)
    print()
    print("Supported operations:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    print("  % : Modulo (Remainder)")
    print()
    
    while True:
        try:
            print("-" * 60)
            print()
            
            # Get first number
            num1_input = input("Enter first number: ").strip()
            if num1_input.lower() == 'exit':
                print("Thank you for using Calculator Program!")
                break
            
            num1 = float(num1_input)
            
            # Get operator
            operator = input("Enter operator (+, -, *, /, %): ").strip()
            
            if operator.lower() == 'exit':
                print("Thank you for using Calculator Program!")
                break
            
            # Get second number
            num2_input = input("Enter second number: ").strip()
            if num2_input.lower() == 'exit':
                print("Thank you for using Calculator Program!")
                break
            
            num2 = float(num2_input)
            
            print()
            
            # Calculate result
            result = calculate(num1, num2, operator)
            
            # Display result
            print("=" * 60)
            print("CALCULATION RESULT:")
            print("=" * 60)
            print(num1, operator, num2, "=", round(result, 2))
            print("=" * 60)
            print()
            
            # Ask if user wants to continue
            continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                print("Thank you for using Calculator Program!")
                break
            
            print()
        
        except ValueError as e:
            print()
            print("Error:", str(e))
            print("Please enter valid numbers and a valid operator.")
            print()
        
        except Exception as e:
            print()
            print("An unexpected error occurred:", str(e))
            print()


# Test cases for verification
if __name__ == "__main__":
    # Run the interactive program
    calculator_interactive()
    
    # Or test with specific examples:
    """
    print("TEST CASES:")
    print()
    
    test_cases = [
        (10, 5, '+'),
        (10, 5, '-'),
        (10, 5, '*'),
        (10, 5, '/'),
        (10, 3, '%'),
        (7.5, 2.5, '+'),
        (20, 4, '/'),
    ]
    
    for num1, num2, op in test_cases:
        try:
            result = calculate(num1, num2, op)
            print(f"{num1} {op} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
    """