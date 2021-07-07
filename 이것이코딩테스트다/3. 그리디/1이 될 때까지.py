n, k = map(int, input().split())

count = 0
while n >= k:
    n //= k
    count += 1

print(count if n == 1 else count + (n - 1))