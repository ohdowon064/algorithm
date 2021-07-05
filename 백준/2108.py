"""
    문제
    1. 산술평균 : N개 합 / N
    2. 중앙값 : N개 수 오름차순 시 중앙위치 값
    3. 최빈값 : 가장 많이 출현하는 값
    4. 범위 : 최댓값 - 최솟값

    조건
    입력
    1. 1 <= N <= 500000
    2. N은 홀수
    3. 정수 절대값 <= 4000

    출력
    1. 산술평균, 소수점 첫째자리에서 반올림 round()
    2. 중앙값
    3. 최빈값, 여러개 -> 두번째로 작은 값
    4. 범위
"""
from collections import Counter
import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
number_list = list(set(numbers))

# 산술평균
math_avg = round(sum(numbers) / n)

# 중앙값
mid_avg = sorted(numbers)[n//2]

# 최빈값
freq = Counter(numbers)
max_count = freq.most_common(1)[0][1]
freq_list = sorted(filter(lambda x: freq[x] == max_count, freq.keys()))
freq_avg = freq_list[1] if len(freq_list) > 1 else freq_list[0]

# 범위
range_avg = max(numbers) - min(numbers)

print(math_avg)
print(mid_avg)
print(freq_avg)
print(range_avg)

