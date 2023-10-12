from pprint import pprint

n, m, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
persons = [list(map(int, input().split())) for _ in range(m)]
goal = list(map(int, input().split()))

# 1. 출구 쪽으로 이동하는 함수
# 2. 미로를 한바퀴 돌리는 함수
# 3. 내구도를 깎는 함수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not can_move(nx, ny):
            continue
        if should_move(x, y, nx, ny):
            return nx, ny
    return x, y


def can_move(x, y) -> bool:
    return 1 <= x <= n and 1 <= y <= n and maze[x-1][y-1] == 0

def should_move(x, y, nx, ny) -> bool:
    if dist(nx, ny, goal[0], goal[1]) < dist(x, y, goal[0], goal[1]):
        return True
    return False

def is_exit(x, y) -> bool:
    return x == goal[0] and y == goal[1]

def dist(x1, y1, x2, y2) -> int:
    return abs(x1-x2) + abs(y1 - y2)


def find_square():
    def square(x, y) -> int:
        return max(abs(x - goal[1]), abs(y - goal[0]))

    squares = []
    for person in persons:
        l = square(person[0], person[1])
        if l != 0:
            squares.append((l, person))
    squares.sort(key=lambda x: (x[0], x[1][0], x[1][1]))

    l, person = squares[0]
    x_min = min(person[0], goal[0])
    y_min = min(person[1], goal[1])
    x_max = x_min + l
    y_max = y_min + l
    return x_min, y_min, x_max, y_max

def rotate_coords(x1, y1, x2, y2):
    def rotate_coord(x, y):
        return y, n + 1 - x

    for person in persons:
        if x1 <= person[0] <= x2 and y1 <= person[1] <= y2:
            person[1], person[0] = rotate_coord(person[1], person[0])
    goal[1], goal[0] = rotate_coord(goal[1], goal[0])


def rotate_maze(x1, y1, x2, y2):
    partial_maze = maze[x1-1:x2]
    partial_maze = [row[y1-1:y2] for row in partial_maze]
    print(partial_maze)

    reversed_maze = partial_maze[::-1]
    rotated_maze = [[row[i] for row in reversed_maze] for i in range(len(reversed_maze[0]))]
    for i in range(x1, x2):
        for j in range(y1, y2):
            maze[i - 1][j - 1] = rotated_maze[i - x1][j - y1]
            if maze[i - 1][j - 1] > 0:
                maze[i - 1][j - 1] -= 1

def solve():
    result = 0
    out = [False] * m
    for _ in range(k):
        for i, person in enumerate(persons):
            if out[i]:
                continue
            nx, ny = move(person[0], person[1])
            if nx != person[0] or ny != person[1]:
                person[0], person[1] = nx, ny
                result += 1
            if is_exit(ny, nx):
                out[i] = True

        if all(out):
            return result

        print(_ + 1, "번째")
        square = find_square()
        x1, y1, x2, y2 = square
        print("square 좌표", x1, y1, x2, y2)
        rotate_maze(x1, y1, x2, y2)
        rotate_coords(x1, y1, x2, y2)
        print("goal 좌표", goal)
        pprint(maze)
        pprint(persons)
        print()

    return result

print(solve(), goal)
