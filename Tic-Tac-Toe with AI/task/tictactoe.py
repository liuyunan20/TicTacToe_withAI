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
def win_check(grids):
    win_cells = [[grids[0][0], grids[0][1], grids[0][2]],
                 [grids[1][0], grids[1][1], grids[1][2]],
                 [grids[2][0], grids[2][1], grids[2][2]],
                 [grids[0][0], grids[1][0], grids[2][0]],
                 [grids[0][1], grids[1][1], grids[2][1]],
                 [grids[0][2], grids[1][2], grids[2][2]],
                 [grids[0][0], grids[1][1], grids[2][2]],
                 [grids[0][2], grids[1][1], grids[2][0]]
                 ]

    if ['X', 'X', 'X'] in win_cells:
        return "X wins"
    elif ['O', 'O', 'O'] in win_cells:
        return "O wins"
    else:
        return ""


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


def check_full(grids):
    for x in range(3):
        for y in range(3):
            if grids[x][y] == "_":
                return False
    return True


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


def make_move(grids, co, part):
    x = co[0]
    y = co[1]
    if co in find_blank_positions(grids):
        grids[x][y] = part
    return grids


# def user_make_move(grids, co):
#     while True:
#         x = co[0]
#         y = co[1]
#
#         if check_blank_position(grids, co):
#             grids[x - 1][y - 1] = "X"
#             return grids
#         else:
#             print("This cell is occupied! Choose another one!")
#             co = process_input()


def find_blank_positions(grids):
    blank_positions = []
    for x in range(3):
        for y in range(3):
            if grids[x][y] == "_":
                blank_positions.append([x, y])
    return blank_positions


# def computer_move_easy(grids):
#     blank_positions = []
#     for x in range(3):
#         for y in range(3):
#             if grids[x][y] == "_":
#                 blank_positions.append([x, y])
#     p = random.choice(blank_positions)
#     x = p[0]
#     y = p[1]
#     grids[x][y] = "O"
#     return grids


def check_end(grids):
    if win_check(grids):
        return win_check(grids)
    elif check_full(grids):
        return "Draw"
    else:
        return ""


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
                if x in ["easy", "user"] and o in ["easy", "user"]:
                    return [x, o]
                else:
                    print("Bad parameters!")
        elif user_in[0] == "exit":
            return None
        else:
            print("Bad parameters!")


class TicTacToe:
    grid = initial_grids("_" * 9)

    def __init__(self, user_type, user_part):
        self.user_type = user_type
        self.user_part = user_part

    def game(self):
        blank_positions = find_blank_positions(self.grid)
        if self.user_type == "user":
            coordinates = process_input()
            while True:
                if coordinates in blank_positions:
                    make_move(self.grid, coordinates, self.user_part)
                    return self.grid
                else:
                    print("This cell is occupied! Choose another one!")
                    coordinates = process_input()
        elif self.user_type == "easy":
            coordinates = random.choice(blank_positions)
            make_move(self.grid, coordinates, self.user_part)
            print('Making move level "easy"')
            return self.grid
        else:
            print("Bad parameters!")


    # while True:
    #     if check_end(grid):
    #         print(check_end(grid))
    #         break
    #     else:
    #
    #         if check_part(grid) == "X":
    #             coordinates = process_input()
    #             grid = user_make_move(grid, coordinates)
    #         elif check_part(grid) == "O":
    #             grid = computer_move_easy(grid)
    #             print('Making move level "easy"')
    #         print_grids(grid)


while True:
    parts = menu()
    if parts:
        x_part = TicTacToe(parts[0], "X")
        o_part = TicTacToe(parts[1], "O")
        print_grids(TicTacToe.grid)
        while True:
            if check_end(TicTacToe.grid):
                print(check_end(TicTacToe.grid))
                TicTacToe.grid = initial_grids("_" * 9)
                break
            else:
                if check_part(TicTacToe.grid) == "X":
                    x_part.game()
                elif check_part(TicTacToe.grid) == "O":
                    o_part.game()

                print_grids(TicTacToe.grid)
    else:
        break


