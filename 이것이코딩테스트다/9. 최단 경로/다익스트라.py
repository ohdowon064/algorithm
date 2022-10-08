n, m = map(int, input().split())
INF = int(1e9)
start = int(input())

graph = [[] for i in range(n + 1)]
visited = set()

distance = [INF] * (n + 1)

for _ in range(m):
    _from, _to, cost = map(int, input().split())

    graph[_from].append((_to, cost))

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

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited.add(now)

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

import heapq

def dijkstra_with_heap(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])