"""
input
5 3
1 3 2 3 2

input
8 5
1 5 4 3 2 4 5 2
"""
n, m = map(int, input().split())
balls = list(map(int, input().split()))

weights = [0] * 11
for ball in balls:
    weights[ball] += 1

result = 0
for i in range(1, m + 1):
    n -= weights[i]
    result += weights[i] * n

print(result)