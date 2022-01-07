import random


# board class including grid status and method for checking it
class Board:
    def __init__(self, initial):
        self.initial = initial
        self.grid = self.initial_grids()
        self.win_cells = []
        self.win_cells_position = [[[0, 0], [0, 1], [0, 2]],
                                   [[1, 0], [1, 1], [1, 2]],
                                   [[2, 0], [2, 1], [2, 2]],
                                   [[0, 0], [1, 0], [2, 0]],
                                   [[0, 1], [1, 1], [2, 1]],
                                   [[0, 2], [1, 2], [2, 2]],
                                   [[0, 0], [1, 1], [2, 2]],
                                   [[0, 2], [1, 1], [2, 0]]
                                   ]
        self.blank_positions = self.find_blank_positions()
        self.result = None

# build initial grid
    def initial_grids(self):
        positions = list(self.initial)
        grids = []
        for n in range(3):
            grids.append([])
            for m in range(3):
                grids[n].append(positions[m + 3 * n])
        return grids

    def grid_is_empty(self):
        if self.grid == [["_" for i in range(3)] for n in range(3)]:
            return True
        else:
            return False

    def print_grids(self):
        print('---------')
        print('| ' + ' '.join(self.grid[0]) + ' |')
        print('| ' + ' '.join(self.grid[1]) + ' |')
        print('| ' + ' '.join(self.grid[2]) + ' |')
        print('---------')

# Analyze if there are 3 in a row
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
        return self.win_cells

    def win_check(self):
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
            return None

    def check_part(self):
        x_num = 0
        o_num = 0
        for x in range(3):
            for y in range(3):
                if self.grid[x][y] == "X":
                    x_num += 1
                elif self.grid[x][y] == "O":
                    o_num += 1
        if x_num == o_num:
            return "X"
        elif x_num > o_num:
            return "O"

    def find_blank_positions(self):
        self.blank_positions = []
        for x in range(3):
            for y in range(3):
                if self.grid[x][y] == "_":
                    self.blank_positions.append([x, y])
        return self.blank_positions

    def clone(self):
        self.initial = "".join(["".join(self.grid[i]) for i in range(3)])
        board = Board(self.initial)
        return board


class Player:
    def __init__(self, user_part):
        self.user_part = user_part
        self.coordinates = []
        self.opponent_part = self.opponent()

    def opponent(self):
        if self.user_part == "X":
            self.opponent_part = "O"
        else:
            self.opponent_part = "X"
        return self.opponent_part

    def make_move(self, board):
        x = self.coordinates[0]
        y = self.coordinates[1]
        if self.coordinates in board.blank_positions:
            board.grid[x][y] = self.user_part
            board.win_cells = board.build_win_cells()
            board.blank_positions = board.find_blank_positions()
            board.result = board.check_end()
            print(f"move {self.user_part}")


class UserPlayer(Player):

    # check input coordinates format
    def process_input(self):
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

    def play(self, board):
        self.coordinates = self.process_input()
        while True:
            if self.coordinates in board.blank_positions:
                self.make_move(board)
                return board
            else:
                print("This cell is occupied! Choose another one!")
                self.coordinates = self.process_input()


class ComputerEasy(Player):

    def play(self, board):
        self.coordinates = random.choice(board.blank_positions)
        self.make_move(board)
        print('Making move level "easy"')
        return board


class ComputerMedium(Player):

    def play(self, board):
        opponent_point = None
        my_point = None
        board.win_cells = board.build_win_cells()
        for n in range(8):
            if board.win_cells[n].count(self.opponent_part) == 2 and "_" in board.win_cells[n]:
                i = board.win_cells[n].index("_")
                opponent_point = board.win_cells_position[n][i]

            if board.win_cells[n].count(self.user_part) == 2 and "_" in board.win_cells[n]:
                i = board.win_cells[n].index("_")
                my_point = board.win_cells_position[n][i]

        if my_point:
            self.coordinates = my_point
        elif opponent_point:
            self.coordinates = opponent_point
        else:
            self.coordinates = random.choice(board.blank_positions)
        self.make_move(board)
        print('Making move level "medium"')
        return board


class ComputerHard(Player):

    def ai_make_move(self, board, part):
        # print(self.coordinates)
        x = self.coordinates[0]
        y = self.coordinates[1]
        if self.coordinates in board.blank_positions:
            board.grid[x][y] = part
            board.win_cells = board.build_win_cells()
            board.blank_positions = board.find_blank_positions()
            board.result = board.check_end()
            # board.print_grids()

    def decide_co(self, board, part):
        co_scores = []
        score = 0
        for position in board.blank_positions:
            new_board = board.clone()
            self.coordinates = position
            self.ai_make_move(new_board, part)
            new_board.result = new_board.check_end()

            if new_board.result:
                if part == self.user_part and new_board.result.startswith(self.user_part):
                    score = 10
                    return [position, score]

                elif part == self.opponent_part and new_board.result.startswith(self.opponent_part):
                    score = -10
                    return [position, score]

                else:
                    return [position, 0]

            else:
                if part == self.user_part:
                    co_score = self.decide_co(new_board, self.opponent_part)
                    co_scores.append([position, co_score[1]])

                if part == self.opponent_part:
                    co_score = self.decide_co(new_board, self.user_part)
                    co_scores.append([position, co_score[1]])
        result_score = None
        if part == self.user_part:
            for co_score in co_scores:
                if co_score[1] == 10:
                    return co_score
                elif result_score is None:
                    result_score = co_score
                elif co_score[1] == 0:
                    result_score = co_score
        if part == self.opponent_part:
            for co_score in co_scores:
                if co_score[1] == -10:
                    return co_score
                elif result_score is None:
                    result_score = co_score
                elif co_score[1] == 0:
                    result_score = co_score
        return result_score

    def play(self, board):
        if board.grid_is_empty():
            self.coordinates = random.choice(board.blank_positions)
            self.make_move(board)
        else:
            co_score = self.decide_co(board, self.user_part)
            self.coordinates = co_score[0]
            print('Making move level "hard"')
            self.ai_make_move(board, self.user_part)


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
                if x in ["easy", "user", "medium", "hard"] and o in ["easy", "user", "medium", "hard"]:
                    return [x, o]
                else:
                    print("Bad parameters!")
        elif user_in[0] == "exit":
            return None
        else:
            print("Bad parameters!")


my_board = Board("_" * 9)
while True:
    parts = menu()
    if parts:
        if parts[0] == "user":
            x_part = UserPlayer("X")
            my_board.print_grids()
        elif parts[0] == "easy":
            x_part = ComputerEasy("X")
        elif parts[0] == "medium":
            x_part = ComputerMedium("X")
        elif parts[0] == "hard":
            x_part = ComputerHard("X")
        else:
            print("Bad parameters!")
        if parts[1] == "user":
            o_part = UserPlayer("O")
        elif parts[1] == "easy":
            o_part = ComputerEasy("O")
        elif parts[1] == "medium":
            o_part = ComputerMedium("O")
        elif parts[1] == "hard":
            o_part = ComputerHard("O")
        else:
            print("Bad parameters!")

        while True:
            if my_board.result:
                print(my_board.result)
                my_board = Board("_" * 9)
                break
            else:
                if my_board.check_part() == "X":
                    x_part.play(my_board)
                    print("x")
                elif my_board.check_part() == "O":
                    o_part.play(my_board)
                    print("o")
                my_board.print_grids()
    else:
        break


