"""
입력값
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""
n, m = map(int ,input().split())
city = [i for i in range(n + 1)]
edges = []



def find_city(x):
    if city[x] != x:
        city[x] = find_city(city[x])
    return city[x]


def union_city(x, y):
    x_city = find_city(x)
    y_city = find_city(y)

    if x_city < y_city:
        city[y_city] = x_city
    else:
        city[x_city] = y_city

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))


edges.sort()

result = 0
last = 0
for cost, x, y in edges:
    if find_city(x) != find_city(y):
        result += cost
        union_city(x, y)
        last = cost

print(result - last)