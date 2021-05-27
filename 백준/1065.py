def isAp(n):
    n = str(n)
    if len(n) == 1 or len(n) == 2:
        return True

    dist = []
    n = list(map(int, n))
    for i in range(len(n) - 1):
        dist.append(n[i] - n[i+1])

    return dist.count(dist[0]) == len(dist)

N = int(input())
print(len(list(filter(isAp, range(1, N+1)))))
