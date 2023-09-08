# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


#In this program:

# 1. We use the input function to get a number as input from the user and convert it to an integer using int().

# 2. We use the modulo operator % to check if the number is divisible by 2. If the remainder is 0, the number is even; otherwise, it's odd.

# 3. Depending on the result of the if condition, we print whether the number is even or odd.