T = int(input())

for _ in range(T):
    ox = input().split('X')
    score = 0
    for o in ox:
        score += len(o) * (len(o) + 1) // 2
    print(score)