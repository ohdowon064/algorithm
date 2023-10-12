from collections import deque

n, m = map(int, input().split())
start_r, start_c, start_d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

north, east, south, west = 0, 1, 2, 3
clean_count = 0

# 0: 북, 1: 동, 2: 남, 3: 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def rotate_counterclockwise(d):
    return (d - 1) % 4


def forward(r, c, d):
    return r + dr[d], c + dc[d]


def backward(r, c, d):
    d = (d - 2) % 4
    return r + dr[d], c + dc[d]


def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= m


def can_clean(r, c):
    return not out_of_range(r, c) and board[r][c] == 0


def cannot_move(r, c):
    return out_of_range(r, c) or board[r][c] == 1


def clean(r, c):
    global clean_count
    board[r][c] = -1
    clean_count += 1


def bfs(r, c, d):
    q = deque()
    q.append((r, c))

    while q:
        r, c = q.popleft()
        if can_clean(r, c):
            clean(r, c)

        check_clean = 0
        while check_clean < 4:
            # 반 시계 회전
            d = rotate_counterclockwise(d)
            nr, nc = forward(r, c, d)
            if can_clean(nr, nc):
                # 앞쪽 칸 청소가능 -> 전진
                q.append((nr, nc))
                break
            check_clean += 1
        else:
            # 빈 칸 없음
            # 방향 유지하고 후진
            nr, nc = backward(r, c, d)
            # 뒤칸 벽이면 종료
            if cannot_move(nr, nc):
                return
            q.append((nr, nc))


bfs(start_r, start_c, start_d)
print(clean_count)
