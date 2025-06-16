# Create a funcntion
def factorial(n):
    result = 1  # Start with 1 (* by 0 gives 0)
    for i in range(1, n + 1): # Loop from 1 to n
        result *= i  # Multiply result by the current number i
    return result # Return the final factorial value

# Example usage:
num = int(input("Enter a number to find its factorial: "))
print("Factorial of", num, "is", factorial(num))
