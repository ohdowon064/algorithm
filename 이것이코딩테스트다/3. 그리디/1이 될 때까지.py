n, k = map(int, input().split())

count = 0
# while n != 1:
#     if n % k == 0:
#         n //= k
#     else:
#         n -= 1
#     count += 1

while True:
    target = (n // k) * k
    count += (n - target)
    n = target
    if n < k:
        break
    count += 1
    n //= k

count += (n - 1)


print(count)

