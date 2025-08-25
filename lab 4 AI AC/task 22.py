def factorial(n):
    """
    Computes the factorial of a non-negative integer n.
    Returns 1 if n is 0.
    Returns a message if n is negative.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage
num = 5
output = factorial(num)
print(f"Input: {num}")
print(f"Output: {output}")