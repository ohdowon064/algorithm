x = int(input())

i = 0
end = 0
while end < x:
    i += 1
    end += i

start = end - i + 1
if i % 2 == 0:
    col = i - (x - start)
    row = i - (end - x)

    print(f'{row}/{col}')
else:
    col = x - start + 1
    row = i - col + 1

    print(f'{row}/{col}')