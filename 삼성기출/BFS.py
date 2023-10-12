from collections import deque

n = 10
# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n

def do_something(r, c):
    pass

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited = set()

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if out_of_range(nr, nc) or (nr, nc) in visited:
                continue
            do_something(nr, nc)
            q.append((nr, nc))
            visited.add((nr, nc))






