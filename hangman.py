#!/usr/bin/env python3
"""
Hangman Game - A command-line word guessing game
"""

import random
import sys


# Predefined word list
WORD_LIST = [
    "python", "programming", "computer", "algorithm", "function",
    "variable", "database", "network", "internet", "software",
    "hardware", "keyboard", "monitor", "development", "debugging",
    "compiler", "interface", "terminal", "command", "execute",
    "library", "framework", "application", "security", "encryption"
]

MAX_INCORRECT_GUESSES = 6


def display_hangman(incorrect_count):
    """Display hangman ASCII art based on incorrect guess count"""
    stages = [
        """
           --------
           |      |
           |      
           |     
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        --------
        """
    ]
    
    if 0 <= incorrect_count < len(stages):
        print(stages[incorrect_count])


def display_word_state(word, guessed_letters):
    """Display the current state of the word with underscores for unguessed letters"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_valid_guess(guessed_letters):
    """Get a valid letter guess from the player"""
    while True:
        guess = input("\nGuess a letter: ").lower().strip()
        
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        if not guess.isalpha():
            print("Please enter a valid letter (a-z).")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        
        return guess


def play_game():
    """Main game loop for a single round of hangman"""
    word = random.choice(WORD_LIST)
    guessed_letters = set()
    incorrect_guesses = set()
    incorrect_count = 0
    
    print("\n" + "="*50)
    print("Welcome to Hangman!")
    print("="*50)
    print(f"\nThe word has {len(word)} letters.")
    
    while incorrect_count < MAX_INCORRECT_GUESSES:
        # Display current game state
        display_hangman(incorrect_count)
        print(f"\nWord: {display_word_state(word, guessed_letters)}")
        
        if incorrect_guesses:
            print(f"Incorrect guesses ({incorrect_count}/{MAX_INCORRECT_GUESSES}): {', '.join(sorted(incorrect_guesses))}")
        else:
            print(f"Incorrect guesses: {incorrect_count}/{MAX_INCORRECT_GUESSES}")
        
        # Check if player has won
        if all(letter in guessed_letters for letter in word):
            print("\n" + "="*50)
            print(f"🎉 Congratulations! You won! The word was '{word}'")
            print("="*50)
            return True
        
        # Get player's guess
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word:
            print(f"✓ Good guess! '{guess}' is in the word.")
        else:
            print(f"✗ Sorry, '{guess}' is not in the word.")
            incorrect_guesses.add(guess)
            incorrect_count += 1
    
    # Player lost
    display_hangman(incorrect_count)
    print("\n" + "="*50)
    print(f"💀 Game Over! You ran out of guesses.")
    print(f"The word was '{word}'")
    print("="*50)
    return False


def play_again():
    """Ask player if they want to play again"""
    while True:
        response = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    """Main program entry point"""
    wins = 0
    losses = 0
    
    try:
        while True:
            if play_game():
                wins += 1
            else:
                losses += 1
            
            print(f"\nYour score - Wins: {wins}, Losses: {losses}")
            
            if not play_again():
                print("\nThanks for playing! Goodbye!")
                break
    
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)


if __name__ == "__main__":
    main()
