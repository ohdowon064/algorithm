N = int(input())
cnt = 0

for _ in range(N):
    s = input()
    is_group = True
    chk = set()
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            if s[i + 1] in chk:
                is_group = False
                break
            else:
                chk.add(s[i])
    if is_group:
        cnt += 1

print(cnt)