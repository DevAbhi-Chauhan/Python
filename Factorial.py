# Input a number from the user
num = int(input("Enter a number: "))

# Initialize the factorial to 1
factorial = 1

# Calculate the factorial
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i

    print(f"The factorial of {num} is {factorial}")

# In this program:

# 1. We use the input function to get a number as input from the user and convert it to an integer using int().

# 2. We initialize the factorial variable to 1 because the factorial of 0 and 1 is 1.

# 3. We use a for loop to calculate the factorial of the given number. 
# 4. The loop runs from 1 to num, and in each iteration, we multiply factorial by the current value of i.

# 5. Depending on the value of num, we print either the factorial or a message indicating that factorial is not defined for negative numbers or that the factorial of 0 is 1.