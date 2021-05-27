T = int(input())

for _ in range(T):
    scores = list(map(int, input().split()))[1:]
    avg = sum(scores) / len(scores)
    cnt = list(filter(lambda x: x > avg, scores))
    print(f'{len(cnt) / len(scores)* 100:.3f}%')
    