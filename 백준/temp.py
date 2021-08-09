n = int(input())
graph = [list(map(int, input())) for _ in range(n)]


apart = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

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

count = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            apart.append(count)
            count = 0
apart.sort()
print(len(apart), *apart, sep='\n')