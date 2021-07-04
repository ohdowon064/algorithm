from collections import defaultdict

inputString = '77777729'
numbers = range(1000)
data = []

k = 0
n = 0
while n < 1000:
    if not inputString:
        break
    if k + 10 == n:
        k = n
    if n <= k + int(inputString[0]):
        if n == k + int(inputString[0]):
            inputString = inputString[1:]

    n += 1

print(n-1)
