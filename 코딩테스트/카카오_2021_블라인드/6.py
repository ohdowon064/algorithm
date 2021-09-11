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
from itertools import chain
from collections import defaultdict

def solution(board, skill):
    c = len(board[0])
    city = list(chain.from_iterable(board))
    attack = defaultdict(int)

    for act, r1, c1, r2, c2, degree in skill:
        if act == 2:
            degree = -degree

        # for i in range(r1, r2+1):
        #     city[i*r + c1 : i*r + c2 + 1] = map(lambda x: x - degree, city[i*r + c1 : i*r + c2 + 1])
        city[r1 * c + c1: r2 * c + c2 + 1] = map(lambda x: x - degree, city[r1 * c + c1: r2 * c + c2 + 1])
        print(city)

    print(city)
    ans = len(list(filter(lambda x: x > 0, city)))

    print(ans)
    return ans



# board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
# skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

solution(board, skill)