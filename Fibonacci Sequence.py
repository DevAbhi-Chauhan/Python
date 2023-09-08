# Function to generate the first N terms of the Fibonacci sequence
def generate_fibonacci(n):
    fibonacci_sequence = []
    
    if n <= 0:
        return fibonacci_sequence
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, n):
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)
        return fibonacci_sequence

# Input the number of terms (N)
N = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate and print the first N terms
result = generate_fibonacci(N)
print("Fibonacci Sequence:", result)


# In this program:

# 1. We define a function generate_fibonacci that takes an integer n as an argument and returns a list containing the first n terms of the Fibonacci sequence.

# 2. We handle special cases when n is 0, 1, or 2, returning appropriate lists to handle those cases efficiently.

# 3. For n greater than 2, we initialize the sequence with the first two terms [0, 1] and then use a for loop to calculate and append the next terms to the sequence.

# 4. Finally, we take user input for the value of N, call the generate_fibonacci function to generate the sequence, and print the result.4