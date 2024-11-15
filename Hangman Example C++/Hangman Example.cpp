#include <iostream>
#include <string>
#include <vector>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For seeding random number generator
#include <algorithm> // For std::find

using namespace std;

// Function to display the current state of the word with guessed letters and underscores
string getDisplayWord(const string& word, const vector<char>& guessedLetters) {
    string displayWord;
    for (char letter : word) {
        // Check if the letter has been guessed
        if (find(guessedLetters.begin(), guessedLetters.end(), letter) != guessedLetters.end()) {
            displayWord += letter; // Show the guessed letter
        } else {
            displayWord += '_'; // Replace unguessed letters with an underscore
        }
        displayWord += ' '; // Add space between letters for better readability
    }
    return displayWord;
}

// Main Hangman game function
void playHangman() {
    // List of words for the game
    vector<string> words = {"PYTHON", "JAVASCRIPT", "HANGMAN"};
    
    // Select a random word from the list
    srand(static_cast<unsigned>(time(0))); // Seed the random number generator
    string word = words[rand() % words.size()];

    vector<char> guessedLetters; // Store guessed letters
    int attempts = 6; // Number of attempts allowed

    // Game loop
    while (attempts > 0) {
        // Display the current state of the word
        string displayWord = getDisplayWord(word, guessedLetters);
        cout << "Word: " << displayWord << "\n";

        // Ask the user for a letter
        char guess;
        cout << "Guess a letter: ";
        cin >> guess;
        guess = toupper(guess); // Convert input to uppercase for consistency

        // Check if the letter was already guessed
        if (find(guessedLetters.begin(), guessedLetters.end(), guess) != guessedLetters.end()) {
            cout << "You already guessed that letter.\n";
            continue; // Skip to the next iteration
        }

        // Add the guess to the list of guessed letters
        guessedLetters.push_back(guess);

        // Check if the guess is correct
        if (word.find(guess) != string::npos) {
            cout << "Correct!\n";

            // Check if the player has guessed the entire word
            if (getDisplayWord(word, guessedLetters).find('_') == string::npos) {
                cout << "Congratulations! You've guessed the word: " << word << "\n";
                break; // Exit the loop
            }
        } else {
            attempts--; // Decrease attempts for incorrect guess
            cout << "Incorrect! Attempts remaining: " << attempts << "\n";
        }
    }

    // If the player runs out of attempts
    if (attempts == 0) {
        cout << "Game Over! The word was: " << word << "\n";
    }
}

// Main function
int main() {
    cout << "Welcome to Hangman!\n";
    playHangman(); // Start the game
    return 0;
}
