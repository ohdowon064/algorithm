"""
문제
1. 어피치 n발 후 라이언 n발
2. 점수계산
    1) 가장 작은 원 10점, 차례대로 원 바깥 0점
        10 9 8 7 6 5 4 3 2 1 0
    2) k점 어피치 a발, 라이언 b발
        -> a > b 또는 a == b : 어피치가 k점 (k * a점 아님!!!!)
        -> a < b : 라이언 k점
    3) 모든 과녁에 대해 각 선수의 최종 점수 계산
3. 최종 점수 높은 선수 우승
    -> 같으면 어피치 우승
4. 어피치가 n발 쏜 상태일 때, 가장 큰 점수차로 이기기 위한 과녁 점수
5. n : 화살개수
6. info : 어피치 과녁 점수 당 맞춘 화살개수 리스트
7. 무조건 지거나 비김 -> [-1] 리턴
8. 여러개 -> 더 낮은 점수 많이 맞춘 것 리턴

알고리즘
1. 중복조합
"""
from itertools import combinations_with_replacement as H

def solution(n, info):
    target = list(range(11))

    cases = list(H(target, n))
    can_win = set()

    def calc_score(ryan, apeach = info[::-1]):
        ryan_score = 0
        apeach_score = 0
        for point in target:
            if apeach[point] != 0 or point in ryan:
                if ryan.count(point) > apeach[point]:
                    ryan_score += point
                else:
                    apeach_score += point

        return ryan_score - apeach_score

    for case in cases:
        if (diff := calc_score(case)) > 0:
            can_win.add((case, diff))

    # max_score = max(list(zip(*can_win))[1])
    # print(list(filter(lambda x: x[1] == max_score, list(can_win))))

    if not can_win:
        return [-1]

    winner = max(can_win, key=lambda x: (x[1], -min(x[0]), x[0].count(min(x[0]))))
    print(winner)

    ryan = [0 for _ in range(11)]
    for score in winner[0]:
        ryan[10 - score] += 1

    print(ryan)
    return ryan

# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]

# n = 1
# info = [1,0,0,0,0,0,0,0,0,0,0]

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]

solution(n, info)