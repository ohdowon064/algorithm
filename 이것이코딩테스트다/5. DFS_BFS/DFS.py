# DFS 메서드 정의
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
visited = set()

def dfs(graph, v, visited):
    visited.add(v)
    print(v, end=" ")

    for i in graph[v]:
        if i not in visited:
            dfs(graph, i, visited)

def dfs_with_stack(graph, v):
    visited = [False] * 9
    stack = [v]

    while stack:
        _v = stack.pop()

        if not visited[_v]:
            visited[_v] = True
            print(_v, end=" ")
            stack.extend(reversed(graph[_v]))

dfs(graph, 1, visited)
print()
dfs_with_stack(graph, 1)
