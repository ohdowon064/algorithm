T = int(input())
numbers = [list(map(int, input().split())) for _ in range(T)]

for a, b in numbers:
    print(a + b)