# 나선이동
# 중심에서 시작하여 방향을 2번 바꿀 때마다 이동거리가 1씩 증가한다.
from pprint import pprint

n = 5
board = [[0] * n for _ in range(n)]

# 이동 방향: 좌, 하, 우, 상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

def spiral_move():
    r = c = n // 2 # 중앙 좌표
    direction = move_count = number = 0
    dist = 1

    while True:
        move_count += 1
        for _ in range(dist):
            nr, nc = r + dr[direction], c + dc[direction]

            # 종료조건: 이동 좌표가 마지막 좌표 도착한 경우
            # 좌하우상: (0, -1)
            if (nr, nc) == (0, -1):
                return
            number += 1
            board[nr][nc] = number

            r, c = nr, nc

        if move_count == 2:
            dist += 1
            move_count = 0

        direction = (direction + 1) % 4

spiral_move()
pprint(board)