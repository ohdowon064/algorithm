"""
    고정비용 : A
    가변비용 : B
    노트북가격 : C
    C > A + B가 되는 손익분기점 구하기
"""
fixed, variable, price = map(int, input().split())
profit = price - variable

print(-1 if profit <= 0 else fixed // profit + 1)
