from sudoko import SudokoGame
from time import sleep

class AstarSudokoSolver(object):
    def __init__(self, game):
        self.game = game
        self.solver()
    
    def solver(self):
        self.solve(0)

    def solve(self, current_step):
        if self.game.board[current_step//9, current_step%9] == 0:
            for i in range(9):
                self.game.board[current_step//9, current_step%9] = i + 1
                print(self.game)
                print(self.game.check_board())

                if self.game.check_board():
                    self.solve(current_step + 1)
            self.game.board[current_step//9, current_step%9] = 0
        else:
            self.solve(current_step + 1)

if __name__ == '__main__':
    game = SudokoGame()
    solver = AstarSudokoSolver(game)