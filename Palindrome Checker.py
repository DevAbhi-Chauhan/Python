# Input a string from the user
input_string = input("Enter a string: ")

# Remove spaces and convert to lowercase for case-insensitive comparison
cleaned_string = input_string.replace(" ", "").lower()

# Reverse the string
reversed_string = cleaned_string[::-1]

# Check if the original and reversed strings are the same
if cleaned_string == reversed_string:
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")


# In this program:

# 1. We use the input function to get a string as input from the user.

# 2. We remove spaces from the input string and convert it to lowercase using the replace and lower methods to make the comparison case-insensitive.

# 3. We use string slicing with [::-1] to reverse the cleaned string.

# 4. Finally, we check if the cleaned string is the same as its reversed version and print whether it's a palindrome or not.