"""
    1. 회의실 N개
    2. 회의 I : 시작시간, 끝 시간

    알고리즘
    1. 끝 시각으로 오름차순 정렬
    2. 시작 시각으로 오름차순 정렬
    3. 회의가능(시작시각이 현재시각보다 크거나 같다)하면 +1

    주의
    => 끝 시각으로 먼저 정렬해야 한다.
    why? 빨리 끝나야 뒤에 진행할 수 있는 회의가 많기 때문이다.
    시작 시각으로 먼저 정렬하면 늦게 끝났을 경우 진행할 수 있는 회의가 오히려 더 적다.
"""
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[1], x[0]))
time = 0
ans = 0

for meet in data:
    if time <= meet[0]:
        ans += 1
        time = meet[1]

print(ans)