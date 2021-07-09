"""
    문제
    1. 수빈 N, 동생 K
    2. 걷기 : 1초 후 x-1, x+1
    3. 순간이동 : 1초 후 2*x
    4. 동생 찾는 가장 빠른 시간

    알고리즘
    1. n - k 거리계산
    2. x-1, x+1, 2*x bfs
"""
from collections import deque

n, k = map(int, input().split())
MAX = 100000

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        if x == k:
            return

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and time[nx] == 0:
                q.append(nx)
                time[nx] = time[x] + 1

time = [0] * (MAX + 1)
bfs(n)
print(time[k])
