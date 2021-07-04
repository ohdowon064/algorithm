"""
    1. 지뢰 : -1
    2. 지뢰인접 : 지뢰개수 (상하좌우, 대각선)


"""
n = 9
mine = [ [1, 1], [1, 7], [2, 7], [3, 6], [4, 1], [4, 4], [4, 8], [8, 4], [8, 5], [9, 6] ]

board = [[0] * n for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for x, y in mine:
    board[x-1][y-1] = -1


for x, y in mine:
    for i in range(8):
        nx = (x - 1) + dx[i]
        ny = (y - 1) + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny] == -1:
            continue

        board[nx][ny] += 1

print(board)