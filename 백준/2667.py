"""
    문제
    1. 집 : 1
        집없는곳 : 0
    2. 단지 구성하기
    3. 단지 구성 : 상하좌우 연결
    4. 각 단지별 집 수 오름차순으로 출력

    알고리즘
    1. dfs 탐색하면서 단지 파악
    2. 리턴 시 단지의 집 수 반환
"""
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

apart = []
count = 0

def dfs(x, y):
    global count
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])

        return True

    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            apart.append(count)
            count = 0

apart.sort()
print(len(apart))
for k in apart:
    print(k)