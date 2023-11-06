n, m, k = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]




class Player:
    __slots__ = ["i", "x", "y", "d", "s", "g", "gi", "point"]

    def __init__(self, i, x, y, d, s):
        self.i = i
        self.x = x - 1
        self.y = y - 1
        self.d = d
        self.s = s
        self.g = 0
        self.gi = -1
        self.point = 0

    def __repr__(self):
        return f"{self.x} {self.y} {self.d} {self.s} {self.i}"

    def fight(self, other: "Player") -> bool:
        if self.s + self.g > other.s + other.g:
            return True
        if self.s + self.g == other.s + other.g:
            return self.s > other.s
        return False

class Gun:
    __slots = ["x", "y", "g", "gi"]

    def __init__(self, x, y, g, gi):
        self.gi = gi
        self.x = x
        self.y = y
        self.g = g

    def __hash__(self):
        return hash((self.x, self.y, self.g, self.gi))

    def __eq__(self, other):
        return (self.x, self.y, self.g, self.gi) == (other.x, other.y, other.g, other.gi)


players = [
    Player(i, *list(map(int, input().split())))
    for i in range(m)
]

gun_i = 0
guns = set()
for i in range(n):
    for j in range(n):
        guns.add(Gun(i, j, board[i][j], gun_i))
        gun_i += 1

def out_of_range(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def step1(p: Player):
    d = p.d
    nx, ny = p.x + dx[d], p.y + dy[d]
    if not out_of_range(nx, ny):
        p.x, p.y = nx, ny
        return

    d = (p.d + 2) % 4
    p.x, p.y = p.x + dx[d], p.y + dy[d]
    p.d = d

def is_there_player(i, x, y) -> Player | None:
    for p in players:
        if i != p.i and x == p.x and y == p.y:
            return p
    return None

def defeat(p: Player):
    x, y, d = p.x, p.y, p.d
    if p.g:
        gun = Gun(p.x, p.y, p.g, p.gi)
        guns.add(gun)
        p.g = 0

    while True:
        nx, ny = x + dx[d], y + dy[d]
        if not out_of_range(nx, ny) and is_there_player(p.i, nx, ny) is None:
            p.x, p.y, p.d = nx, ny, d
            gun = strongest_gun(nx, ny)
            if gun:
                p.g = gun.g
                p.gi = gun.gi
                guns.discard(gun)
            return
        d = (d + 1) % 4

def victory(p: Player):
    gun = strongest_gun(p.x, p.y)
    if gun and gun.g > p.g:
        prev_gun = Gun(p.x, p.y, p.g, p.gi)
        guns.add(prev_gun)
        p.g = gun.g
        p.gi = gun.gi
        guns.discard(gun)


def strongest_gun(x, y) -> Gun | None:
    guns_here: list[Gun] = []
    for gun in guns:
        if x == gun.x and y == gun.y:
            guns_here.append(gun)
    guns_here.sort(key=lambda gun: gun.g)
    return guns_here[0] if guns_here else None


def step2(p: Player):
    x, y = p.x, p.y
    other = is_there_player(p.i, x, y)

    if other is None:
        gun = strongest_gun(x, y)
        if gun and gun.g > p.g:
            prev_gun = Gun(p.x, p.y, p.g, p.gi)
            guns.add(prev_gun)
            p.g = gun.g
            p.gi = gun.gi
            guns.discard(gun)
        return

    win = p.fight(other)
    if win:
        p.point += (p.s + p.g) - (other.s + other.g)
        defeat(other)
        victory(p)
    else:
        other.point += (other.s + other.g) - (p.s + p.g)
        defeat(p)
        victory(other)



def simulate():
    for i, p in enumerate(players, 1):
        step1(p)
        step2(p)
        # print(i, "번째@@@@@")
        # print(p)


for _ in range(k):
    # print()
    # print(_+1, "라운드########")
    simulate()

print(' '.join([str(p.point) for p in players]))
