

def dfs(graph, visited: set, node: int):
    visited.add(node)
    print(node, end=" ")

    for adj in graph[node]:
        if adj not in visited:
            dfs(graph, visited, adj)

graph = {
   1: [2, 3, 8], # 1번 노드에 2, 3, 8번 노드가 연결되어있다.
   2: [1, 7],
   3: [1, 4, 5],
   4: [3, 5],
   5: [3, 4],
   6: [7],
   7: [2, 6, 8],
   8: [1, 7]
}

dfs(graph, set(), 1)

def dfs2(graph, visited, cur):
    visited.add(cur)
    print(cur, end=" ")

    for node in graph[cur]:
        if node not in visited:
            dfs2(graph, visited, node)

print()
dfs2(graph, set(), 1)


def mydfs(visited, curr):
    visited.add(curr)
    print(curr, end=" ")

    for v in graph[curr]:
        if v not in visited:
            mydfs(visited, v)

print()
mydfs(set(), 1)