n, m, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
people = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
exit_pos = list(map(lambda x: int(x) - 1, input().split()))
maze[exit_pos[0]][exit_pos[1]] = "*"

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def out_of_range(r, c):
    return r < 0 or r >= n or c < 0 or c >= n


def dist(ar, ac, br, bc):
    return abs(ar - br) + abs(ac - bc)


def rotate(board):
    return list(map(list, zip(*board[::-1])))

def rotate_sublist(ar, ac, br, bc):
    global exit_pos
    sublist = [row[ac: bc + 1] for row in maze[ar: br + 1]]
    sublist = rotate(sublist)
    for r in range(ar, br + 1):
        for c in range(ac, bc + 1):
            maze[r][c] = sublist[r - ar][c - ac]
            if maze[r][c] == "*":
                exit_pos = (r, c)
            elif maze[r][c] > 0:
                maze[r][c] -= 1

def find_square(xr, xc, yr, yc):
    length = max(abs(xr - yr), abs(xc - yc))
    xr, xc, yr, yc = min(xr, yr), min(xc, yc), max(xr, yr), max(xc, yc)

    nr, nc = yr - length, yc - length
    if out_of_range(nr, nc):
       return xr, xc, xr - length, xc - length, length
    return nr, nc, yr, yc, length

out = 0
people_dist = [0] * m
for _ in range(k):
    squares = []
    for i in range(m):
        r, c = people[i]
        if maze[r][c] == "*":
            continue

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if out_of_range(nr, nc) or (maze[nr][nc] != "*" and maze[nr][nc] > 0):
                continue

            if dist(r, c, *exit_pos) > dist(nr, nc, *exit_pos):
                people[i] = (nr, nc)
                people_dist[i] += 1
                break

        if maze[people[i][0]][people[i][1]] == '*':
            out += 1
            continue

        squares.append(find_square(*people[i], *exit_pos))

    if out == len(people):
        break

    squares.sort(key=lambda x: (x[-1], x[0], x[1]))
    rotate_sublist(*squares[0][:-1])

print(sum(people_dist))
for i in range(n):
    for j in range(n):
        if maze[i][j] == "*":
            print(i + 1, j + 1)
