"""
입력값
0001100
"""
s = input()

count0 = 0
count1 = 0

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i] == "0":
            count0 += 1
        else:
            count1 += 1

if s[-1] == "0":
    count0 += 1
else:
    count1 += 1

print(count0, count1)