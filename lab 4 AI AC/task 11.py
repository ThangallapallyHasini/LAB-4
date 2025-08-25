import re

def is_valid_indian_mobile(number):
    """
    Validates if the given number is a valid Indian mobile number.
    The number should start with 6, 7, 8, or 9 and be exactly 10 digits long.
    """
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, number))

# Examples
examples = [
    "9876543210",  # Valid
    
]

for num in examples:
    print(f"{num}: {'Valid' if is_valid_indian_mobile(num) else 'Invalid'}")