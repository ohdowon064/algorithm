"""
    문제
    1. 섬 개수 구하기
    2. 가로, 세로, 대각선이면 같은 섬
    3. 1 : 땅, 0 : 바다
    4. 입력 마지막은 0, 0

    알고리즘
    1. dfs
    2. 상하좌우, 대각선까지 이동
"""
import sys
print(sys.getrecursionlimit())

def dfs(x, y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0

        for i in range(8):
            dfs(x + dx[i], y + dy[i])

        return True
    return False

while True:
    # 너비(열) : w, 높이(행) : h
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    # 상하좌우, 우상, 좌상, 우하, 좌하
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]

    ans = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                ans += 1
    print(ans)


