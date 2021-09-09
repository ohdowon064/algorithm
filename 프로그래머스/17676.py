"""
문제
1. 초당 최대 처리량 : 응답 관계없이 1초간 처리하는 요청 최대개수
2. lines : n개의 로그 문자열
3. 로그문자열 : 응답완료시간 S, 처리시간 T, 공백으로 구분
4. S예시) 2016-09-15 hh:mm:ss.sss
5. T는 소수점 셋째자리까지 기록, s로 끝남
6. T예시) 0.011s
7. 처리시간은 시작시간, 끝시간 포함
8. 예시
    2016-09-15 03:10:33.020 0.011s
    -> 33.010부터 33.020까지 0.011초동안 처리
9. 타임아웃은 3초 : 0.001 <= T <= 3.000

알고리즘
1. 시작시간 순으로 정렬
2. 시작시간 부터 1초동안 가장 많은 것
"""
from datetime import datetime, timedelta, time

def solution(lines):

    logs = []
    for log in lines:
        s, t = log.lstrip("2016-09-15").split()

        process = float(t.replace('s', '')) - 0.001
        process_time = timedelta(seconds=process)

        end_time = datetime.strptime(s, "%H:%M:%S.%f")
        start_time = end_time - process_time

        logs.append((start_time, end_time))

    logs.sort(key=lambda x: x[0])
    end = None
    start = None
    one_sec = timedelta(seconds=0.999)
    time_filter = lambda x: end >= x[0] and start < x[1]
    cnt = -1
    for start_time, end_time in logs:
        end = start_time + one_sec
        start = start_time
        cnt = max(cnt, len(list(filter(time_filter, logs))))

    return cnt


lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))