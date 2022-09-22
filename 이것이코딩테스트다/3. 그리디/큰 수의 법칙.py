n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
print(n, m, k, numbers)
numbers.sort()
first, second = numbers[n-1], numbers[n-2]

# answer = 0
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         answer += first
#         m -= 1
#
#     if m == 0:
#         break
#
#     answer += second
#     m -= 1
#
# print(answer)

count = (m // (k + 1)) * k
count += m % (k + 1)

answer = count * first
answer += (m - count) * second
print(answer)