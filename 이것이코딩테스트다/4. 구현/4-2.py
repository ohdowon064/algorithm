n = int(input())

ans = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if '3' in f'{h}{m}{s}':
                ans += 1

print(ans)