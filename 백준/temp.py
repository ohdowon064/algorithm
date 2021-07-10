# bfs를 위한 queue 자료구조
from collections import deque
import sys
input = sys.stdin.readline

# n : 세로길이(행), m : 가로길이(열)
n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0)) # (0, 0)에서 시작

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 행렬을 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 방문하지 않은 길이 아닌 경우 -> 벽이 거나, 이미 방문한 길
            if miro[nx][ny] != 1:
                continue

            miro[nx][ny] = miro[x][y] + 1 # 최소 이동 칸 수 저장
            q.append((nx, ny))

    return miro[n - 1][m - 1] # (n, m)까지의 이동 칸 수 반환

print(bfs())