"""
문제
1. orders : 각 손님들의 주문메뉴
2. course : 각 수에 맞는 최대 공통부분
    -> 최소 2명이상 공통
3. 여러개이면 전부 담는다.
4. 오름차순

알고리즘
1. 조합
2. 모든 경우의 수 배열 생성
3. Counter
4. 가장 많은 것 찾음
"""
from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = []
    # 각 course에 대해서 반복
    for n in course:
        # 각 orders에 대해서 개수에 해당하는 조합 탐색
        total = []
        cnt = 0
        for order in orders:
            case = list(map(''.join, map(sorted, combinations(order, n))))
            if len(case) < 1:
                continue

            cnt += 1
            total.extend(case)

        # 각 조합의 손님수 체크 -> 2 미만이면 break
        if cnt < 2:
            continue

        # 모든 경우의 수에 대해서 Counter
        common = Counter(total).most_common()
        max_common = max(common, key=lambda x: x[1])[1]

        if max_common < 2:
            continue

        menu = list(zip(*filter(lambda x: x[1] == max_common, common)))[0]
        print(menu)

        ans.extend(list(menu))

    return sorted(ans)


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
solution(orders, course)