from collections import deque

n, m, k = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

records = [[0] * m for _ in range(n)]
in_war = [[False] * m for _ in range(n)]
live_turret = []
direction_for_laser = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_for_bomb = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
turn = 0


class Turret:
    def __init__(self, x, y, record, power):
        self.x = x
        self.y = y
        self.record = record
        self.power = power


def select_attacker():
    live_turret.sort(key=lambda x: (x.power, -x.record, -(x.x + x.y), -x.y))
    weak_turret = live_turret[0]
    attack_x, attack_y = weak_turret.x, weak_turret.y
    board[attack_x][attack_y] += n + m
    records[attack_x][attack_y] = turn
    weak_turret.power = board[attack_x][attack_y]
    weak_turret.record = records[attack_x][attack_y]
    in_war[attack_x][attack_y] = True
    live_turret[0] = weak_turret


def laser_attack():
    attacker = live_turret[0]
    defender = live_turret[-1]
    sx, sy = attacker.x, attacker.y
    power = attacker.power
    ex, ey = defender.x, defender.y

    q = deque()
    q.append((sx, sy, []))
    visited = {(sx, sy)}
    path = []

    while q:
        x, y, current_path = q.popleft()
        if x == ex and y == ey:
            path = current_path
            break

        for dx, dy in direction_for_laser:
            nx, ny = (x + dx) % n, (y + dy) % m

            if board[nx][ny] == 0 or (nx, ny) in visited:
                continue

            visited.add((nx, ny))
            q.append((nx, ny, current_path + [(nx, ny)]))

    if path:
        for x, y in path:
            if x == ex and y == ey:
                board[x][y] = max(0, board[x][y] - power)
            else:
                board[x][y] = max(0, board[x][y] - power // 2)
            in_war[x][y] = True

    return bool(path)


def bomb_attack():
    attacker = live_turret[0]
    defender = live_turret[-1]
    sx, sy = attacker.x, attacker.y
    power = attacker.power
    ex, ey = defender.x, defender.y

    for dx, dy in direction_for_bomb:
        nx, ny = (ex + dx) % n, (ey + dy) % m
        if board[nx][ny] == 0 or (nx == sx and ny == sy):
            continue
        if nx == ex and ny == ey:
            board[nx][ny] = max(0, board[nx][ny] - power)
        else:
            board[nx][ny] = max(0, board[nx][ny] - power // 2)
        in_war[nx][ny] = True


def repair():
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and not in_war[i][j]:
                board[i][j] += 1


for _ in range(k):
    live_turret = []
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                live_turret.append(
                    Turret(i, j, records[i][j], board[i][j])
                )

    if len(live_turret) <= 1:
        break

    turn += 1
    in_war = [[False] * m for _ in range(n)]

    select_attacker()
    if not laser_attack():
        bomb_attack()
    repair()

print(max([max(row) for row in board]))
