numbers = list(map(int, input()))

result = numbers[0]
for number in numbers[1:]:
    if result == 0 or result == 1:
        result += number
    else:
        result *= number

print(result)