"""
문제
1. 2진트리
2. 0: 양
3. 1: 늑대
4. info[i] = i번 노드에 있는 양 또는 늑대
"""
from collections import defaultdict


def solution(info, edges):
    tree = defaultdict(list)

    for parent, child in edges:
        tree[parent].append(child)
        tree[child].append(parent)

    visited = set()
    wolf = sheep = 0

    def dfs(node):
        nonlocal wolf, sheep

        visited.add(node)
        print(node, end=' ')

        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1
        if wolf >= sheep:
            return sheep

        for i in tree[node]:
            if i not in visited:
                dfs(i)

    dfs(0)
    print()
    print(wolf, sheep)


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
solution(info, edges)