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
    job_remain = list(map(lambda x: 100 - x, progresses))
    process_time = [ceil(job_remain[i]/speeds[i]) for i in range(len(speeds))]

    ans = []
    count = 1
    max_time = process_time[0]

    for i in range(len(process_time) - 1):
        if max_time >= process_time[i + 1]:
            count += 1
        else:
            ans.append(count)
            max_time = process_time[i + 1]
            count = 1
    ans.append(count)

    print(ans)

progresses = [1, 2, 1]
speeds = [98, 97, 5]
solution(progresses, speeds)