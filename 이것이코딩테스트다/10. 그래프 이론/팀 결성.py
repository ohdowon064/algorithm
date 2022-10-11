"""
입력값
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""

n, m = map(int, input().split())

team = [i for i in range(n + 1)]


def find_team(x):
    if team[x] != x:
        team[x] = find_team(team[x])
    return team[x]


def union_team(x, y):
    x_team = find_team(x)
    y_team = find_team(y)

    if x_team < y_team:
        team[y_team] = x_team
    else:
        team[x_team] = y_team


for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union_team(a, b)
    elif find_team(a) == find_team(b):
        print("YES")
    else:
        print("NO")
