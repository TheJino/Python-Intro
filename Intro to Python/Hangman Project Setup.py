# Hangman Game - Fill in the Blanks

# Import necessary libraries
# Instructions: Import the random library to select a random word from a list.
import random

# 1. Function to select a random word
def choose_word():
    """
    Selects and returns a random word from a list of words.
    Instructions:
    - Create a list of words that the player might guess.
    - Use the `random.choice()` function to select a word randomly from this list.
    - Return the selected word.
    """
    # words = ["python", "java", "kotlin", "javascript"]
    # return random.choice(words)
    pass  # Remove this line after adding your code

# 2. Function to display the current state of the word
def display_word(word, guessed_letters):
    """
    Displays the current state of the word, with guessed letters revealed and unguessed letters as underscores.
    Instructions:
    - Initialize an empty string to build the displayed word.
    - Loop through each letter in the word.
    - If the letter has been guessed (i.e., it's in guessed_letters), add it to the display string.
    - If not, add an underscore (_) to the display string.
    - Return the display string showing the current guessed state of the word.
    """
    pass  # Remove this line after adding your code

# 3. Function to check if the player has won
def check_win(word, guessed_letters):
    """
    Checks if the player has won by guessing all letters in the word.
    Instructions:
    - Loop through each letter in the word.
    - If any letter in the word has not been guessed, return False.
    - If all letters have been guessed, return True.
    """
    pass  # Remove this line after adding your code

# 4. Function to process a player's guess
def process_guess(guess, word, guessed_letters, wrong_guesses):
    """
    Processes the player's guess: updates guessed letters and tracks wrong guesses.
    Instructions:
    - Check if the guessed letter is in the word.
    - If it is, add the letter to guessed_letters and return True.
    - If it is not, add the letter to wrong_guesses and return False.
    """
    pass  # Remove this line after adding your code

# 5. Main game loop
def play_hangman():
    """
    The main function to play the Hangman game.
    Instructions:
    - Call choose_word() to get the word to guess.
    - Initialize guessed_letters as an empty list.
    - Initialize wrong_guesses as an empty list.
    - Set the maximum number of allowed wrong guesses (e.g., 6).
    - Use a while loop to keep the game running until the player wins or loses.
    - Within the loop:
        - Display the current state of the word using display_word().
        - Get a letter guess from the player.
        - Check if the letter has already been guessed (either correct or wrong).
        - Process the guess using process_guess().
        - Check if the player has won using check_win().
        - If the player has won, print a congratulatory message and break the loop.
        - If the player has used all attempts, print a game-over message and break the loop.
    """
    pass  # Remove this line after adding your code

# 6. Start the game
# Instructions: Call the `play_hangman` function to start the game.
play_hangman()
