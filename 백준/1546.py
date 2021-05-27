N = int(input())
scores = list(map(int, input().split()))
scores = list(map(lambda x: x/max(scores)*100, scores))

print(sum(scores) / N)