"""
문제
1. n을 k진수로 바꿀 떄 조건에 맞는 소수개수
    1) 0P0 처럼 양쪽에 0
    2) P0 처럼 소수 우측 0, 좌측 아무것도 없음
    3) 0P 처럼 소수 좌측 0, 우측 아무것도 없음
    4) P 처럼 좌우 아무것도 없음
    5) P는 각 자릿수에 0을 포함하지 않는 소수
        ex) 101은 가운데 0이 있으므로 소수 안됨

알고리즘
1. 일단 k 진수로 변환
2. 0으로 split
3. 1제거
"""
import re


def solution(n, k):
    result = ''

    while n > 0:
        n, q = divmod(n, k)
        result += str(q)

    prime_list = list(filter(lambda x: x != '', result[::-1].split('0')))

    def is_prime(n):
        if n == 1: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    ans = len(list(filter(lambda x: is_prime(int(x)), prime_list)))

    return ans


solution(437674, 3)
solution(110011, 10)