from collections import deque

n, m = map(int, input().split())
lab = []
viruses = []
for i in range(n):
    _lab = list(map(int, input().split()))
    lab.append(_lab)
    for j in range(n):
        if _lab[j] == 2:
            viruses.append((i, j))

min_time = float('inf')
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n

def dfs(comb: list, depth: int):
    global min_time
    if len(comb) == m:
        min_time = min(min_time, bfs(*comb))
        return

    if depth == len(viruses):
        return

    comb.append(viruses[depth])
    dfs(comb, depth + 1)
    comb.pop()
    dfs(comb, depth + 1)

wall = -2
blank = -1
def bfs(*active_viruses):
    q = deque()
    times = [[-1] * n for _ in range(n)]
    for r, c in active_viruses:
        times[r][c] = 0
        q.append((r, c))

    for i in range(n):
        for j in range(n):
            if lab[i][j] == 1:
                times[i][j] = wall

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if out_of_range(nr, nc):
                continue

            if lab[nr][nc] == 1:
                continue

            if times[nr][nc] == blank:
                times[nr][nc] = times[r][c] + 1
                q.append((nr, nc))

    for r, c in viruses:
        times[r][c] = 0

    result = float('-inf')
    for time in times:
        if blank in time:
            return float('inf')
        result = max(result, max(time))
    return result

dfs([], 0)
print(min_time if min_time < float('inf') else -1)