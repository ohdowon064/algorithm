line1 = "abbbcbbb"
line2 = "bbb"

chk_len = len(line1) - len(line2)
first = []
for i in range(len(line1)):
    if line1[i] == line2[0]:
        first.append(i)

chk = 0
l_set = set()

for l in range(chk_len):
    for i in first:
        ok = True

        for j in range(1, len(line2)):
            nx = i + l * j + j
            if nx >= len(line1):
                ok = False
                break

            if line1[nx] != line2[j]:
                ok = False
                break

        if ok:
            chk += 1

print(chk)


