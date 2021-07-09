"""
    문제
    1. n * m 토마토 창고
    2. 익은 토마토 인접 토마토는 같이 익음
    3. 인접 -> 상하좌우, 대각선 포함 x
    4. 혼자 익는 경우 x
    5. 모든 토마토가 익는 최소 일수

    입력 조건
    1. 1 : 익은 토마토
    2. 0 : 안 익은 토마토
    3. -1 : 토마토 없는 칸

    출력 조건
    1. 이미 모두 익음 : 0
    2. 모두 익을 수 없음 : -1
    3. 모두 익는데 최소 일수

    알고리즘
    1. bfs
    2. 각 칸의 토마토가 익는데 걸린 날짜 저장
    3. 토마토 창고에서 가장 큰 수 반환
"""
# bfs를 위해서 deque를 통한 자료구조 queue
from collections import deque

# 입력
m, n  = map(int, input().split()) # 창고 크기 n * m
graph = [list(map(int, input().split())) for _ in range(n)] # 각 토마토 상태

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수 정의
def bfs():
    while q:
        x, y = q.popleft()

        # 상하좌우로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

# 이미 모두 익은 토마토인 경우
count = 0
for tomato in graph:
    count += sum(tomato)

if count == n * m:
    print(0)
else:
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j))

    bfs()
    ans = float('-inf')
    for tomato in graph:
        if 0 in tomato:
            ans = -1
            break
        ans = max(ans, max(tomato))

    print(ans if ans == -1 else ans - 1)