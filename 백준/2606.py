"""
    문제
    1. 1번을 통해 감염되는 컴퓨터 수

    알고리즘
    1. 1번과 연결된 컴퓨터 수 구하기
    2. dfs

"""
from collections import defaultdict
n = int(input())
k = int(input())

graph = defaultdict(list)
visited = set()

for _ in range(k):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited.add(v)

    for i in graph[v]:
        if i not in visited:
            dfs(i)

dfs(1)
print(len(visited) - 1) # 1번 컴퓨터 제외