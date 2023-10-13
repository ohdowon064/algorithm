n = int(input())
desert = [list(map(int, input().split())) for _ in range(n)]
# 좌하우상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n
"""
0  0 2 0
0 10 7 1
5  a y x
0 10 7 1
0  0 2 0

0 1 x 1 0
2 7 y 7 2
0 10 a 10 0
0 0 5 0 0

0 2 0 0
1 7 10 0
x y a 5
1 7 10 0
0 2 0 0

0 0 5 0 0
0 10 a 10 0
2 7 y 7 2
0 1 x 1 0
"""

out_of_desert = 0

def move_sand(xr, xc, yr, yc, d):
    global out_of_desert
    percents = {}
    if d == 0:
        percents[1] = [(yr - 1, yc + 1), (yr + 1, yc + 1)]
        percents[2] = [(yr - 2, yc), (yr + 2, yc)]
        percents[7] = [(yr - 1, yc), (yr + 1, yc)]
        percents[10] = [(yr - 1, yc - 1), (yr + 1, yc - 1)]
        percents[5] = [(yr, yc - 2)]
        pa = (yr, yc - 1)

    elif d == 1:
        percents[1] = [(yr - 1, yc - 1), (yr - 1, yc + 1)]
        percents[2] = [(yr, yc - 2), (yr, yc + 2)]
        percents[7] = [(yr, yc - 1), (yr, yc + 1)]
        percents[10] = [(yr + 1, yc - 1), (yr + 1, yc + 1)]
        percents[5] = [(yr + 2, yc)]
        pa = (yr + 1, yc)

    elif d == 2:
        percents[1] = [(yr - 1, yc - 1), (yr + 1, yc - 1)]
        percents[2] = [(yr - 2, yc), (yr + 2, yc)]
        percents[7] = [(yr - 1, yc), (yr + 1, yc)]
        percents[10] = [(yr - 1, yc + 1), (yr + 1, yc + 1)]
        percents[5] = [(yr, yc + 2)]
        pa = (yr, yc + 1)

    elif d == 3:
        percents[1] = [(yr + 1, yc - 1), (yr + 1, yc + 1)]
        percents[2] = [(yr, yc - 2), (yr, yc + 2)]
        percents[7] = [(yr, yc - 1), (yr, yc + 1)]
        percents[10] = [(yr - 1, yc - 1), (yr - 1, yc + 1)]
        percents[5] = [(yr - 2, yc)]
        pa = (yr - 1, yc)
    else:
        raise ValueError(f"direction is wrong: {d}")

    total = 0
    for percent, positions in percents.items():
        amount = int(desert[yr][yc] * percent / 100)

        for x, y in positions:
            total += amount
            if out_of_range(x, y):
                out_of_desert += amount
            else:
                desert[x][y] += amount

    rest = desert[yr][yc] - total
    if out_of_range(pa[0], pa[1]):
        out_of_desert += rest
    else:
        desert[pa[0]][pa[1]] += rest
    desert[yr][yc] = desert[xr][xc]

def spiral_move():
    r = c = n // 2
    direction = 0
    move_count = 0
    dist = 1

    while True:
        move_count += 1
        for _ in range(dist):
            nr, nc = r + dr[direction], c + dc[direction]
            if out_of_range(nr, nc):
                return

            move_sand(r, c, nr, nc, direction)
            r, c = nr, nc

        direction = (direction + 1) % 4

        if move_count == 2:
            dist += 1
            move_count = 0

spiral_move()
print(out_of_desert)