"""
문제
1. price: 이용료
2. 놀이기구 n번 이용 -> 이용료 n배
    ex) 처음 price 100, n == 2: price 200, n == 3: price 300
3. count번 탄 후, 금액에서 얼마 모자라는지 반환

알고리즘
1. 필요 = price + price * 2 + ... + price * count = price*count*(count + 1) / 2
2. if (이용료 > money) return 이용료 - money
    else return 0
"""

def solution(price, money, count):
    needs = price * count * (count + 1) / 2
    ans = needs - money if needs > money else 0
    return ans