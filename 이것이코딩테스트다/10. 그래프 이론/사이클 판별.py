v, e = map(int, input().split())
parent_table = [i for i in range(v + 1)]


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

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_root(a) == find_root(b):
        cycle = True
        break
    else:
        union_root(a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 없음")