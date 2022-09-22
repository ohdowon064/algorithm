n, m = map(int, input().split())

answer = 0
for _ in range(n):
    min_value = min(list(map(int, input().split())))
    answer = max(answer, min_value)

print(answer)