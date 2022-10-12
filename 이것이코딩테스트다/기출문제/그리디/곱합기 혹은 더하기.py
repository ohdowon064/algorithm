"""
입력값1
02984

입력값2
567
"""
numbers = list(map(int, input()))
result = numbers[0]

for number in numbers[1:]:
    if result == 0 or result == 1 or number == 0 or number == 1:
        result += number
    else:
        result *= number

print(result)