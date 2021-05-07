from collections import defaultdict, deque
n, m, start = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for node in graph:
    graph[node].sort()

def dfs(node, visit=set()):
    print(node, end=' ')
    visit.add(node)
    for v in graph[node]:
        if v not in visit:
            dfs(v)

def bfs(root):
    q = deque([root])
    visit = [root]
    while q:

        node = q.popleft()
        print(node, end=' ')

        for v in graph[node]:
            if v not in visit:
                visit.append(v)
                q.append(v)

dfs(start)
print()
bfs(start)





