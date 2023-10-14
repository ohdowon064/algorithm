from collections import deque
from pprint import pprint

n, m, k = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
rec = [[0] * m for _ in range(n)]

direction_for_laser = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_for_bomb = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
turn = 0
in_war = [[False] * m for _ in range(n)]

class Turret:
    def __init__(self, x, y, r, p):
        self.x = x
        self.y = y
        self.r = r
        self.p = p

live_turret = []


def awake():
    live_turret.sort(key=lambda x: (x.p, -x.r, -(x.x + x.y), -x.y))
    weak_turret = live_turret[0]
    x = weak_turret.x
    y = weak_turret.y
    board[x][y] += n + m
    rec[x][y] = turn
    weak_turret.p = board[x][y]
    weak_turret.r = rec[x][y]
    in_war[x][y] = True
    live_turret[0] = weak_turret

def laser_attack():
    weak_turret = live_turret[0]
    sx = weak_turret.x
    sy = weak_turret.y
    power = weak_turret.p

    strong_turret = live_turret[-1]
    ex = strong_turret.x
    ey = strong_turret.y

    q = deque()
    visited = {(sx, sy)}
    q.append((sx, sy, []))
    path = []

    while q:
        x, y, _path = q.popleft()
        if x == ex and y == ey:
            path = _path
            break

        for dx, dy in direction_for_laser:
            nx, ny = (x + dx) % n, (y + dy) % m
            if board[nx][ny] == 0 or (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            q.append((nx, ny, _path + [(nx, ny)]))

    if path:
        for x, y in path:
            if x == ex and y == ey:
                damage = power
            else:
                damage = power // 2
            board[x][y] = max(0, board[x][y] - damage)
            in_war[x][y] = True

    return bool(path)

def bomb_attack():
    weak_turret = live_turret[0]
    sx = weak_turret.x
    sy = weak_turret.y
    power = weak_turret.p

    strong_turret = live_turret[-1]
    ex = strong_turret.x
    ey = strong_turret.y

    for dx, dy in direction_for_bomb:
        nx, ny = (ex + dx) % n, (ey + dy) % m

        if nx == sx and ny == sy or board[nx][ny] == 0:
            continue

        if nx == ex and ny == ey:
            board[nx][ny] = max(0, board[nx][ny] - power)
        else:
            board[nx][ny] = max(0, board[nx][ny] - power // 2)
        in_war[nx][ny] = True

def repair():
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and not in_war[i][j]:
                board[i][j] += 1

for _ in range(k):
    live_turret = []
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                new_turret = Turret(i, j, rec[i][j], board[i][j])
                live_turret.append(new_turret)


    if len(live_turret) <= 1:
        break

    turn += 1
    for i in range(n):
        for j in range(m):
            in_war[i][j] = False

    awake()
    if not laser_attack():
        bomb_attack()
    repair()

print(max([max(row) for row in board]))