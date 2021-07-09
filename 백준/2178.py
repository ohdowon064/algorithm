"""
    문제
    1. n * m 미로탈출하기
    2. 시작 : (1, 1)
    3. 도착 : (n, m)
    4. 최소칸 수 구하기
    5. 벽 : 0
        길 : 1

    알고리즘
    1. bfs 탐색하면서 길에 이동칸 수 기록
"""
from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if miro[nx][ny] != 1:
                continue

            miro[nx][ny] = miro[x][y] + 1
            q.append((nx, ny))

    return miro[n - 1][m - 1]

print(bfs())










