n = int(input())
scores = [input().split() for _ in range(n)]
scores.sort(key=lambda x: int(x[1]))
for score in scores:
    print(score[0], end=" ")