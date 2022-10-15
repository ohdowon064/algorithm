"""
입력값
5
3 2 1 1 9

압력값 - 답: 22
5
1 2 4 5 9
"""
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
    if target < coin:
        break
    target += coin

print(target)