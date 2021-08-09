rows = 4
columns = 3
swipes = [[1,1,2,4,3],[3,2,1,2,3],[4,1,1,4,3],[2,2,1,3,3]]

data = [[0] * (columns + 1) for _ in range(rows + 1)]
k = 1
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        data[i][j] = k
        k += 1

print(data)

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
result = 0
ans = []

def f_row(d, r1, c1, r2, c2):
    result = 0
    for y in range(c1, c2 + 1):
        for x in range(r1, r2 + 1):
            nx, ny = x + dx[d], y + dy[d]

            if nx < 0:
                nx = r2
                result += temp2
            if nx >= r2 + 1:
                nx = r1
                result += temp2

            temp1 = data[nx][ny]

            if x == r1:
                data[nx][ny] = data[x][y]
            else:
                data[nx][ny] = temp2

            temp2 = temp1
    return result

def f_col(d, r1, c1, r2, c2):
    result = 0
    for x in range(r1, r2 + 1):
        for y in range(c1, c2 + 1):
            nx, ny = x + dx[d], y + dy[d]

            if ny < 0:
                ny = c2
                result += temp2
            if ny >= c2 + 1:
                ny = c1
                result += temp2

            temp1 = data[nx][ny]

            if y == c1:
                data[nx][ny] = data[x][y]
            else:
                data[nx][ny] = temp2

            temp2 = temp1
    return result

for d, r1, c1, r2, c2 in swipes:
    if d == 1 or d == 2:
        ans.append(f_row(d, r1, c1, r2, c2))
    else:
        ans.append(f_col(d, r1, c1, r2, c2))

print(ans)