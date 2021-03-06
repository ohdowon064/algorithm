"""
문제
1. 가로 w, 세로 h
2. 대각선을 따라 자름 -> 직각삼각형 2개
3. 1 * 1 정사각형으로 자를 때 사용할 수 있는 정사각형 개수

알고리즘
1억 이하 자연수 -> O(k) 시간복잡도로 계산해야함
1. 원래 정사각형 개수 w * h - 대각선이 지나가는 정사각형 수
2. 대각선이 지나가는 정사각형 -> ???
3. 둘 중 하나 1이면 0개
4. w == h이면 w 개
5. 더 하고 최대공약수만큼 뺀다 -> 어떻게? 걍 노가다로 규칙찾음
최대공약수 -> math.gcd
"""
from math import gcd

def solution(w, h):
    total = w * h
    useless = w + h - gcd(w, h)
    return total - useless