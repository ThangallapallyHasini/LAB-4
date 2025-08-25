def factorial_one_shot(n):
    if n == 0:
        return "no negative number"
    elif n == 1:
        return 0
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

# Example inputs and outputs
print(factorial_one_shot(0))  # Output: no negative number
print(factorial_one_shot(1))  # Output: 0
print(factorial_one_shot(5))  # Output: 120