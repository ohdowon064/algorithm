import collections
import heapq
import pprint
def dijk(times, N, K):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    pprint.pprint(graph)
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    if len(dist) == N:
        return max(dist.values())

    return -1

inp = [[3, 1, 3], [3, 2, 2], [2,1,2], [3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]]
print(dijk(inp, 8, 3))