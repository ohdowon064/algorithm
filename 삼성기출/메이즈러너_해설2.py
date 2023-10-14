n, m, k = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp_board = [[0] * n for _ in range(n)]
people = [
    tuple(map(lambda x: int(x) - 1, input().split()))
    for _ in range(m)
]
exits = tuple(map(lambda x: int(x) - 1, input().split()))
ans = sx = sy = square_size = 0


def move_people():
    global exits, ans

    for i in range(m):
        if people[i] == exits:
            continue

        px, py = people[i]
        ex, ey = exits

        if px != ex:
            nx, ny = px, py

            if ex > nx:
                nx += 1
            else:
                nx -= 1

            if not board[nx][ny]:
                people[i] = (nx, ny)
                ans += 1
                continue

        if py != ey:
            nx, ny = px, py

            if ey > ny:
                ny += 1
            else:
                ny -= 1

            if not board[nx][ny]:
                people[i] = (nx, ny)
                ans += 1
                continue


def find_minimum_square():
    global exits, sx, sy, square_size
    ex, ey = exits

    for size in range(2, n + 1):
        for x1 in range(n - size + 1):
            for y1 in range(n - size + 1):
                x2, y2 = x1 + size - 1, y1 + size - 1

                if not (x1 <= ex <= x2 and y1 <= ey <= y2):
                    continue

                for i in range(m):
                    px, py = people[i]
                    if x1 <= px <= x2 and y1 <= py <= y2:
                        if not (px == ex and py == ey):
                            sx, sy = x1, y1
                            square_size = size
                            return



# 정사각형 내부의 벽을 회전시킵니다.
def rotate_square():
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            if board[x][y]:
                board[x][y] -= 1

    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            temp_x, temp_y = x - sx, y - sy
            rotate_x, rotate_y = temp_y, square_size - temp_x - 1
            temp_board[rotate_x + sx][rotate_y + sy] = board[x][y]

    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            board[x][y] = temp_board[x][y]


# 모든 참가자들 및 출구를 회전시킵니다.
def rotate_traveler_and_exit():
    global exits

    for i in range(m):
        px, py = people[i]
        if sx <= px < sx + square_size and sy <= py < sy + square_size:
            temp_x, temp_y = px - sx, py - sy
            rotate_x, rotate_y = temp_y, square_size - temp_x - 1
            people[i] = (rotate_x + sx, rotate_y + sy)

    ex, ey = exits
    temp_x, temp_y = ex - sx, ey - sy
    rotate_x, rotate_y = temp_y, square_size - temp_x - 1
    exits = (rotate_x + sx, rotate_y + sy)


for _ in range(k):
    move_people()
    is_all_escaped = True
    for i in range(m):
        if people[i] != exits:
            is_all_escaped = False

    if is_all_escaped:
        break

    find_minimum_square()
    rotate_square()
    rotate_traveler_and_exit()

print(ans)

ex, ey = exits
print(ex + 1, ey + 1)
