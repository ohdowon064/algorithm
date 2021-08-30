"""
문제
1. 지워진 번호 : 0
2. 최고 순위, 최저 순위
3. 6개 선택 -> 6개 ~ 0개 맞추는 순으로 1등 ~ 낙첨(6등)

알고리즘
1. 최소 맞춘 개수 -> 최저 순위
2. 없는 번호 추가 -> 최고 순위
"""

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

rank = [6, 6, 5, 4, 3, 2, 1]
win_nums = set(win_nums)
min_cnt = len(list(filter(lambda x: x in win_nums, lottos)))
max_cnt = min(min_cnt + lottos.count(0), 6)

print(rank[max_cnt], rank[min_cnt])
