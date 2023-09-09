# Function to count the number of words in a text file
def count_words(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return -1  # File not found
    except Exception as e:
        print(f"An error occurred: {e}")
        return -2  # Other error

# Input the filename from the user
filename = input("Enter the name of the text file: ")

# Call the count_words function and print the result
word_count = count_words(filename)

if word_count == -1:
    print(f"Error: The file '{filename}' was not found.")
elif word_count == -2:
    print("Error: An unknown error occurred.")
else:
    print(f"The number of words in '{filename}' is {word_count}.")


# In this program:

# 1. We define a function count_words that takes a filename as input.

# 2. Inside the function, we attempt to open the file specified by the filename in read mode using a with block. We read the contents of the file, split the text into words using the split() method (which splits on spaces by default), and return the count of words.

# 3. We handle potential exceptions such as FileNotFoundError (when the file doesn't exist) and other general exceptions.

# 4. We take user input for the filename of the text file they want to analyze.

# 5. We call the count_words function with the provided filename and display the word count or error messages as appropriate.