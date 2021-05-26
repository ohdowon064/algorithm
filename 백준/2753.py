# 윤년 : (4의 배수 그리고 !(100의 배수)) || 400의 배수

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(1)
else:
    print(0)