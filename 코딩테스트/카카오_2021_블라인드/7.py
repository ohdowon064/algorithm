"""
문제
1. 패배
    1) 이동 할 수 없으면 패배
    2) 같은 발판에 있는데 상대가 먼저 이동
2. 상하좌우 이동
3. 이동 시 기존 발판 사라짐
4.
"""
from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

memo = defaultdict(int)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dp(board, aloc, bloc, order):
    n, m = len(board), len(board[0])
    if aloc[0] < 0 or aloc[1] >= n or bloc[0] < 0 or bloc[1] >= m:
        return 1

    cnt = memo[(aloc[0], aloc[1], bloc[0], bloc[1], order)]
    if cnt != 0:
        return cnt

    if order == 'A':
        for i in range(4):
            new_aloc = (aloc[0] + dx[i], aloc[1] + dy[i])
            cnt += dp(board, new_aloc, bloc, 'B')
    else:
        for i in range(4):
            new_bloc = (bloc[0] + dx[i], bloc[1] + dy[i])
            cnt += dp(board, aloc, new_bloc, 'A')

    return cnt

def solution(board, aloc, bloc):
    return dp(board, aloc, bloc, 'A')


board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]
solution(board, aloc, bloc)