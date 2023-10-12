from collections import deque
from pprint import pprint

n, m = map(int, input().split())
virus = []
lab = []
for i in range(n):
    row = list(map(int, input().split()))
    lab.append(row)
    for j in range(n):
        if row[j] == 2:
            virus.append((i, j))

min_time = float('inf')
def dfs(comb: list, depth: int):
    global min_time
    if len(comb) == m:
        min_time = min(min_time, bfs(*comb))
        return

    if depth == len(virus):
        return

    comb.append(virus[depth])
    dfs(comb, depth + 1)
    comb.pop()
    dfs(comb, depth + 1)


def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(*pos):
    q = deque()
    times = [[-2] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 1:
                times[i][j] = -1

    for p in pos:
        times[p[0]][p[1]] = 0
        q.append(p)

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if out_of_range(nr, nc):
                continue

            if lab[nr][nc] == 1:
                times[nr][nc] = -1
                continue

            if times[nr][nc] == -2:
                times[nr][nc] = times[r][c] + 1
                q.append((nr, nc))

    for v in virus:
        times[v[0]][v[1]] = 0

    time = float('-inf')
    # pprint(times)
    for t in times:
        if -2 in t:
            return float('inf')
        time = max(max(t), time)
    return time

dfs([], 0)
print(min_time if min_time != float('inf') else -1)
