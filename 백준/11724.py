"""
    문제
    1. 연결요소 구하기
    2. 정점개수 n, 간선개수 m
    3.

    알고리즘
    1. dfs
    2.

"""
from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = set()

def dfs(v):
    visited.add(v)

    for i in graph[v]:
        if i not in visited:
            dfs(i)

ans = 0
for i in range(1, n + 1):
    if i not in visited:
        dfs(i)
        ans += 1

print(ans)