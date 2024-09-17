# Implementation of knights tour
import copy


def print_at(row, col, text):
    print(f"\033[{row};{col}H{text}")


def cls():
    print("\033[2J\033[H", end='')


def draw_board(current_board: list):
    i = 0
    for row in current_board:
        line = ''
        for value in row:
            line += '**' if value == 1 else '..'
        print_at(i, 0, line)
        i += 1


class vertex:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class knight_moves:
    def __init__(self):
        self.up_left = -1
        self.up_right = -1
        self.down_left = -1
        self.down_right = -1
        self.left_up = -1
        self.left_down = -1
        self.right_up = -1
        self.right_down = -1

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
        self.up_left = self.calculate(x-1, y+2, current_board) if self.inrange(x-1) and self.inrange(y+2) and current_board[x-1][y+2] == 0 else -1
        self.up_right = self.calculate(x+1, y+2, current_board) if self.inrange(x+1) and self.inrange(y+2) and current_board[x+1][y+2] == 0 else -1
        self.down_left = self.calculate(x-1, y-2, current_board) if self.inrange(x-1) and self.inrange(y-2) and current_board[x-1][y-2] == 0 else -1
        self.down_right = self.calculate(x+1, y-2, current_board) if self.inrange(x+1) and self.inrange(y-2) and current_board[x+1][y-2] == 0 else -1
        self.left_up = self.calculate(x-2, y+1, current_board) if self.inrange(x-2) and self.inrange(y+1) and current_board[x-2][y-1] == 0 else -1
        self.left_down = self.calculate(x-2, y-1, current_board) if self.inrange(x-2) and self.inrange(y-1) and current_board[x-2][y-1] == 0 else -1
        self.right_up = self.calculate(x+2, y+1, current_board) if self.inrange(x+2) and self.inrange(y+1) and current_board[x+2][y+1] == 0 else -1
        self.right_down = self.calculate(x+2, y-1, current_board) if self.inrange(x+2) and self.inrange(y-1) and current_board[x+2][y-1] == 0 else -1

    def getmoves(self, is_first: bool) -> list[vertex]:
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

        valid_moves = [move for move in moves if move[0] > -1]
        if not valid_moves:
            return [vertex(0, 0)]  # No valid moves available

        valid_moves.sort(key=lambda x: x[0])
        min_onward_moves = valid_moves[0][0]
        best_moves = [move for cost, move in valid_moves] if is_first else [move for cost, move in valid_moves if cost == min_onward_moves]

        return best_moves


def walk_board(x: int, y: int, current_board: list, path: list[vertex], winning_paths: list):
    new_board = copy.deepcopy(current_board)
    new_path = copy.deepcopy(path)
    new_board[x][y] = 1
    available_moves = knight_moves()
    available_moves.update(x, y, new_board)
    next_moves = available_moves.getmoves(len(path) == 1)

    # Exit condition
    if len(next_moves) == 1 and next_moves[0].x == 0 and next_moves[0].y == 0:
        if not any(0 in row for row in new_board):
            winning_paths.append(new_path)
        return

    # Search paths
    for chosen_move in next_moves:
        if chosen_move.x != 0 and chosen_move.y != 0:
            new_path.append(vertex(x + chosen_move.x, y + chosen_move.y))
            walk_board(x + chosen_move.x, y + chosen_move.y, new_board, new_path, winning_paths)


board = [[0 for x in range(8)] for y in range(8)]
knights_tour = [vertex(1, 0)]
winning_tours = []
cls()
walk_board(1, 0, board, knights_tour, winning_tours)

print(f'Found {len(winning_tours)} winning tours')
