from collections import deque
m, n = map(int, input().split())
maze = [list(input()) for _ in range(m)]
print(maze)
def bfs():
    q = deque((0, 0, 1))

    while q:
        i, j, cnt = q.popleft()
        if i == m - 1 and j == n - 1:
            return cnt
        elif maze[i][j] != '1':

        maze[i][j] = '0'
        if i >= 0:
            q.

print(dfs(0, 0, 1))