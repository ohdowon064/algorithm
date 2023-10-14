from collections import deque

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = 5, 5

def get_adjacent(node):
    x, y = node
    adjacent_nodes = []

    for dx, dy in directions:
        nx, ny = (x + dx) % n, (y + dy) % m
        adjacent_nodes.append((nx, ny))

    return adjacent_nodes


def bfs(grid, start, end):
    visited = {start}
    q = deque()
    q.append((start, [start]))

    while q:
        node, path = q.popleft()
        if node == end:
            return path

        if node in visited:
            continue

        for adj in get_adjacent(node):
            if grid[adj[0]][adj[1]] != 0 or adj in visited:
                continue

            visited.add(adj)
            q.append((adj, path + [adj]))

