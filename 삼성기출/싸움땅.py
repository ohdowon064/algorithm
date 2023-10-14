n, m, k = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

guns = {(i, j, board[i][j]) for i in range(n) for j in range(n) if board[i][j] > 0}

class Player:
    def __init__(self, i, x, y, d, s):
        self.i = i
        self.x = x
        self.y = y
        self.d = d
        self.s = s
        self.g = 0
        self.point = 0

    def __repr__(self):
        return f"{self.x} {self.y} {self.d} {self.s}"

    def fight(self, other: "Player") -> bool:
        if self.s + self.g > other.s + other.g:
            return True
        if self.s + self.g == other.s + other.g:
            return self.s > other.s
        return False


players = [
    Player(i, *list(map(int, input().split())))
    for i in range(m)
]

def out_of_range(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def step1(p: Player):
    d = p.d
    nx, ny = p.x + dx[d], p.y + dy[d]
    if not out_of_range(nx, ny):
        p.x, p.y = nx, ny

    d = (p.d + 2) % 4
    p.x, p.y = p.x + dx[d], p.y + dy[d]
    p.d = d

def is_there_player(i, x, y) -> Player:
    for player in players:
        if i != player.i and x == player.x and y == player.y:
            return player
    return None

def defeat(p: Player):
    x, y, d = p.x, p.y, p.d
    if p.g:
        guns.add((x, y, p.g))

    while True:
        nx, ny = x + dx[d], y + dy[d]
        if not out_of_range(nx, ny) and is_there_player(p.i, nx, ny) is None:
            p.x, p.y, p.d = nx, ny, d
            gun = strongest_gun(nx, ny)
            if gun:
                p.g = gun[2]
                guns.discard(gun)
        d = (d + 1) % 4

def victory(p: Player):
    gun = strongest_gun(p.x, p.y)
    if gun and gun[2] > p.g:
        guns.add((p.x, p.y, p.g))
        p.g = gun[2]
        guns.discard(gun)


def strongest_gun(x, y):
    guns_here = []
    for gun in guns:
        if x == gun[0] and y == gun[1]:
            guns_here.append(gun)
    guns_here.sort(key=lambda x: x[2])
    return guns_here[0] if guns_here else None


def step2(p: Player):
    x, y = p.x, p.y
    other = is_there_player(p.i, p.x, p.y)

    if other is None:
        gun = strongest_gun(x, y)
        if gun and gun[2] > p.g:
            guns.add((x, y, p.g))
            p.g = gun[2]
            guns.discard(gun)
        return

    win = p.fight(other)
    if win:
        p.point += p.s + p.g
        defeat(other)
        victory(p)
    else:
        other.point += other.s + other.g
        defeat(p)
        victory(other)



def simulate():
    for p in players:
        step1(p)
        step2(p)

for _ in range(k):
    simulate()

print(' '.join([str(p.point) for p in players]))
