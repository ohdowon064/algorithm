# from collections import Counter
# n = 1
# for _ in range(3):
#     n *= int(input())
#
# cnt = Counter(list(str(n)))
# for i in range(10):
#     if str(i) in cnt:
#         print(cnt[str(i)])
#     else:
#         print(0)

n = 1
for _ in range(3):
    n *= int(input())
numbers = list(map(int, str(n)))

for i in range(10):
    print(numbers.count(i))