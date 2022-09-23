from collections import deque

# 그래프 - 인접리스트
graph = [
    [],
    [2, 3, 8], # 1번 노드에 2, 3, 8번 노드가 연결되어있다.
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# BFS 메서드 정의
def bfs(graph, start):
    q = deque([start])
    visited = {start}

    while q:
        v = q.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if i not in visited:
                q.append(i)
                visited.add(i)


bfs(graph, 1)