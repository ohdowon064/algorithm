croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
cnt = 0
for char in croatia:
    cnt += s.count(char)
    s = s.replace(char, '$')

print(cnt + len(s.replace('$', '')))


