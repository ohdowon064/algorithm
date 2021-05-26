n = int(input())
result, cnt = n, 0

while result != n or cnt == 0:
    result = 10 * (result % 10) + (sum(divmod(result, 10)) % 10)
    cnt += 1
print(cnt)
