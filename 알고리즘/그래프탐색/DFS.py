

def dfs(graph: dict[list], visited: set, node: int):
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
