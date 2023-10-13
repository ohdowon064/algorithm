# 2차원 배열 회전
# 직사각형 회전
# 부분배열 회전
from pprint import pprint

n = 5
board = [[i * n + j for j in range(1, n + 1)] for i in range(n)]

def transpose():
    return list(map(list, zip(*board)))

def rotate(clockwise=True):
    if clockwise:
        return list(map(list, zip(*board[::-1])))
    return transpose()[::-1]

pprint(transpose())
pprint(rotate())
pprint(rotate(clockwise=False))