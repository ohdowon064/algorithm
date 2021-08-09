from collections import defaultdict
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = defaultdict(list)
visited = set()
distance = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 방문안한 노드 중, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and i not in visited:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited.add(start)

    for v, w in graph[start]:
        distance[v] = w

    for i in range(n - 1):
        now = get_smallest_node()
        visited.add(now)

        for v, w in graph[now]:
            cost = distance[now] + w
            if cost < distance[v]:
                distance[v] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])