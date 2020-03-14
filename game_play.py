"""
Author: Evan Gibson, Derek Turner
Purpose: Array-based connect four gameeplay without GUI
"""

# Impport statments

import Board_Setup
import rules
import numpy as np
import os

welcome_message = "Welcome to ConnectFour for your terminal window!" +\
                  "\n"  +\
                  "WARNING: This version of the game will clear your command prompt" +\
                  "\n" +\
                  "Before proceeding, please be sure to copy any text from your prompt. Cheers!"

class ConnectFour:
    """Scehma for game data storage and master organization"""
    def __init__(self, rows, columns):

        # Static conditional data
        self.rows = rows
        self.columns = columns

        # Dyanmic data

        # Holds last player coordinates for use in rule check
        self.player_1_last_move = None
        self.player_2_last_move = None


        # Flexible gameplay objects
        self.act_board = Board_Setup.Board(self.rows, self.columns)


def main():
    print(welcome_message)

    # Constrain parameters to int
    y_ = int(input("Enter the number of columns for your board:"))
    x_ = int(input("Enter the number of rows for your board:"))

    # Function to clear console
    clear = lambda: os.system('cls')

    # Game completion indicator
    game_win = False

    # Instantiate game object
    game_board = ConnectFour(x_, y_)



    # Game requires win condition before the maximum number of spaces are filled
    for t in range((y_*x_)+1):
        print("Turn: " + str(t))
        print("Current Turn: ")

        # Player 1 moves first
        if t%2 == 0:
            player = game_board.act_board.p1

        else:
            player = game_board.act_board.p2

        # Player initiates action

        print(game_board.act_board.board)
        print("Player " + str(player) + "'s turn.")
        move = int(input("Please enter a column to place your piece (columns are ordered from left to right):"))

        if player == game_board.act_board.p1:
            game_board.act_board.player_one(move)
            # Check win condition post player action
            temp_checker = rules.diaglysis(game_board.act_board.board,
                                           game_board.act_board.p1,
                                           game_board.act_board.last_play)
        else:
            game_board.act_board.player_two(move)
            temp_checker = rules.diaglysis(game_board.act_board.board,
                                           game_board.act_board.p2,
                                           game_board.act_board.last_play)

        # Check every direction for the last play
        wins = []
        wins.append(temp_checker.down_left())
        wins.append(temp_checker.down_right())
        wins.append(temp_checker.up_left())
        wins.append(temp_checker.up_right())
        wins.append(temp_checker.just_down())
        wins.append(temp_checker.just_left())
        wins.append(temp_checker.just_right())

        if any(wins):
            game_win = True
            break








if __name__ == "__main__":
    main()

