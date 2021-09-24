"""
문제
1. n * m
2. 각 칸마다 내구도
3. 공격 : 내구도 0 이하면 파괴
4. 회복 : 내구도 회복
5. 파괴되지않은 건물 수
6. board : 행렬
7. skill
    [공격/회복, r1, c1, r2, c3, 정도]
"""
from collections import defaultdict
from time import time


def solution(board, skill):
    attack = defaultdict(int)

    for act, r1, c1, r2, c2, degree in skill:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                attack[(r, c)] += degree * ((-1) ** act)

    for i, j in attack.keys():
        board[i][j] -= attack[(i, j)]

    ans = 0
    for row in board:
        ans += len(list(filter(lambda x: x > 0, row)))

    return ans



board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

# board = [[1,2,3],[4,5,6],[7,8,9]]
# skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

solution(board, skill)

def solution(board, skill):
    answer = 0
    for s in skill :
        t, r1, c1, r2, c2, degree = s
        for i in range(r1, r2 + 1) :
            for j in range(c1, c2 + 1) :
                    board[i][j] = board[i][j] + degree * ((-1)**t)

    for b in board :
        for e in b :
            if e > 0 :
                answer = answer+1
    return answer