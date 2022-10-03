n = int(input())
foods = list(map(int, input().split()))

d = [0] * 101
d[1] = foods[0]
d[2] = max(foods[0], foods[1])

for i in range(3, n + 1):
    d[i] = max(d[i - 1], d[i - 2] + foods[i - 1])

print(d[n])