# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is prime and print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# In this program:

# 1. We define a function is_prime that takes an integer number as an argument and returns True if it's prime and False otherwise.

# 2. We handle some special cases: numbers less than or equal to 1 are not prime, and numbers less than or equal to 3 are prime.

# 3. We use a loop to check for factors of the number. We start with i = 5 and then increment i by 6 in each iteration (taking advantage of the fact that prime numbers are often in the form of 6k ± 1). We only need to check factors up to the square root of the number to determine primality efficiently.

# 4. Finally, we take user input for the number to be checked and call the is_prime function to check if it's prime or not, and print the result.