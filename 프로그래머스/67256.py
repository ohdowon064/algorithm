"""
문제

123
456
789
*0#

1. 왼손 *, 오른손 #에서 시작
2. 엄지는 상하좌우만 이동가능, 키패드 이동 한칸 = 거리 1
3. 좌측 1, 4, 7은 왼손, 우측 3, 6, 9는 오른손 사용
4. 가운데 2, 5, 8, 0은 가까운 손으로 사용
    -> 만약 거리 같을경우 오른, 왼손잡이 기준

알고리즘
1. 왼손 : 1,4,7
2. 오른손 : 3, 6, 9
3. 그 외 : 거리계산 후 선택, 같으면 손잡이 기준
"""

def solution(numbers, hand):
    left = {1, 4, 7}
    right = {3, 6, 9}

    # n에서 p까지의 거리
    dist = lambda n, p : sum(divmod(abs(n - p), 3))

    ans = ""
    lp, rp = 10, 12
    numbers = list(map(lambda x: 11 if x == 0 else x, numbers))

    for number in numbers:
        # 1, 4, 7인 경우
        if number in left:
            ans += "L"
            lp = number

        # 3, 6, 9인 경우
        elif number in right:
            ans += "R"
            rp = number

        # 2, 5, 8, 0인 경우
        else:
            l_dist = dist(number, lp)
            r_dist = dist(number, rp)

            # 왼손이 더 가까운 경우
            if l_dist < r_dist:
                ans += "L"
                lp = number

            # 오른손이 더 가까운 경우
            elif l_dist > r_dist:
                ans += "R"
                rp = number

            # 왼손잡이인 경우
            elif hand == "left":
                ans += "L"
                lp = number

            # 오른손잡이인 경우
            else:
                ans += "R"
                rp = number

    return ans

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
solution(numbers, hand)

# def solution(numbers, hand):
#     answer = ''
#     lastL, lastR = 10, 12
#
#     for n in numbers:
#         if n in [1, 4, 7]:
#             answer += 'L'
#             lastL = n
#         elif n in [3, 6, 9]:
#             answer += 'R'
#             lastR = n
#         else:
#             n = 11 if n == 0 else n
#             absL = abs(lastL - n)
#             absR = abs(lastR - n)
#             if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
#                 answer += 'R'
#                 lastR = n
#             elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
#                 answer += 'L'
#                 lastL = n
#             else:
#                 if hand == 'left':
#                     answer += 'L'
#                     lastL = n
#                 else:
#                     answer += 'R'
#                     lastR = n
#
#     return answer