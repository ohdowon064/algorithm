# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def dfs_with_stack(graph, v):
    visited = [False] * 9  # 0번 노드제외 총 8개 노드
    stack = [v]

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            print(node, end=' ')

            stack.extend(reversed(graph[node]))

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

visited = [False] * 9 # 0번 노드제외 총 8개 노드

dfs(graph, 1, visited) # 1번 노드를 최상위 노드로 호출

dfs_with_stack(graph, 1)
