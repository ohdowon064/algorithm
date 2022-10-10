v, e = map(int, input().split())
parent_table = [i for i in range(v + 1)]

def find_root(x):
    if parent_table[x] != x:
        return find_root(parent_table[x])
    return x

def union_root(a, b):
    a_root = find_root(a)
    b_root = find_root(b)

    if a_root < b_root:
        parent_table[b_root] = a_root
    else:
        parent_table[a_root] = b_root


for i in range(e):
    a, b = map(int, input().split())
    union_root(a, b)

print("각 원소가 속한 집합: ", end=" ")
for i in range(1, v + 1):
    print(find_root(i), end=" ")

print()

print("부모 테이블:", end=" ")
for i in range(1, v + 1):
    print(parent_table[i], end=" ")