"""
입력값
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
costs = [0] * n
indegree = [0] * n

for i in range(n):
    cost, *needs = map(int, input().split())
    costs[i] = cost

    for need in needs[:-1]:
        graph[need - 1].append(i)
        indegree[i] += 1

def topology_sort():
    result = costs[:]
    q = deque()

    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + costs[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    print(result)

topology_sort()