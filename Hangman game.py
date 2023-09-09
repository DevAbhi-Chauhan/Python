import random

# List of words for the game
word_list = ["python", "hangman", "programming", "computer", "algorithm", "keyboard"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word with blanks
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to play the Hangman game
def play_hangman():
    # Choose a random word
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6  # You can customize the number of allowed attempts

    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print(display_word(secret_word, guessed_letters))

    while True:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        word_display = display_word(secret_word, guessed_letters)
        print(word_display)

        if word_display == secret_word:
            print("Congratulations! You've guessed the word.")
            break

        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The word was '{secret_word}'.")
            break

# Start the game
play_hangman()


# In this Hangman game:

# 1. We start by defining a list of words (word_list) that the game can choose from.

# 2. We have several functions:

## choose_word() selects a random word from the list.
## initialize_game() sets up the game state, including the chosen word, its length, guessed letters, and remaining attempts.
## display_game() displays the current state of the word with underscores for unguessed letters.
## The main game loop (hangman_game()) starts by initializing the game and displaying the initial state.

# 3. Inside the loop, the player is prompted to guess a letter, and their guess is processed accordingly. The game checks if the guessed letter is correct, updates the display, and keeps track of attempts.

# 4. The game continues until the player either correctly guesses the word or runs out of attempts.

# 5. You can customize the word_list with your own words and set the number of allowed attempts according to your preferences.