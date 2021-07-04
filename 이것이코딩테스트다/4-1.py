# N = int(input())
# move = input().split()
# x, y = 0, 0
#
# for m in move:
#     if m == 'R' and y < 4:
#         y += 1
#     elif m == 'L' and y > 0:
#         y -= 1
#     elif m == 'U' and x > 0:
#         x -= 1
#     elif m == 'D' and x < 4:
#         x += 1
# print(x + 1, y + 1)

n = int(input())
plans = input().split()

x, y = 1, 1
# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)