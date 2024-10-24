# Recursive function to find Fibonacci number
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Function to generate Fibonacci sequence up to n terms
def generate_fibonacci_sequence(n):
    sequence = []
    for i in range(n):
        sequence.append(fibonacci_recursive(i))
    return sequence

# Get the number of terms from the user
n = int(input("Enter the number of terms: "))
print(generate_fibonacci_sequence(n))
