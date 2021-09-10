"""
문제
1. 진도 100% -> 반영
2. progresses : 현재 작업된 기능개수, 배포 순서
3. speeds: i번째 progress의 기능당 작업 속도
4. 하루에 배포하는 개수 반환

알고리즘
1. 남은 진도 구함
2. 하루 작업량으로 나누고 올림
3. 이전 일보다 작으면 +1
"""
from math import ceil

def solution(progresses, speeds):
    end_days = [-((t - 100)//s) for t, s in zip(progresses, speeds)]

    ans = []
    count, max_day = 1, end_days[0]

    for i in range(len(end_days) - 1):
        if max_day >= end_days[i + 1]:
            count += 1
        else:
            ans.append(count)
            count, max_day = 1, end_days[i + 1]
    ans.append(count)

    return ans


progresses = [93, 30, 55]
speeds = [1, 30, 5]
solution(progresses, speeds)