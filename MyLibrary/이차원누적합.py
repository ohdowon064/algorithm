from random import randint
from pprint import pprint as pp
from typing import List

arr = [[randint(1, 100) for j in range(10)]
       for i in range(100)]

arr = [[0, 1, 1, 0, 0, 1],
       [0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 1]]

def get_sum_list(arr: List[List]):
    # 먼저 행의 합을 구한다.
    sum_list = [[sum(arr[i][:j + 1]) for j in range(len(arr[0]))]
                for i in range(len(arr))]

    # 열의 합을 구한다.
    for i in range(len(sum_list) - 1):
        for j in range(len(sum_list[0])):
            sum_list[i + 1][j] += sum_list[i][j]

    return sum_list

sum_list = get_sum_list(arr)
print(sum_list)

# sum_list를 S라 할 때, 꼭짓점 list(x1, y1) ~ list(x2, y2)의 구역합 구하기
# S(x2, y2) - {S(x1, y2) + S(x2, y1)} + S(x1, y1)

def accum(S: List[List], x1: int, y1: int, x2: int, y2: int) -> int:
    return S[x2][y2] - (S[x1][y2] + S[x2][y1]) + S[x1][y1]

print(accum(sum_list, 0, 1, 2, 4))
