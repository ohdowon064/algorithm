chars = input()

count0 = 0
count1 = 0

if chars[0] == '0':
    count0 = 1
else:
    count1 = 1

for i in range(1, len(chars) - 1):
    if chars[i] != chars[i + 1]:
        if chars[i + 1] == '0':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))