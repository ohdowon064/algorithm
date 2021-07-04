"""
    1. 동전 N 종류
    2. 동전 합 K

"""
n, k = map(int, input().split())
coin_types = []
for _ in range(n):
    coin_types.append(int(input()))

ans = 0
coin_types.sort(reverse=True)
for coin in coin_types:
    if k >= coin:
       ans += k // coin
       k %= coin

print(ans)