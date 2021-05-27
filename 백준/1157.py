from collections import Counter
s = Counter(input().lower())
# if len(s) == 1:
#     print(s.most_common(1)[0][0].upper())
# else:
#     a, b = s.most_common(2)
#     print('?' if a[1] == b[1] else a[0].upper())
try:
    a, b = s.most_common(2)
    print('?' if a[1] == b[1] else a[0].upper())
except:
    print(s.most_common()[0][0].upper())