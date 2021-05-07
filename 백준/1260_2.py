n, m, start = map(int, input().split())
from collections import defaultdict, deque

graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(node, visit=set()):
    print(node, end=' ')
    visit.add(node)

    for v in graph[node]:
        if v not in visit:
            dfs(v, visit)


def bfs():
    q = deque([start])
    visit = set([start])

    while q:
        node = q.popleft()
        print(node, end=' ')
        for v in graph[node]:
            if v not in visit:
                visit.add(v)
                q.append(v)


dfs(start)
print()
bfs()