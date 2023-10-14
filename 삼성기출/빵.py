from collections import deque

n, m = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
stores = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
banned_area = set()
direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
temp_banned_area = set()
t = 0
basecamp_set = {(i, j) for i in range(n) for j in range(n) if board[i][j] == 1}

def calc_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

class Person:
    def __init__(self, i, x, y, basecamp, store):
        self.i = i
        self.x = x
        self.y = y
        self.basecamp = basecamp
        self.store = store

    def __repr__(self):
        print(f'======{self.i}번째=====')
        print(f"현재 좌표: ({self.x}, {self.y})")
        print(f"베이스캠프: {self.basecamp}")
        print(f"편의점: {self.store}")
        print("=============")
        return "\n"



people: list[Person] = []
for i in range(m):
    person = Person(i + 1, -1, -1, (-1, -1), stores[i])
    people.append(person)

def find_my_basecamp(p: Person):
    basecamp_candidates = []
    for base_x, base_y in basecamp_set:
        q = deque()
        visited = {(base_x, base_y)}
        q.append((base_x, base_y, 0))

        while q:
            x, y, current_dist = q.popleft()
            if (x, y) == p.store and (x, y) not in banned_area:
                basecamp_candidates.append((base_x, base_y, current_dist))
                break

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if out_of_range(nx, ny) or (nx, ny) in banned_area or (nx, ny) in visited:
                    continue

                visited.add((nx, ny))
                q.append((nx, ny, current_dist + 1))

    basecamp_candidates.sort(key=lambda x: (x[2], x[0], x[1]))
    p.basecamp = basecamp_candidates[0][:-1]
    return p


def out_of_range(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def step1(p: Person):
    if out_of_range(p.x, p.y):
        return p

    for dx, dy in direction:
        nx, ny = p.x + dx, p.y + dy
        if out_of_range(nx, ny) or (nx, ny) in banned_area:
            continue
        if calc_dist(p.x, p.y, *p.store) > calc_dist(nx, ny, *p.store):
            p.x, p.y = nx, ny
    return p

def step2(p: Person):
    if (p.x, p.y) == p.store and (p.x, p.y) not in banned_area:
        temp_banned_area.add(p.store)
    return p

def step3(p: Person):
    if out_of_range(p.x, p.y) and t >= p.i:
        p = find_my_basecamp(p)
        basecamp_set.discard(p.basecamp)
        p.x, p.y = p.basecamp
        temp_banned_area.add(p.basecamp)
    return p


while True:
    t += 1
    # print(t, "분 순회입니다.@@@@@@@@@@@@@@@@")
    all_out = True
    for i in range(m):
        people[i] = step1(people[i])
        people[i] = step2(people[i])
        people[i] = step3(people[i])



        if (people[i].x, people[i].y) != people[i].store:
            all_out = False
        # print(people[i])
    banned_area |= temp_banned_area
    temp_banned_area = set()





    if all_out:
        break
# print(banned_area)
print(t)


