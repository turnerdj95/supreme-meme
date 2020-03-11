"""
Author: Evan Gibson, Derek Turner
Purpose: Array-based connect four gameeplay without GUI
"""

# Impport statments

import Board_Setup
import numpy as np

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



