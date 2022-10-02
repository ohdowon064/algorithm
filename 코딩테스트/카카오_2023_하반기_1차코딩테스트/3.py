"""
1. 가입자 최대 늘리기
2. 판매액 최대 늘리기

- n명에게 m개 할인 판매
- 할인율 10, 20, 30, 40% 중 하나

- 사용자는 이모티콘구매 또는 서비스가입
- 사용자 각 기준에 따라 일정비율 할인 이모티콘을 모두구매
- 사용자 이모티콘 구매비용 합이 일정가격 이상이면 구매 취소 후 서비스 가입

- 각 할인율 적용 후 최대값 반환
"""
from itertools import product


def member_or_purchase(user, emoticons, percents):
    total = 0
    for emoticon, percent in zip(emoticons, percents):
        if percent >= user[0]:
            total += emoticon * percent // 100

    return total >= user[1], total


def solution(users, emoticons):
    # cases = list(product([10, 20, 30, 40], repeat=len(emoticons)))
    max_members = max_sales = 0
    cases = [(30, 40)]
    for case in cases:
        members = sales = 0
        for user in users:
            is_member, total = member_or_purchase(user, emoticons, case)
            if is_member:
                members += 1
            else:
                sales += total
            if case == (30, 40):
                print(is_member, total)

    return max_members, max_sales

solution([[40, 10000], [25, 10000]], [7000, 9000])