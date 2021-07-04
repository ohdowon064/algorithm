from collections import defaultdict
numbers = list(input())
data = defaultdict(list)

k = 1

for i in range(len(numbers)):
    if data[k] is None:
        data[k].append(numbers[i])
    elif numbers[i] in data[k] or data[k] and int(numbers[i]) < int(data[k][-1]):
        k = int(f'{k}0')
        data[k].append(numbers[i])
    else:
        data[k].append(numbers[i])

if k == 1:
    print(max(map(int, data[k])))
print(data)
max_num = max(map(int, data[k]))
print(k + max_num)
