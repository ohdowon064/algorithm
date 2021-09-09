"""
문제
1. 반복되는 문자열의 개수로 압축
2. 반복 문자열 길이단위
3. 가장 짧은 압축 문자열

알고리즘
1. 1개 문자 존재하는지 체크
    -> 무조건 문자열 길이가 최소길이
2. 
"""
from collections import Counter

def solution(s):
    if Counter(s).most_common()[-1][1] == 1:
        return len(s)


