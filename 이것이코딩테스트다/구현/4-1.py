n = int(input())
plans = input().split()
x, y = 1, 1

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i, move in enumerate(move_types):
        if move == plan:
            nx = x + dx[i]
            ny = y + dy[i]
            break

    if nx >= 1 and ny >= 1 and nx <= n and ny <= n:
        x, y = nx, ny

print(x, y)