n = int(input())
mans = list(map(int, input().split()))
mans.sort()

count = 0
i = 0
while True:
    if len(mans[i: i + mans[i]]) >= max(mans[i: i + mans[i]]):
        count += 1
    if i + mans[i] >= n:
        break
    i = i + mans[i]

print(count)