import numpy as np

class Board:
    def __init__(self,rows,columns):
        self.rows=int(rows)
        self.columns=int(columns)
        self.board = np.zeros((self.rows,self.columns),dtype='int8')
        self.last_play = None
        self.p1 = 1
        self.p2 = -1

    def player_one(self,col_select):
        while col_select > self.columns-1:
            col_select = int(input("Invalid column.  Please select a number between 0-{}: ".format(self.rows-1)))
        col = self.board[:,col_select]
        counter = self.rows-1
        while col[counter] != 0:
            counter -= 1
        self.board[counter,col_select] = self.p1
        self.last_play = [counter,col_select]

    def player_two(self,col_select):
        while col_select > self.columns-1:
            col_select = int(input("Invalid column.  Please select a number between 0-{}: ".format(self.rows-1)))
        col = self.board[:,col_select]
        counter = self.rows-1
        while col[counter] != 0:
            counter -= 1
        self.board[counter,col_select] = self.p2
        self.last_play = [counter, col_select]


def check_x(rows,columns):

    """Board condition setter"""
    board = Board(rows,columns)
    while 0 in board.board:
        try:
            move1 = np.random.randint(0,board.columns)
            while 0 not in board.board[:,move1]:
                move1 = np.random.randint(0,board.columns)
                if 0 not in board.board:
                    break
            board.player_one(move1)
            print(board.board,'\n')

            move2 = np.random.randint(0,board.columns)
            while 0 not in board.board[:,move2]:
                move2 = np.random.randint(0,board.columns)
                if 0 not in board.board:
                    break
            board.player_two(move2)
            print(board.board,'\n')
        except IndexError:
            continue

if __name__ == '__main__':
    check_x(20,20)
