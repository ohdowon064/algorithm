"""
문제
1. 작업 중요도
2. 처리 방식에 따라 작업 분류
3. 한 작업을 시작 시 끝까지
4. 같은 방식의 작업이 중간 또는 끝남과 동시에 들어오면 이어서 진행
5. 하나 끝나면 다음 중요도 높은 것
    -> 여러개 : 분류 번호 낮은 것
6. (요청시각, 작업시간, 분류번호, 작업중요도)


알고리즘
1. 힙큐
"""
import heapq

def solution(jobs):
    heap = [jobs[0]]

    t = i = 0
    while heap:
        time, hour, number, priority = heapq.heappop(heap)
        t = t + time + hour

        for