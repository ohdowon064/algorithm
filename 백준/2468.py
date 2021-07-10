"""
    문제
    1. 안전영역 최대 몇개
    2. 일정 높이 이하 지점은 물에 잠김
    3. n * n 정배열
    4. 각 지점에 높이 표시
    5. 안전영역 : 상하좌우 인접

    알고리즘
    1. 최솟값 ~ 최댓값 비 조절
    2. dfs로 안전영역 개수 비교
"""
import sys
from copy import deepcopy
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

min_height = 101
max_height = 0
for i in graph:
    max_height = max(max_height, max(i))
    min_height = min(min_height, min(i))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(area, x, y, h):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if area[x][y] > h:
        area[x][y] = 0

        for i in range(4):
            dfs(area, x + dx[i], y + dy[i], h)
        return True

    return False

ans = 0
for h in range(min_height, max_height):
    area = deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if dfs(area, i, j, h):
                cnt += 1
    ans = max(ans, cnt)

print(ans)