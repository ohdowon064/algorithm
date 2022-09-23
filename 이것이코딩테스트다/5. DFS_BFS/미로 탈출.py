from collections import deque

n, m = map(int, input().split())
map = [list(input()) for _ in range(n)]
steps = [[0] * m for _ in range(n)]
steps[0][0] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return steps[x][y]

        if map[x][y] == "1":
            map[x][y] = "0"

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if map[nx][ny] == "1":
                    q.append((nx, ny))
                    steps[nx][ny] = steps[x][y] + 1

print(bfs())