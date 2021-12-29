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
                return [user_in_1, user_in_2]


def check_blank_position(grids, co):
    x = co[0]
    y = co[1]
    if grids[x - 1][y - 1] == "_":
        return True
    else:
        return False


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


def make_move(grids, co):
    while True:
        x = co[0]
        y = co[1]

        if check_blank_position(grids, co):
            grids[x - 1][y - 1] = check_part(grids)
            return grids
        else:
            print("This cell is occupied! Choose another one!")
            co = process_input()


def check_end(grids):
    if win_check(grids):
        return win_check(grids)
    elif check_full(grids):
        return "Draw"
    else:
        return ""


initials = input("Enter the cells: ")
grid = initial_grids(initials)
print_grids(grid)


coordinates = process_input()
grid = make_move(grid, coordinates)
print_grids(grid)
if check_end(grid):
    print(check_end(grid))
else:
    print("Game not finished")


