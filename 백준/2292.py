# 가고자 하는 방의 모서리의 육각형 수 = 가는데 지나치는 방 수
room = int(input())

i = 1
cur = 1
while cur < room:
    i += 1
    cur = cur + (i - 1) * 6

print(i)