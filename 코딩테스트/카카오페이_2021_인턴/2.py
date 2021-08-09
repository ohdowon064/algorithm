dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]

rows = 4
columns = 3
swipes = [[1,1,2,4,3]] # ,[3,2,1,2,3],[4,1,1,4,3],[2,2,1,3,3]]

data = [[0] * (columns + 1) for _ in range(rows + 1)]
k = 1
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        data[i][j] = k
        k += 1

print(data)

result = []
for d, r1, c1, r2, c2 in swipes:
    temp1, temp2 = 0, 0
    for x in range(r1, r2 + 1):
        for y in range(c1, c2 + 1):
            nx, ny = x + dx[d], y + dy[d]

            if nx >= r2 + 1:
                nx = r1
            elif nx < r1:
                nx = r2
            elif ny >= c2 + 1:
                ny = c1
            elif ny < c1:
                ny = c2

            temp1 = data[nx][ny]

            if x == r1:
                data[nx][ny] = data[x][y]
            else:
                data[nx][ny] = temp2

            temp2 = temp1


print(data)