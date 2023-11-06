from pprint import pprint

n = 5
board = [[0] * n for _ in range(n)]

# 이동방향: 좌하우상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n

def spiral_move():
    r = c = n // 2
    dist = 1
    move_count = 0
    d = 0

    while True:
        move_count += 1
        for _ in range(dist):
            nr, nc = r + dr[d], c + dc[d]
            if out_of_range(nr, nc):
                return

            board[nr][nc] = board[r][c] + 1
            r, c = nr, nc

        d = (d + 1) % 4
        if move_count == 2:
            dist += 1
            move_count = 0

spiral_move()
pprint(board)

