"""
    문제
    - 각 구간별
    - 백의 자리 밑 버림

    알고리즘
    1. 금액 -> 백의 자리 밑 버림
    2. threshold를 통해 세율 판단
    3. 징수 후 남은 금액
    4. months동안 반복
"""
# money = 12345678
# minratio = 10
# maxratio = 20
# ranksize = 250000
# threshold = 10000000
# months = 4

money = 1000000000
minratio = 50
maxratio = 99
ranksize = 100000
threshold = 0
months = 6

def tax(money):
    money = money // 100 * 100
    limit = maxratio - minratio
    if money < threshold:
        return 0

    for i in range(0, limit):
        if money < threshold + (i + 1) * ranksize:
            return (minratio + i) * money // 100

    return maxratio * money // 100

for _ in range(months):
    money -= tax(money)

print(money)