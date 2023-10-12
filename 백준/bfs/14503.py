from collections import deque

north = 0
east = 1
south = 2
west = 3

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
clean_count = 0


# north 0-> west 3-> south 2-> east 1-> north
def rotate_counterclockwise(current_direction):
    return (current_direction - 1) % 4


def forward(r, c, d):
    if d == north: # 상
        return r + dr[0], c + dc[0]
    if d == east: # 우
        return r + dr[3], c + dc[3]
    if d == south: # 하
        return r + dr[1], c + dc[1]
    if d == west: # 좌
        return r + dr[2], c + dc[2]


def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= m


def backward(r, c, d):
    if d == north:
        return r + dr[1], c + dc[1]
    if d == east:
        return r + dr[2], c + dc[2]
    if d == south:
        return r + dr[0], c + dc[0]
    if d == west:
        return r + dr[3], c + dc[3]


n, m = map(int, input().split())
start_r, start_c, start_d = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(n)]


def clean(r, c):
    global clean_count
    maze[r][c] = -1
    clean_count += 1


def can_clean(r, c):
    return not out_of_range(r, c) and maze[r][c] == 0


def bfs(r, c, d):
    q = deque()
    q.append((r, c))

    while 1:
        # 현재 칸이 청소안됐으면 현재 칸 청소
        r, c = q.popleft()
        if can_clean(r, c):
            clean(r, c)

        # 4칸 확인
        clean_check = 0

        while clean_check < 4:
            # 반시계 회전
            d = rotate_counterclockwise(d)
            # 바라보는 방향 기준 앞쪽칸 청소 안됐으면
            nr, nc = forward(r, c, d)
            if can_clean(nr, nc):
                q.append((nr, nc))
                break
            # 청소 안되면 반시계 회전
            clean_check += 1
        else:
            # 빈칸 없으면 후진
            nr, nc = backward(r, c, d)
            if out_of_range(nr, nc) or maze[nr][nc] == 1:
                return
            q.append((nr, nc))


bfs(start_r, start_c, start_d)
print(clean_count)