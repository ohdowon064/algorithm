"""
입력값
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""
v, e = map(int, input().split())
parent_table = [i for i in range(v + 1)]

edges = []
result = 0

for _ in range(e):
    x, y, cost = map(int, input().split())
    edges.append((cost, x, y))

edges.sort()


def find_root(x):
    if parent_table[x] != x:
        parent_table[x] = find_root(parent_table[x])
    return parent_table[x]

def union_root(x, y):
    x_root = find_root(x)
    y_root = find_root(y)

    if x_root < y_root:
        parent_table[y_root] = x_root
    else:
        parent_table[x_root] = y_root

for cost, x, y in edges:
    # x, y 사이에 사이클이 없는 경우
    if find_root(x) != find_root(y):
        union_root(x, y)
        result += cost

print(result)