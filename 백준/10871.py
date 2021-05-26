import sys
n, x = map(int, input().split())
numbers = list(filter(lambda k : k < x, map(int, sys.stdin.readline().split())))
print(*numbers)


