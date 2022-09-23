from collections import deque

n, m = map(int, input().split())
tray = [list(input()) for _ in range(n)]
print(n, m)
print(tray)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r, c):
    q = deque([(r, c)])

    count = 0
    while q:
        x, y = q.popleft()

        if tray[x][y] == "0":
            count += 1
            tray[x][y] = "#"

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if tray[nx][ny] == "0":
                q.append((nx, ny))

    if count > 0:
        return True
    return False

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if tray[x][y] == "0":
        tray[x][y] = "1"
        for i in range(4):
            dfs(x + dx[i], y + dy[i])

        return True
    return False

ice = 0
for r in range(n):
    for c in range(m):
        if dfs(r, c):
            ice += 1
print(ice)