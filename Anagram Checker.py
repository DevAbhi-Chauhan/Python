# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths of the two strings are equal
    if len(str1) != len(str2):
        return False

    # Create dictionaries to store character frequency in both strings
    char_count1 = {}
    char_count2 = {}

    # Count characters in the first string
    for char in str1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    # Count characters in the second string
    for char in str2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    # Compare the character frequencies in both dictionaries
    return char_count1 == char_count2

# Input two strings from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check if the strings are anagrams and print the result
if are_anagrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")


# In this program:

# 1. We define a function are_anagrams that takes two strings as input and returns True if they are anagrams and False otherwise.

# 2. We remove spaces and convert both strings to lowercase to make the comparison case-insensitive.

# 3. We check if the lengths of the two strings are equal. If they have different lengths, they cannot be anagrams.

# 4. We create dictionaries (char_count1 and char_count2) to store the character frequencies of both strings.

# 5. We count the character frequencies in each string by iterating through the characters and updating the dictionaries.

# 6. Finally, we compare the character frequencies in both dictionaries. If they are the same, the strings are anagrams; otherwise, they are not.