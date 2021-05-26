# numbers = [int(input()) for _ in range(9)]
# n = max(numbers)
# print(n, numbers.index(n) + 1, sep='\n')

numbers = [int(input()) for _ in range(9)]
max, max_idx = float('-inf'), 0
for i, n in enumerate(numbers):
    if n > max:
        max, max_idx = n, i

print(max)
print(max_idx + 1)
