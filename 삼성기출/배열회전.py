from copy import deepcopy
from pprint import pprint


def transpose(board):
    return list(map(list, zip(*board)))

def rotate(board, clockwise=True):
    if clockwise:
        return list(map(list, zip(*board[::-1])))
    return transpose(board)[::-1]

n = 5
myboard = [[i * n + j for j in range(1, n + 1)] for i in range(n)]

# pprint(transpose(myboard))
# pprint(rotate(myboard))
# pprint(rotate(myboard, clockwise=False))

def rotate_sublist(board, xr, xc, yr, yc):
    board = deepcopy(board)
    sublist = [row[xc: yc + 1] for row in board[xr: yr + 1]]
    sublist = rotate(sublist)
    for i in range(xr, yr + 1):
        for j in range(xc, yc + 1):
            board[i][j] = sublist[i - xr][j - xc]

    return board
pprint(myboard)
pprint(rotate_sublist(myboard, 1, 1, 3, 3))