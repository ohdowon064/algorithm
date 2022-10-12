"""
입력값
5
2 3 1 2 2
"""
n = int(input())
mans = list(map(int, input().split()))
mans.sort()

i = 0
result = 0
while i < n:
    team = mans[i: i+mans[i]]
    if len(team) >= max(team):
        result += 1
    i += mans[i]

print(result)


