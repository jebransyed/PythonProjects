#!/usr/bin/env python3
"""
Tic Tac Toe Game - A command-line Tic Tac Toe game against the computer
"""

import random
import sys


def display_board(board):
    """Display the current state of the game board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def display_position_guide():
    """Display the position guide for the board"""
    print("\nPosition guide:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()


def check_winner(board, player):
    """Check if the specified player has won"""
    # All possible winning combinations
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal top-left to bottom-right
        [2, 4, 6]   # Diagonal top-right to bottom-left
    ]
    
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False


def check_draw(board):
    """Check if the game is a draw (board is full with no winner)"""
    return all(pos in ['X', 'O'] for pos in board)


def get_available_positions(board):
    """Return a list of available positions on the board"""
    return [i for i in range(9) if board[i] not in ['X', 'O']]


def get_player_move(board):
    """Get a valid move from the player"""
    available = get_available_positions(board)
    
    while True:
        try:
            move = input("Enter your move (1-9): ").strip()
            
            if not move.isdigit():
                print("Please enter a valid number between 1 and 9.")
                continue
            
            move = int(move)
            
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue
            
            position = move - 1  # Convert to 0-indexed
            
            if position not in available:
                print("That position is already taken. Choose another.")
                continue
            
            return position
        
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            sys.exit(0)


def get_computer_move(board):
    """Get the computer's move using simple AI logic"""
    available = get_available_positions(board)
    
    if not available:
        return None
    
    # Strategy 1: Check if computer can win in next move
    for pos in available:
        board[pos] = 'O'
        if check_winner(board, 'O'):
            board[pos] = str(pos + 1)  # Reset before returning
            return pos
        board[pos] = str(pos + 1)  # Reset
    
    # Strategy 2: Block player from winning
    for pos in available:
        board[pos] = 'X'
        if check_winner(board, 'X'):
            board[pos] = str(pos + 1)  # Reset before returning
            return pos
        board[pos] = str(pos + 1)  # Reset
    
    # Strategy 3: Take center if available
    if 4 in available:
        return 4
    
    # Strategy 4: Take a corner if available
    corners = [0, 2, 6, 8]
    available_corners = [c for c in corners if c in available]
    if available_corners:
        return random.choice(available_corners)
    
    # Strategy 5: Take any remaining position
    return random.choice(available)


def play_game():
    """Main game loop for a single round of Tic Tac Toe"""
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    print("\n" + "="*50)
    print("Welcome to Tic Tac Toe!")
    print("="*50)
    print("\nYou are X, and the computer is O.")
    display_position_guide()
    
    while True:
        # Display current board
        display_board(board)
        
        # Player's turn (X)
        print("Your turn!")
        player_move = get_player_move(board)
        board[player_move] = 'X'
        
        # Check if player won
        if check_winner(board, 'X'):
            display_board(board)
            print("="*50)
            print("🎉 Congratulations! You win!")
            print("="*50)
            return True
        
        # Check for draw
        if check_draw(board):
            display_board(board)
            print("="*50)
            print("🤝 It's a draw! Well played!")
            print("="*50)
            return None
        
        # Computer's turn (O)
        print("Computer's turn...")
        computer_move = get_computer_move(board)
        board[computer_move] = 'O'
        print(f"Computer chose position {computer_move + 1}")
        
        # Check if computer won
        if check_winner(board, 'O'):
            display_board(board)
            print("="*50)
            print("💻 Computer wins! Better luck next time!")
            print("="*50)
            return False
        
        # Check for draw
        if check_draw(board):
            display_board(board)
            print("="*50)
            print("🤝 It's a draw! Well played!")
            print("="*50)
            return None


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
    draws = 0
    
    try:
        while True:
            result = play_game()
            
            if result is True:
                wins += 1
            elif result is False:
                losses += 1
            else:
                draws += 1
            
            print(f"\nYour score - Wins: {wins}, Losses: {losses}, Draws: {draws}")
            
            if not play_again():
                print("\nThanks for playing! Goodbye!")
                break
    
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)


if __name__ == "__main__":
    main()
