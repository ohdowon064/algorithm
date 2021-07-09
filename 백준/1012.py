"""
    문제
    1. 인접 : 상하좌우
    2. 인접한 배추 구역 개수 구하기
    3. 0 : 배추없는땅, 1 : 배추

    알고리즘
    1. dfs
    2. 구역개수 구하기
"""
import sys
sys.setrecursionlimit(10000)

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0

        for i in range(4):
            dfs(x + dx[i], y + dy[i])

        return True
    return False

for _ in range(T):
    # 가로(열), 세로(행), 배추개수
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        col, row = map(int, input().split())
        graph[row][col] = 1

    ans = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                ans += 1

    print(ans)