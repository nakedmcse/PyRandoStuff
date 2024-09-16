# Implementation of knights tour
import random

class vertex:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class knight_moves:
    def __init__(self):
        self.up_left = 0
        self.up_right = 0
        self.down_left = 0
        self.down_right = 0
        self.left_up = 0
        self.left_down = 0
        self.right_up = 0
        self.right_down = 0

    def inrange(self, val: int) -> bool:
        return 0 <= val <= 7

    def calculate(self, x: int, y: int, current_board: list) -> int:
        total = 0
        # ups
        total = total + (1 if self.inrange(x-1) and self.inrange(y+2) and current_board[x-1][y+2] == 0 else 0)
        total = total + (1 if self.inrange(x+1) and self.inrange(y+2) and current_board[x+1][y+2] == 0 else 0)
        # downs
        total = total + (1 if self.inrange(x-1) and self.inrange(y-2) and current_board[x-1][y-2] == 0 else 0)
        total = total + (1 if self.inrange(x+1) and self.inrange(y-2) and current_board[x+1][y-2] == 0 else 0)
        # lefts
        total = total + (1 if self.inrange(x-2) and self.inrange(y-1) and current_board[x-2][y-1] == 0 else 0)
        total = total + (1 if self.inrange(x-2) and self.inrange(y+1) and current_board[x-2][y+1] == 0 else 0)
        # rights
        total = total + (1 if self.inrange(x+2) and self.inrange(y-1) and current_board[x+2][y-1] == 0 else 0)
        total = total + (1 if self.inrange(x+2) and self.inrange(y+1) and current_board[x+2][y+1] == 0 else 0)
        return total

    def update(self, x: int, y: int, current_board: list):
        self.up_left = self.calculate(x-1, y+2, current_board) if self.inrange(x-1) and self.inrange(y+2) and current_board[x-1][y+2] == 0 else 0
        self.up_right = self.calculate(x+1, y+2, current_board) if self.inrange(x+1) and self.inrange(y+2) and current_board[x+1][y+2] == 0 else 0
        self.down_left = self.calculate(x-1, y-2, current_board) if self.inrange(x-1) and self.inrange(y-2) and current_board[x-1][y-2] == 0 else 0
        self.down_right = self.calculate(x+1, y-2, current_board) if self.inrange(x+1) and self.inrange(y-2) and current_board[x+1][y-2] == 0 else 0
        self.left_up = self.calculate(x-2, y+1, current_board) if self.inrange(x-2) and self.inrange(y+1) and current_board[x-2][y-1] == 0 else 0
        self.left_down = self.calculate(x-2, y-1, current_board) if self.inrange(x-2) and self.inrange(y-1) and current_board[x-2][y-1] == 0 else 0
        self.right_up = self.calculate(x+2, y+1, current_board) if self.inrange(x+2) and self.inrange(y+1) and current_board[x+2][y+1] == 0 else 0
        self.right_down = self.calculate(x+2, y-1, current_board) if self.inrange(x+2) and self.inrange(y-1) and current_board[x+2][y-1] == 0 else 0

    def getmove(self, x: int, y: int, current_board: list) -> vertex:
        moves = [
            (self.up_left, vertex(-1, 2)),
            (self.up_right, vertex(1, 2)),
            (self.down_left, vertex(-1, -2)),
            (self.down_right, vertex(1, -2)),
            (self.left_up, vertex(-2, 1)),
            (self.left_down, vertex(-2, -1)),
            (self.right_up, vertex(2, 1)),
            (self.right_down, vertex(2, -1))
        ]

        valid_moves = [move for move in moves if move[0] > 0]
        if not valid_moves:
            return vertex(0, 0)  # No valid moves available

        valid_moves.sort(key=lambda x: x[0])
        min_onward_moves = valid_moves[0][0]
        best_moves = [move for cost, move in valid_moves if cost == min_onward_moves]
        best_move = random.choice(best_moves)

        return best_move


def walk_board(x: int, y: int, current_board: list, path: list[vertex]):
    current_board[x][y] = 1
    available_moves = knight_moves()
    available_moves.update(x, y, current_board)
    chosen_move = available_moves.getmove(x, y, current_board)
    if chosen_move.x != 0 and chosen_move.y != 0:
        path.append(vertex(x + chosen_move.x, y + chosen_move.y))

    # exit conditions
    if chosen_move.x == 0 and chosen_move.y == 0:
        return

    # walk
    walk_board(x + chosen_move.x, y + chosen_move.y, current_board, path)

while True:
    board = [[0 for x in range(8)] for y in range(8)]
    knights_tour = [vertex(1, 0)]
    walk_board(1, 0, board, knights_tour)
    if not any(0 in row for row in board):
        break

for step in knights_tour:
    print(f'({step.x},{step.y})')
print(board)
