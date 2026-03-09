def celsius_to_fahrenheit(celsius):
    """
    Converts temperature from Celsius to Fahrenheit.
    
    Args:
        celsius: Temperature in Celsius
    
    Returns:
        Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Converts temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit: Temperature in Fahrenheit
    
    Returns:
        Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9


def temperature_converter():
    """
    Interactive temperature conversion program.
    Allows user to convert between Celsius and Fahrenheit.
    """
    print("=" * 60)
    print("TEMPERATURE CONVERSION PROGRAM")
    print("=" * 60)
    print()
    
    while True:
        print("Choose conversion option:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")
        print()
        
        choice = input("Enter your choice (1/2/3): ").strip()
        print()
        
        if choice == '3':
            print("Thank you for using Temperature Conversion Program!")
            break
        
        elif choice == '1':
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print()
                print("-" * 60)
                print(celsius, "°C =", round(fahrenheit, 2), "°F")
                print("-" * 60)
                print()
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                print()
        
        elif choice == '2':
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print()
                print("-" * 60)
                print(fahrenheit, "°F =", round(celsius, 2), "°C")
                print("-" * 60)
                print()
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                print()
        
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
            print()


# Test cases for verification
if __name__ == "__main__":
    # Uncomment the following line to run the interactive program
    temperature_converter()
    
    # Or run test cases without user input:
    """
    print("TEST CASES:")
    print()
    print("Celsius to Fahrenheit conversions:")
    print("0°C =", celsius_to_fahrenheit(0), "°F")
    print("100°C =", celsius_to_fahrenheit(100), "°F")
    print("37°C =", celsius_to_fahrenheit(37), "°F")
    print()
    print("Fahrenheit to Celsius conversions:")
    print("32°F =", fahrenheit_to_celsius(32), "°C")
    print("212°F =", fahrenheit_to_celsius(212), "°C")
    print("98.6°F =", fahrenheit_to_celsius(98.6), "°C")
    """