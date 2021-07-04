import math

T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    floor = h if n % h == 0 else n % h
    room = math.ceil(n / h)
    print(floor * 100 + room)