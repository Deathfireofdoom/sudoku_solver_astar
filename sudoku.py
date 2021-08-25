import numpy as np
from collections import Counter
from contextlib import suppress
from time import sleep
import os

from boards import BOARD1, BOARD2

class SudokoGame(object):
    def __init__(self, board=None):
        super().__init__()
        self.org_board = board
        self._init_board()

    def _init_board(self):
        if self.org_board == None: # This is for testing
            #self.org_board = np.zeros(9*9)
            self.org_board = BOARD1
        self.board = np.array(self.org_board).reshape(9, 9)
        print(self.board)


    def check_board(self):
        if self.check_column() and self.check_row() and self.check_sub_grid():
            return True
        else:
            return False


    def check_sub_grid(self):
        for i in range(3):
            for k in range(3):
                sub_grid = self.board[k*3:k*3+3,i*3:i*3+3].reshape(9)
                if not self.duplicates(part_of_board=sub_grid):
                    return False
        return True


    def check_row(self):
        for row in range(9):
            if not self.duplicates(part_of_board=self.board[row]):
                return False
        return True

            
    def check_column(self):
        for column in range(9):
            if not self.duplicates(part_of_board=self.board[:,column]):
                return False
        return True


    def duplicates(self, part_of_board):
        dup = [cell for cell, count in Counter(part_of_board).items() if count > 1]
        with suppress(ValueError):
            dup.remove(0)
        if len(dup) != 0:
            return False
        return True


    def __repr__(self):
        #clear = lambda: os.system('cls')
        #clear()

        print('')
        print('')
        print('')
        print('')
        print('')
        for row_n, row in enumerate(self.board):
            if not (row_n)%3:
                print('-'*(9*3+4))
            for cell_n, cell in enumerate(row):
                if not cell_n%3:
                    print('|', end='')
                print(f" {cell} ", end='')
            print('|')
        print('-'*(9*3+4))
        
        return ''

if __name__ == '__main__':
    sudokogame = SudokoGame()
    print(sudokogame.check_row())
    print(sudokogame.check_column())
    print(sudokogame.check_sub_grid())
    print(sudokogame.check_board())
