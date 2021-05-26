# 45분전 시각구하기
h, m = map(int, input().split())
h = h if h > 0 else 24

t = h * 60 + m - 45
alarm_h, alarm_m = divmod(t, 60)
print(alarm_h, alarm_m)