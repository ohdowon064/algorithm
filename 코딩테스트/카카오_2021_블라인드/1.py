"""
문제
1. 한번 한명 유저 신고
2. 신고횟수 제한 x
    - 다른 유저 신고 가능
    - 같은 유저 여러번 -> 1회 처리
3. k번 이상 신고 -> 즉시 정지
    - 해당 유저 신고한 사람에게 정지 사실 알림
4. 정지 유저도 불량 이용자 신고 가능

id_list : 이용자 ID
report : 각 이용자가 신고한 ID
k : 정지 기준
"""
from collections import defaultdict


def solution(id_list, report, k):
    report_list = defaultdict(set)
    check_list = defaultdict(set)

    for r in report:
        a, b = r.split()
        report_list[b].add(a)
        check_list[a].add(b)

    print(report_list)
    print(check_list)

    block_list = set(filter(lambda x: len(report_list[x]) >= k, id_list))
    email_list = [len(check_list[id] & block_list) for id in id_list]
    print(email_list)

    return email_list


# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

solution(id_list, report, k)