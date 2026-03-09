def reverse_string(s):
    """
    Reverses any input string.
    
    Args:
        s: The input string to reverse (can be any string).
    
    Returns:
        The reversed string.
    
    Example:
        reverse_string("hello")
        'olleh'
        reverse_string("hello.")
        '.olleh'
    """
    return s[::-1]


# Interactive program to reverse any string input
if __name__ == "__main__":
    print("=" * 50)
    print("STRING REVERSAL PROGRAM")
    print("=" * 50)
    print()
    
    while True:
        # Get user input
        user_input = input("Enter a string to reverse (or type 'exit' to quit): ")
        
        # Check if user wants to exit
        if user_input.lower() == 'exit':
            print("Thank you for using the String Reversal Program!")
            break
        
        # Reverse and display the string
        reversed_string = reverse_string(user_input)
        print("Original: '" + user_input + "'")
        print("Reversed: '" + reversed_string + "'")
        print("-" * 50)
        print()