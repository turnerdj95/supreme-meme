"""
Author: Evan Gibson, Derek Turner
Purpose: Array-based connect four gameeplay without GUI
"""

# Impport statments

import Board_Setup
import rules
import numpy as np

welcome_message = "Welcome to ConnectFour for your terminal window!" +\
                  "\n"  +\
                  "WARNING: This version of the game will clear your command prompt" +\
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
        self.board = Board_Setup.Board(self.rows, self.columns)


def main():
    print(welcome_message)
    y_ = input("Enter the number of columns for your board:")
    x_ = input("Enter the number of rows for your board:")


