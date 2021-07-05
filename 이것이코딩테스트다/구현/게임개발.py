"""
    1. n * m 크기
    2. (x, y)
    3. 현재 위치에서 현재 방향 기준 왼쪽 방향부터 탐색
    4. 방문 칸 수 구하기

    탐색 방법
    1. 왼쪽 방문 x -> 좌회전 후 1칸 전진
    2. 왼쪽 방문 o -> 좌회전 후 1단계 수행
    3. 상하좌우 전부 방문 또는 바다이면 뒤로 한칸, 뒤 바다 -> 움직임 멈춤

    알고리즘
    1. 완전탐색
    2. 북서남동 : (-1, 0), (0, -1), (1, 0), (0, 1)
    3. 방향(북->서->남->동) : 0, 3, 2, 1
"""

n, m = map(int, input().split())
x, y, current_direct = map(int, input().split())
direct_order = [0, 3, 2, 1]
steps = {
    0: (-1, 0),
    3: (0, -1),
    2: (1, 0),
    1: (0, 1)
}
ans = 0

game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))

while True:
    if game_map[x][y] == 0:
        game_map[x][y] = '#'
        ans += 1

    can_move = False
    for _ in range(4):
        current_direct = (current_direct + 3) % 4
        nx = x + steps[current_direct][0]
        ny = y + steps[current_direct][1]

        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue

        if game_map[nx][ny] == 0:
            can_move = True
            x, y = nx, ny
            break

    if not can_move:
        next_direct = (current_direct + 2) % 4
        nx = x + steps[next_direct][0]
        ny = y + steps[next_direct][1]

        if nx < 0 or ny < 0 or nx >= m or ny > n or game_map[nx][ny] != 1:
            break

        x, y = nx, ny

print(ans)