"""
    1. 상담 하루 1명
    2. 상담 소요시간 하루
    3. 재상담 불가
    4. 최대한 많은 학생 상담
    5. [a, b] : a ~ b일 중 아무날
    7.
"""
from itertools import permutations

N = 4
K = 4
T = [[1,3],[1,1],[2,2],[3,4]]
T = sorted(T, key=lambda x: (x[1] - x[0], x[0], x[1]))
max_count = 0
pre_count = 0

def dfs(rank, schedule, day, count):
    nonlocal max_count

    if day > K or rank == N:
        pre_count = max_count
        max_count= max(count, max_count)
        return

    start, end = schedule[rank]

    if start > day:
        day = start

    if start <= day and day <= end:
        count += 1
    else:
        return

    dfs(rank + 1, schedule, day + 1, count)


chk = 0
for schedule in permutations(T):
    if max_count == N:
        break
    if pre_count == max_count:
        chk += 1
    if chk > 10000000:
        break
    dfs(0, schedule, 1, 0)

print(max_count)