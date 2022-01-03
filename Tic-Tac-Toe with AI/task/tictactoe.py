import random


# definitions
def initial_grids(initial):
    positions = list(initial)
    grids = []
    for n in range(3):
        grids.append([])
        for m in range(3):
            grids[n].append(positions[m + 3 * n])
    return grids


# Analyze if there are 3 in a row
# def win_check(grids):
#     win_cells = [[grids[0][0], grids[0][1], grids[0][2]],
#                  [grids[1][0], grids[1][1], grids[1][2]],
#                  [grids[2][0], grids[2][1], grids[2][2]],
#                  [grids[0][0], grids[1][0], grids[2][0]],
#                  [grids[0][1], grids[1][1], grids[2][1]],
#                  [grids[0][2], grids[1][2], grids[2][2]],
#                  [grids[0][0], grids[1][1], grids[2][2]],
#                  [grids[0][2], grids[1][1], grids[2][0]]
#                  ]
#
#     if ['X', 'X', 'X'] in win_cells:
#         return "X wins"
#     elif ['O', 'O', 'O'] in win_cells:
#         return "O wins"
#     else:
#         return ""


def print_grids(grids):
    print('---------')
    print('| ' + ' '.join(grids[0]) + ' |')
    print('| ' + ' '.join(grids[1]) + ' |')
    print('| ' + ' '.join(grids[2]) + ' |')
    print('---------')


# check input coordinates format
def process_input():
    while True:
        user_in = input("Enter the coordinates: ")
        try:
            d = user_in.split()
            user_in_1 = int(d[0])
            user_in_2 = int(d[1])
        except ValueError:
            print("You should enter numbers!")
        except IndexError:
            print("You should enter numbers!")
        else:
            if user_in_1 > 3 or user_in_1 < 1 or user_in_2 > 3 or user_in_2 < 1:
                print("Coordinates should be from 1 to 3!")
            else:
                return [user_in_1 - 1, user_in_2 - 1]


# def check_blank_position(grids, co):
#     x = co[0]
#     y = co[1]
#     if grids[x - 1][y - 1] == "_":
#         return True
#     else:
#         return False


# def check_full(grids):
#     for x in range(3):
#         for y in range(3):
#             if grids[x][y] == "_":
#                 return False
#     return True


def check_part(grids):
    x_num = 0
    o_num = 0
    for x in range(3):
        for y in range(3):
            if grids[x][y] == "X":
                x_num += 1
            elif grids[x][y] == "O":
                o_num += 1
    if x_num == o_num:
        return "X"
    elif x_num > o_num:
        return "O"


# def make_move(grids, co, part):
#     x = co[0]
#     y = co[1]
#     if co in find_blank_positions(grids):
#         grids[x][y] = part
#     return grids


# def find_blank_positions(grids):
#     blank_positions = []
#     for x in range(3):
#         for y in range(3):
#             if grids[x][y] == "_":
#                 blank_positions.append([x, y])
#     return blank_positions


# def check_end(grids):
#     if win_check(grids):
#         return win_check(grids)
#     elif check_full(grids):
#         return "Draw"
#     else:
#         return ""


def menu():
    while True:
        user_in = input("Input command: ").split()
        if user_in[0] == "start":
            try:
                x = user_in[1]
                o = user_in[2]
            except IndexError:
                print("Bad parameters!")
            else:
                if x in ["easy", "user", "medium"] and o in ["easy", "user", "medium"]:
                    return [x, o]
                else:
                    print("Bad parameters!")
        elif user_in[0] == "exit":
            return None
        else:
            print("Bad parameters!")


class TicTacToe:
    grid = initial_grids("_" * 9)
    win_cells = []
    win_cells_position = []

    def __init__(self, user_part):
        self.user_part = user_part
        self.blank_positions = []
        self.coordinates = []
        self.opponent_part = self.opponent()

    def opponent(self):
        if self.user_part == "X":
            self.opponent_part = "O"
        else:
            self.opponent_part = "X"
        return self.opponent_part

    def build_win_cells(self):
        self.win_cells = [[self.grid[0][0], self.grid[0][1], self.grid[0][2]],
                          [self.grid[1][0], self.grid[1][1], self.grid[1][2]],
                          [self.grid[2][0], self.grid[2][1], self.grid[2][2]],
                          [self.grid[0][0], self.grid[1][0], self.grid[2][0]],
                          [self.grid[0][1], self.grid[1][1], self.grid[2][1]],
                          [self.grid[0][2], self.grid[1][2], self.grid[2][2]],
                          [self.grid[0][0], self.grid[1][1], self.grid[2][2]],
                          [self.grid[0][2], self.grid[1][1], self.grid[2][0]]
                          ]
        self.win_cells_position = [[[0, 0], [0, 1], [0, 2]],
                                   [[1, 0], [1, 1], [1, 2]],
                                   [[2, 0], [2, 1], [2, 2]],
                                   [[0, 0], [1, 0], [2, 0]],
                                   [[0, 1], [1, 1], [2, 1]],
                                   [[0, 2], [1, 2], [2, 2]],
                                   [[0, 0], [1, 1], [2, 2]],
                                   [[0, 2], [1, 1], [2, 0]]
                                   ]
        return self.win_cells

    def win_check(self):
        self.build_win_cells()
        if ['X', 'X', 'X'] in self.win_cells:
            return "X wins"
        elif ['O', 'O', 'O'] in self.win_cells:
            return "O wins"
        else:
            return ""

    def check_full(self):
        for x in range(3):
            for y in range(3):
                if self.grid[x][y] == "_":
                    return False
        return True

    def check_end(self):
        if self.win_check():
            return self.win_check()
        elif self.check_full():
            return "Draw"
        else:
            return ""

    def make_move(self):
        x = self.coordinates[0]
        y = self.coordinates[1]
        if self.coordinates in self.find_blank_positions():
            self.grid[x][y] = self.user_part
            print(f"move {self.user_part}")
        return self.grid

    def find_blank_positions(self):
        self.blank_positions = []
        for x in range(3):
            for y in range(3):
                if self.grid[x][y] == "_":
                    self.blank_positions.append([x, y])
        return self.blank_positions


class UserPlayer(TicTacToe):

    def play(self):
        self.coordinates = process_input()
        blank_positions = self.find_blank_positions()
        while True:
            if self.coordinates in blank_positions:
                self.make_move()
                return self.grid
            else:
                print("This cell is occupied! Choose another one!")
                self.coordinates = process_input()


class ComputerEasy(TicTacToe):

    def play(self):
        blank_positions = self.find_blank_positions()
        self.coordinates = random.choice(blank_positions)
        self.make_move()
        print('Making move level "easy"')
        return self.grid


class ComputerMedium(TicTacToe):

    def play(self):
        self.build_win_cells()
        opponent_point = None
        my_point = None

        for n in range(8):
            if self.win_cells[n].count(self.opponent_part) == 2 and "_" in self.win_cells[n]:
                i = self.win_cells[n].index("_")
                opponent_point = self.win_cells_position[n][i]

            if self.win_cells[n].count(self.user_part) == 2 and "_" in self.win_cells[n]:
                i = self.win_cells[n].index("_")
                my_point = self.win_cells_position[n][i]

        if my_point:
            self.coordinates = my_point
        elif opponent_point:
            self.coordinates = opponent_point
        else:
            blank_positions = self.find_blank_positions()
            self.coordinates = random.choice(blank_positions)
        self.make_move()
        print('Making move level "medium"')
        return self.grid


while True:
    parts = menu()
    if parts:
        if parts[0] == "user":
            x_part = UserPlayer("X")
        elif parts[0] == "easy":
            x_part = ComputerEasy("X")
        elif parts[0] == "medium":
            x_part = ComputerMedium("X")
        else:
            print("Bad parameters!")
        if parts[1] == "user":
            o_part = UserPlayer("O")
        elif parts[1] == "easy":
            o_part = ComputerEasy("O")
        elif parts[1] == "medium":
            o_part = ComputerMedium("O")
        else:
            print("Bad parameters!")
        print_grids(TicTacToe.grid)

        while True:
            if x_part.check_end():
                print(x_part.check_end())
                TicTacToe.grid = initial_grids("_" * 9)
                break
            else:
                if check_part(TicTacToe.grid) == "X":
                    x_part.play()
                    print("x")
                elif check_part(TicTacToe.grid) == "O":
                    o_part.play()
                    print("o")
                print_grids(TicTacToe.grid)
    else:
        break


