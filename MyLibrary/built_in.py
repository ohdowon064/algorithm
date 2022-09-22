# sum
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
# product -
# combination_with_replacement - 중복조합
import itertools
data = ["A", "B", "C", "D"]
print(list(itertools.permutations(data, 4)))