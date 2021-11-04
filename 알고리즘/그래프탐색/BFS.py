from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = set([start])

    while q:
        node = q.popleft()
        print(node, end=" ")

        for adj in graph[node]:
            if adj not in visited:
                visited.add(adj)
                q.append(adj)

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

bfs(graph, 1)

