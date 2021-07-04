T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    if n == 1:
        print(1)
        continue

    if k == 0:
        print(n)
        continue

    apart = [[i for i in range(1, n + 1)] for i in range(k + 1)]

    for floor in range(1, k + 1):
        for room in range(1, n):
            apart[floor][room] = apart[floor-1][room] + apart[floor][room-1]

    print(apart[k][n - 1])



