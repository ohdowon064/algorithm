# graph = {
#     1: [2, 3, 8],  # 1번 노드에 2, 3, 8번 노드가 연결되어있다.
#     2: [1, 7],
#     3: [1, 4, 5],
#     4: [3, 5],
#     5: [3, 4],
#     6: [7],
#     7: [2, 6, 8],
#     8: [1, 7]
# }
#
#
# def dfs():
#     visited = set()
#     s = [1]
#
#     while s:
#         v = s.pop()
#
#         if v not in visited:
#             visited.add(v)
#             print(v, end=' ')
#             s.extend(reversed(graph[v]))
#
#
# dfs()


from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v):
    s = [v]

    while s:
        node = s.pop()

        if node not in visited:
            s.extend(reversed(graph[node]))
            visited.add(node)

visited = set()
ans = 0
for v in range(1, n + 1):
    if v not in visited:
        dfs(v)
        ans += 1