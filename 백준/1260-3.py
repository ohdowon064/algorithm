"""
    문제
    1. dfs, bfs 탐색 결과 출력
    2. 인접 노드 여러개 -> 번호가 작은 것을 우선

    입력조건
    1. 정점 개수 N
    2. 간선 개수 M
    3. 탐색 시작 번호 V
    4. 연결 노드

    출력 조건
    1. DFS
    2. BFS
"""
from collections import defaultdict, deque

n, m, v = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    u, w = map(int, input().split())
    graph[u].append(w)
    graph[w].append(u)

for node in graph:
    graph[node].sort()

visited = set()
def dfs(v, visited):
    visited.add(v)
    print(v, end=' ')

    for i in graph[v]:
        if i not in visited:
            dfs(i, visited)

def bfs(v, visited):
    q = deque()
    q.append(v)
    visited.add(v)

    while q:
        node = q.popleft()
        print(node, end=' ')

        for i in graph[node]:
            if i not in visited:
                q.append(i)
                visited.add(i)

dfs(v, visited)
visited.clear()
print()
bfs(v, visited)

