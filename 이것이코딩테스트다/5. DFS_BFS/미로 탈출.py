"""
    문제
    1. n * m 미로
    2. 처음위치 (1, 1)
    3. 출구 (n, m)
    4. 괴물 : 0
    5. 괴물 없음 : 1
    6. 움직이는 최소 칸 개수 구하기
"""
from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# def bfs(miro):
#     q = deque([(0, 0, 0)])
#
#     while q:
#         x, y, count = q.popleft()
#         if miro[x][y] == 1:
#             miro[x][y] = 0
#
#             for i in range(4):
#                 nx, ny = x + dx[i], y + dy[i]
#                 ncnt = count + 1
#                 if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                     continue
#
#                 if nx == n - 1 and ny == n - 1:
#                     return ncnt
#
#                 q.append((nx, ny, ncnt))
#
# print(bfs(miro))

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if miro[nx][ny] == 0:
                continue

            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                q.append((nx, ny))

    return miro[n - 1][m - 1]

print(bfs(0, 0))












