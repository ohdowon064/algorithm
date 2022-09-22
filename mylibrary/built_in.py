# sum
import math

sum([1, 2, 3, 4, 5])

# min, max
min(1, 2, 3, 4, 5)
max([7, 3, 4, 5])

# eval: 문자열의 수학식을 계산
eval("3 * (5 + 7)")

# sorted, sort
sorted([9, 1, 8, 5, 4])
sorted([9, 1, 8, 5, 4])

samples = [("A", 35), ("C", 75), ("D", 100), ("B", 54)]
sorted(samples, key=lambda x: x[1], reverse=True) # 숫자기준으로 내림차순 정렬

samples.sort(key=lambda x: x[1], reverse=True)

# itertools
# permutations - 순열
# combinations - 조합
# product - 중복순열, 데카르트곱
# combination_with_replacement - 중복조합
from itertools import permutations, combinations, product, combinations_with_replacement
data = ["A", "B", "C"]
print(list(permutations(data, 2)))
print(list(combinations(data, 2)))
print(list(product(data, repeat=2)))
print(list(product(["A", "B"], ["C", "D", "E"])))
print(list(combinations_with_replacement(data, 2)))

# heapq - 우선순위 큐
# 힙정렬
import heapq
def heapsort(iterable):
    heap = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(heap, value)

    # 힙에 삽입된 원소를 차례대로 꺼내어 담기
    for _ in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result

result = heapsort([1, 7, 3, 5, 2, 4, 6, 9, 8, 10])
print(result)

# 최대힙 -> heapq로 구현가능
def heapsort_by_descending(iterable):
    heap = []
    result = []

    for value in iterable:
        heapq.heappush(heap, -value)

    for _ in range(len(heap)):
        result.append(-heapq.heappop(heap))

    return result

print(heapsort_by_descending(result))

# bisect - 이진탐색, O(logN)
# bisect_left(a, x), bisect_right(a, x)
# 정렬 순서를 유지하며 리스트a에 데이터x를 삽입할 가장 왼쪽(오른쪽) 인덱스를 반환
from bisect import bisect_left, bisect_right

sample = [1, 2, 4, 4, 8]
print(bisect_left(sample, 4))
print(bisect_right(sample, 4))

# "정렬된 리스트"에서 "값이 특정범위에 속하는" 원소개수 구하기
def count_by_range(sorted_array, min_value, max_value):
    right_index = bisect_right(sorted_array, max_value)
    left_index = bisect_left(sorted_array, min_value)
    print(left_index, right_index)
    return right_index - left_index

# collections
# deque, Counter
from collections import deque, Counter
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
data.popleft()
data.pop()

counter = Counter(["A", "B", "C", "A", "A", "B"])
print(counter)

# math
print(math.factorial(5)) # 5!
print(math.sqrt(7)) # 7의 제곱근
print(math.gcd(21, 14)) # 21, 14의 최대공약수
# print(math.lcm(2, 5)) 2, 5의 최소공배수, python3.9부터 사용가능
print(math.pi, math.e) # 파이, 자연상수(e)