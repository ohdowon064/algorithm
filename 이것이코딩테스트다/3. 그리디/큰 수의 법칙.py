n, m, k = map(int, input().split())
data = sorted(list(map(int, input().split())))
first, second = data[-1], data[-2]
result = 0

# j = 0
# for i in range(m):
#     if j == k:
#         result += second
#         j = 0
#         continue
#     result += first
#     j += 1
#
# print(result)

# O(1)
result += (m // (k + 1) * k + m % (k + 1)) * first
result += (m // (k + 1)) * second
print(result)