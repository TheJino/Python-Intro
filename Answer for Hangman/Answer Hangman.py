import random

def get_display_word(word, guessed_letters):
    """
    Constructs the display string for the word with guessed letters and underscores.
    """
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter  # Show guessed letter
        else:
            display_word += "_"  # Replace unguessed letters with underscores
        display_word += " "  # Add space for readability
    return display_word.strip()

def play_hangman():
    """
    Main Hangman game logic.
    """
    # List of words for the game
    words = ["PYTHON", "JAVASCRIPT", "HANGMAN"]
    word = random.choice(words)  # Randomly choose a word from the list
    guessed_letters = []  # List to store guessed letters
    attempts = 6  # Number of attempts allowed

    # Game loop
    while attempts > 0:
        # Display the current state of the word
        display_word = get_display_word(word, guessed_letters)
        print(f"Word: {display_word}")

        # Get a letter guess from the player
        guess = input("Guess a letter: ").upper()

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue  # Skip to the next iteration

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            print("Correct!")
            # Check if the entire word has been guessed
            if "_" not in get_display_word(word, guessed_letters):
                print(f"Congratulations! You've guessed the word: {word}")
                break  # Exit the loop
        else:
            attempts -= 1  # Decrease attempts for incorrect guess
            print(f"Incorrect! Attempts remaining: {attempts}")

    # If the player runs out of attempts
    if attempts == 0:
        print(f"Game Over! The word was: {word}")

# Run the Hangman game
if __name__ == "__main__":
    print("Welcome to Hangman!")
    play_hangman()
