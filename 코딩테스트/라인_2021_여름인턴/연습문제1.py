"""
    코니 : c, c+1, c+3, c+6 ...
    브라운 : b -> b-1, b+1, 2*b
    1. 브라운이 코니 잡음 -> 잡는 최소시간 N
    2. 코니가 범위 벗어남 -> -1

"""
c, b = map(int, input().split())
cmove = set((c, 0))
i = 1
sec = 1
while c <= 200000:
    cmove.add((c+i, sec))
    i += 1
    c += i
    sec += 1

