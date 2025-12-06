#!/usr/bin/env python3
"""
Rock, Paper, Scissors Game
A simple command-line game where users play Rock, Paper, Scissors against the computer.
"""

import random
import sys


def get_computer_choice():
    """Randomly select the computer's choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def get_user_choice():
    """Get and validate the user's choice."""
    while True:
        user_input = input("\nEnter your choice (rock/paper/scissors): ").strip().lower()
        
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        elif user_input in ['r', 'p', 's']:
            # Accept shorthand inputs
            mapping = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
            return mapping[user_input]
        else:
            print("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")


def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on Rock, Paper, Scissors rules.
    Returns: 'win', 'lose', or 'tie'
    """
    if user_choice == computer_choice:
        return 'tie'
    
    winning_combinations = {
        'rock': 'scissors',      # Rock beats Scissors
        'scissors': 'paper',     # Scissors beats Paper
        'paper': 'rock'          # Paper beats Rock
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return 'win'
    else:
        return 'lose'


def display_result(user_choice, computer_choice, result):
    """Display the choices and game result."""
    print(f"\nYou chose: {user_choice.upper()}")
    print(f"Computer chose: {computer_choice.upper()}")
    print("-" * 40)
    
    if result == 'win':
        print("🎉 YOU WIN! 🎉")
    elif result == 'lose':
        print("😔 YOU LOSE! 😔")
    else:
        print("🤝 IT'S A TIE! 🤝")


def play_again():
    """Ask if the user wants to play another round."""
    while True:
        response = input("\nDo you want to play again? (yes/no): ").strip().lower()
        
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")


def display_welcome():
    """Display welcome message and game rules."""
    print("=" * 50)
    print("  WELCOME TO ROCK, PAPER, SCISSORS!".center(50))
    print("=" * 50)
    print("\nGame Rules:")
    print("  • Rock beats Scissors")
    print("  • Scissors beats Paper")
    print("  • Paper beats Rock")
    print("\nYou can type 'rock', 'paper', or 'scissors'")
    print("Or use shortcuts: 'r', 'p', or 's'")
    print("=" * 50)


def main():
    """Main game loop."""
    display_welcome()
    
    wins = 0
    losses = 0
    ties = 0
    
    try:
        while True:
            # Get choices
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            
            # Determine winner
            result = determine_winner(user_choice, computer_choice)
            
            # Update statistics
            if result == 'win':
                wins += 1
            elif result == 'lose':
                losses += 1
            else:
                ties += 1
            
            # Display result
            display_result(user_choice, computer_choice, result)
            
            # Display statistics
            print(f"\nScore - Wins: {wins} | Losses: {losses} | Ties: {ties}")
            
            # Ask if user wants to continue
            if not play_again():
                break
        
        # Display final statistics
        print("\n" + "=" * 50)
        print("  GAME OVER - FINAL STATISTICS".center(50))
        print("=" * 50)
        print(f"Total Rounds Played: {wins + losses + ties}")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Ties: {ties}")
        
        if wins + losses > 0:
            win_percentage = (wins / (wins + losses)) * 100
            print(f"Win Rate: {win_percentage:.1f}%")
        
        print("\nThanks for playing! Goodbye! 👋")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
