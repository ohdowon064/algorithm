n, m = map(int, input().split())
chickens = []
houses = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            houses.append((i, j))
        elif row[j] == 2:
            chickens.append((i, j))

def dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

min_dist = float('inf')
def calc_min_dist(comb):
    _min_dist = 0
    for house in houses:
        my_min_dist = float('inf')
        for chicken in comb:
            my_min_dist = min(my_min_dist, dist(*house, *chicken))
        _min_dist += my_min_dist

    return _min_dist



def dfs(comb: list, depth: int):
    global min_dist
    if len(comb) == m:
        min_dist = min(min_dist, calc_min_dist(comb))
        return

    if depth == len(chickens):
        return

    comb.append(chickens[depth])
    dfs(comb, depth + 1)
    comb.pop()
    dfs(comb, depth + 1)


dfs([], 0)
print(min_dist)