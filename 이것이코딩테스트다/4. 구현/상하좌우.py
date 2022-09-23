n = int(input())
moves = input().split()
print(n, moves)
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

dir = {"L": 0, "R": 1, "U": 3, "D": 2}

start = (0, 0)
for move in moves:
    nx, ny = start[0] + dx[dir[move]], start[1] + dy[dir[move]]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue

    start = nx, ny

print(start[0] + 1, start[1] + 1)