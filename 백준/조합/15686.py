n, m = map(int, input().split())

chicken_locations = []
house_locations = []
city = []
for i in range(n):
    elements = list(map(int, input().split()))
    city.append(elements)
    for j in range(n):
        if elements[j] == 2:
            chicken_locations.append((i, j))
        elif elements[j] == 1:
            house_locations.append((i, j))


def dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def get_min_dist(comb):
    min_dist = 0
    for house in house_locations:
        my_min_dist = float('inf')
        for chicken in comb:
            my_min_dist = min(my_min_dist, dist(*house, *chicken))

        min_dist += my_min_dist
    return min_dist


def dfs(comb: list, depth: int):
    global final_min_dist

    if len(comb) == m:
        final_min_dist = min(final_min_dist, get_min_dist(comb))
        return

    if depth == len(chicken_locations):
        return

    comb.append(chicken_locations[depth])
    dfs(comb, depth + 1)
    comb.pop()
    dfs(comb, depth + 1)


final_min_dist = float('inf')
dfs([], 0)

print(final_min_dist)
