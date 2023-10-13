from collections import deque
from copy import deepcopy

n, q = map(int, input().split())
ices = [list(map(int, input().split())) for _ in range(2**n)]
lengths = list(map(int, input().split()))

def rotate(board):
    return list(map(list, zip(*board[::-1])))

def rotate_sublist(board, ar, ac, br, bc):
    sublist = [row[ac: bc + 1] for row in board[ar: br + 1]]
    sublist = rotate(sublist)
    for i in range(ar, br + 1):
        for j in range(ac, bc + 1):
            board[i][j] = sublist[i - ar][j - ac]
    return board

cases: list
candidates: list
visited = set()

def combination_with_duplicate(comb, depth):
    if len(comb) == 2:
        cases.append(comb.copy())
        return

    if depth == len(candidates):
        return

    comb.append(candidates[depth])
    combination_with_duplicate(comb, depth)
    comb.pop()
    combination_with_duplicate(comb, depth + 1)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def out_of_range(r, c):
    return r < 0 or r >= 2**n or c < 0 or c >= 2**n

for l in lengths:
    if l != 0:
        cases = []
        candidates = list(range(0, 2**n, 2**l))
        combination_with_duplicate([], 0)

        for ar, ac in cases:
            rotate_sublist(ices, ar, ac, ar + 2**l - 1, ac + 2**l - 1)

    _ices = deepcopy(ices)
    for r in range(2**n):
        for c in range(2**n):
            ice_count = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if out_of_range(nr, nc) or ices[nr][nc] == 0:
                    continue
                ice_count += 1

            if ice_count < 3:
                _ices[r][c] -= 1

    ices = deepcopy(_ices)


print(sum([sum(row) for row in ices]))


