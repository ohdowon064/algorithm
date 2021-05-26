# T = int(input())
# numbers = list(map(int, input().split()))
# min, max = float('inf'), float('-inf')
#
# for n in numbers:
#     if n < min:
#         min = n
#     if n > max:
#         max = n
# print(min, max)

T = int(input())
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers))