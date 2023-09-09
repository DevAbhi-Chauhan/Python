import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize variables
attempts = 0
max_attempts = 10

print("Welcome to the Number Guessing Game!")
print(f"Try to guess the secret number between 1 and 100. You have {max_attempts} attempts.")

# Main game loop
while attempts < max_attempts:
    try:
        # Input a guess from the player
        guess = int(input("Enter your guess: "))

        # Increment the number of attempts
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# If the player couldn't guess the number in the allowed attempts
if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

# In this number guessing game:

# 1. We import the random module to generate a random number.

# 2. The computer generates a random number between 1 and 100 and stores it as the secret_number.

# 3. We set the maximum number of attempts the player has to guess the number (max_attempts).

# 4. The game starts with a welcome message and instructions.

# 5. The main game loop continues until the player guesses the correct number or runs out of attempts.

# 6. In each iteration of the loop, the player is prompted to enter a guess.

# 7. The player's guess is compared to the secret_number, and the player is given feedback whether the guess is too high or too low.

# 8. If the player guesses the correct number, the game ends with a congratulatory message.

# 9. If the player runs out of attempts, the game reveals the secret number.

# 10. The game handles invalid inputs by catching ValueError exceptions when the player enters something that is not a number.
