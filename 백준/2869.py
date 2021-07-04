import math
up, down, h = map(int, input().split())

per_day = up - down
print(math.ceil((h - up) / per_day) + 1)