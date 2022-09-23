n, m = map(int, input().split())
x, y, d = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(m)]
print(n, m)
print(x, y, d)
print(map)
# 0, 1, 2, 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit_count = 1
check_count = 0
while True:
    # 왼쪽 확인
    d = (d - 1) % 4
    nx, ny = x + dx[d], y + dy[d]

    # 갈 수 없거나 갔던 곳이면
    if nx < 0 or nx >= n or ny < 0 or ny >= m or map[nx][ny] != 0:
        # 아직 전부 확인 안함
        if check_count < 4:
            check_count += 1
            continue
        # 전부 다 확인
        else:
            check_count = 0
            # 뒤로 이동
            d = (d - 2) % 4
            nx, ny = x + dx[d], y + dy[d]
            # 뒤가 밖이거나 바다인경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m or map[nx][ny] == 1:
                break

            # 뒤로 이동
            x, y = nx, ny
            continue
    else:
        check_count = 0
        visit_count += 1
        x, y = nx, ny
        map[x][y] = -1

print(visit_count)