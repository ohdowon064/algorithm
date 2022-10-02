n = int(input())
numbers = [int(input()) for _ in range(n)]

print(*sorted(numbers, reverse=True))