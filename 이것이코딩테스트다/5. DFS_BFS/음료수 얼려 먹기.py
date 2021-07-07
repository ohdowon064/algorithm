"""
    문제
    1. n * m 얼음틀
    2. 0 : 구멍
    3. 1 : 칸막이
    4. 아이스크림 개수구하기

    입력조건
    1. 세로길이 N -> 행 개수 N
    2. 가로길이 M -> 열 개수 M

    출력조건
    1. 가능한 아이스크림 개수 출력

    알고리즘
    1. DFS 탐색
        -> 탐색 끊기면 아이스크림 한개
"""
n, m = map(int, input().split())
ice_cube = [list(input()) for _ in range(n)]

# 상하좌우 : (-1, 0), (1, 0), (0, -1), (0, 1)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(ice_cube, x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if ice_cube[x][y] == "0":
        ice_cube[x][y] = "#"

        for i in range(4):
            dfs(ice_cube, x + dx[i], y + dy[i])
        return True

    return False

ans = 0
for i in range(n):
    for j in range(m):
        if dfs(ice_cube, i, j) == True:
            ans += 1

print(ans)
