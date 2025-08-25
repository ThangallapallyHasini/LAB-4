def validate_indian_mobile(mobile_number):
    """
    Function to validate Indian mobile number
    Rules:
    1. Should start with 6, 7, 8, or 9
    2. Should have exactly 10 digits
    3. Should only contain digits
    
    Args:
        mobile_number (str): The mobile number to validate
        
    Returns:
        str: "Valid" if the number is valid, "Invalid" otherwise
    """
    
    # Remove any spaces or special characters
    mobile_number = str(mobile_number).strip()
    
    # Check if the number has exactly 10 digits
    if len(mobile_number) != 10:
        return "Invalid"
    
    # Check if all characters are digits
    if not mobile_number.isdigit():
        return "Invalid"
    
    # Check if the number starts with 6, 7, 8, or 9
    if mobile_number[0] not in ['6', '7', '8', '9']:
        return "Invalid"
    
    # If all conditions are met, the number is valid
    return "Valid"

def main():
    """
    Main function to demonstrate the mobile number validation
    """
    print("Indian Mobile Number Validator")
    print("=" * 30)
    
    while True:
        mobile_input = input("\nEnter mobile number (or 'quit' to exit): ")
        if mobile_input.lower() == 'quit':
            print("Goodbye!")
            break
        result = validate_indian_mobile(mobile_input)
        print(f"Result: {result}")
        if result == "Invalid":
            print("Reason: Number must start with 6, 7, 8, or 9 and have exactly 10 digits")
if __name__ == "__main__":
    # Test cases
    print("Testing the function with sample numbers:")
    print("-" * 40)
    
    test_numbers = [
        "9876543210",  # Valid - starts with 9
        "8765432109",  # Valid - starts with 8
        "7654321098",  # Valid - starts with 7
        "6543210987",  # Valid - starts with 6
        "1234567890",  # Invalid - starts with 1
        "987654321",   # Invalid - only 9 digits
        "98765432101", # Invalid - 11 digits
        "987654321a",  # Invalid - contains letter
        " 9876543210 ", # Valid - with spaces
        "9876543210.0" # Invalid - contains decimal
    ]
    
    for number in test_numbers:
        result = validate_indian_mobile(number)
        print(f"{number}: {result}")
    
    print("\n" + "=" * 40)
    
    # Run interactive mode
    main()