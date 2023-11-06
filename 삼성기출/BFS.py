from collections import deque

n = 10

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
    visited.add((r, c))

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if out_of_range(nr, nc) or (nr, nc) in visited:
                continue

            do_something(nr, nc)
            visited.add((nr, nc))
            q.append((nr, nc))


def bfs2(r, c):
    q = deque()
    visited = {(r, c)}
    q.append((r, c))

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if out_of_range(nr, nc) or (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            q.append((nr, nc))