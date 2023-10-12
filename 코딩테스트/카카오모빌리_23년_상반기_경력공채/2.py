from collections import deque


def solution(N: int, A: list, B: list):
    if set(A).union(set(B)) != set(range(1, N + 1)):
        return False

    edges = sorted(zip(A, B), key=lambda x: min(x))
    for i, j in edges:
        pass


def solution2(N, A, B):
    graph = {i: set() for i in range(1, N + 1)}
    for a, b in zip(A, B):
        graph[a].add(b)
        graph[b].add(a)

    print(graph)
    if any(not v for v in graph.values()):
        print("볼 것도 없음")
        print(False)
        return

    for i in range(1, N):
        if i + 1 not in graph[i]:
            print(False)
            return
    print(True)
    return

solution2(4, [1, 2, 4, 4, 3], [2, 3, 1, 3, 1])
solution2(4, [1, 2, 1, 3], [2, 4, 3, 4])
solution2(6, [2, 4, 5, 3], [3, 4, 6, 4])
solution2(3, [1, 3], [2, 2])


def solution(N, A, B):
    graph = {i: set() for i in range(1, N + 1)}
    isolated = set([i for i in range(1, N + 1)])
    for a, b in zip(A, B):
        graph[a].add(b)
        graph[b].add(a)
        isolated.discard(a)
        isolated.discard(b)

    if isolated:
        return False

    for i in range(1, N):
        if i + 1 not in graph[i]:
            return False
    return True