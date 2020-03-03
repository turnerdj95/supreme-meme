import numpy as np

class Board:
    def __init__(self, rows, columns):
        self.rows = int(rows)
        self.columns = int(columns)
        self.board = np.zeros((self.rows, self.columns), dtype=int)
        self.player1 = 1
        self.player2 = -1

    def player_one(self, col_select):
        col = self.board[:, col_select]
        counter = self.rows - 1
        while col[0] != 0:
            col = self.board[:, int(input("That column is full.  Please select a different column: "))]
        while col[counter] != 0:
            counter -= 1
        self.board[counter, col_select] = self.player1

    def player_two(self, col_select):
        col = self.board[:, col_select]
        counter = self.rows - 1
        while col[0] != 0:
            col = int(input("That column is full.  Please select a different column: "))
        while col[counter] != 0:
            counter -= 1
        self.board[counter, col_select] = self.player2