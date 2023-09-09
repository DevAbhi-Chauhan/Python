# Function to reverse a string
def reverse_string(input_string):
    reversed_str = ""
    for char in input_string[::-1]:
        reversed_str += char
    return reversed_str

# Input a string from the user
input_string = input("Enter a string: ")

# Reverse the string and print the result
reversed_result = reverse_string(input_string)
print("Reversed string:", reversed_result)

# In this program:

# 1. We define a function reverse_string that takes an input string and returns its reverse.

# 2. Inside the function, we initialize an empty string reversed_str.

# 3. We use a for loop to iterate through the characters of the input string in reverse order (achieved by using [::-1]).

# 4. In each iteration, we append the current character to the reversed_str.

# 5. Finally, we take user input for the string to be reversed, call the reverse_string function to reverse it, and print the result.