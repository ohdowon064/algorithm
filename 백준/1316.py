N = int(input())
cnt = 0
for _ in range(N):
    s = input()
    is_group = True
    for char in s:
        removed = s.replace(char, '')
        if removed not in s:
            is_group = False
            break
    if is_group:
        cnt += 1


print(cnt)