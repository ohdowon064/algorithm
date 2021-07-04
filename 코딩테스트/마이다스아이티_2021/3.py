"""
    1. 상담 하루 1명
    2. 상담 소요시간 하루
    3. 재상담 불가
    4. 최대한 많은 학생 상담
    5. [a, b] : a ~ b일 중 아무날
    7.
"""

N = 6
K = 4
T = [ [1,3],[3,4],[2,4],[2,4],[2,3],[1,2] ]

# N = 5
# K = 6
# T = [[1, 1], [1, 6], [2, 5], [3, 4], [4, 4]]

# N = 5
# K = 6
# T = [[1, 1], [1, 6], [3, 4], [4, 4], [5, 5]]

day = 1
count = 0

T = sorted(T, key=lambda x: (x[0], x[1]))
i = 0
while i < len(T) - 1:
    if T[i][0] == T[i][1]:
        i += 1
        continue

    elif T[i+1][1] - T[i+1][0] < T[i][1] - T[i][0] and T[i+1][0] < T[i][1]:
        T[i], T[i+1] = T[i+1], T[i]

    i += 1

print(T)

for start, end in T:
    if end < day:
        continue

    if start > day:
        day = start

    if start <= day and day <= end:
        print(start, end, day)
        count += 1

    day += 1


print(count)


