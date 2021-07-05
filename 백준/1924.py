"""
    1. 2007년 1월 1일 : 월요일
    2. 2007년 x월 y일은 무슨요일

    알고리즘
    1. 365일 -> 완전탐색
    2. 1월 1일 -> x월 y일 날짜차이 : k
    3. k % 7 요일

"""
x, y = map(int, input().split())

day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

days = 0
for month in range(1, x):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        days += 31
    elif month in {4, 6, 9, 11}:
        days += 30
    else:
        days += 28

days += y - 1

print(day[days % 7])